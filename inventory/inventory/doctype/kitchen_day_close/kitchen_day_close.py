# -*- coding: utf-8 -*-
# Copyright (c) 2015, Wayzon and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class KitchenDayClose(Document):
	def validate(self):
		d=self.date
		q1=frappe.db.sql("""select date from `tabKitchen Day Close` where date=%s""",(d))
		if q1:
			frappe.throw("Cannot Save Duplicate Date")
		else:
			s=frappe.db.sql("""select item_name, item_code, quantity,uom from `tabKitchen Stock`""")
			j=len(s)
			for i in range (0, j):
				n=frappe.db.sql("""select max(cast(name as int)) from `tabKitchenDayCloseInfo`""")[0][0]
				if n:
					name=int(n)+1
				else:
					name=1
				q=frappe.db.sql("""insert into `tabKitchenDayCloseInfo` 
				set name=%s, date=%s, item_name=%s, item_code=%s, closing_stock=%s,uom=%s""",(name,d,s[i][0],s[i][1],s[i][2],s[i][3]))
