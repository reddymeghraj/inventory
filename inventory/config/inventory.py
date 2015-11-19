from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"label": _("Documents"),
			"icon": "icon-star",
			"items": [
				{
					"type": "doctype",
					"name": "Kitchen Day Close",
					"description": _("Kitchen day closing")
				},
				{
					"type": "doctype",
					"name": "Counter Day Close",
					"description": _("Counter Day Closing")
				},
			]
		},
		
	]