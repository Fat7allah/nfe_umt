app_name = "nfe_umt"
app_title = "NFE UMT"
app_publisher = "NFE"
app_description = "National Federation of Education Management System"
app_email = "admin@nfe.ma"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
app_include_css = "/assets/nfe_umt/css/nfe_umt.bundle.css"
app_include_js = "/assets/nfe_umt/js/nfe_umt.bundle.js"

# include js, css files in header of web template
web_include_css = "/assets/nfe_umt/css/nfe_umt.bundle.css"
web_include_js = "/assets/nfe_umt/js/nfe_umt.bundle.js"

# Portal Menu Items
portal_menu_items = [
    {"label": "الأعضاء", "route": "/members", "role": "Member"},
    {"label": "بطاقات الإنخراط", "route": "/membership-cards", "role": "Member"},
    {"label": "هيكلة الجامعة", "route": "/federation-structure", "role": "Member"},
    {"label": "هيكلة التعاضدية", "route": "/mutual-structure", "role": "Member"},
    {"label": "المالية", "route": "/finance", "role": "Member"},
]

# Fixtures
fixtures = [
    {
        "doctype": "Custom Field",
        "filters": [
            [
                "name",
                "in",
                [
                    "Member-profession",
                    "Member-education_level",
                    "Member-gender",
                    "Member-role",
                    "Member-region"
                ]
            ]
        ]
    }
]

# Document Events
doc_events = {
    "Member": {
        "after_insert": "nfe_umt.nfe_umt.doctype.member.member.after_insert",
        "on_update": "nfe_umt.nfe_umt.doctype.member.member.on_update",
    },
    "Membership Card": {
        "before_insert": "nfe_umt.nfe_umt.doctype.membership_card.membership_card.before_insert",
        "on_update": "nfe_umt.nfe_umt.doctype.membership_card.membership_card.on_update",
    }
}

# Website Settings
website_context = {
    "brand_html": "NFE UMT",
    "top_bar_items": [
        {"label": "الرئيسية", "url": "/"},
        {"label": "الأعضاء", "url": "/members"},
        {"label": "اتصل بنا", "url": "/contact"}
    ]
}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
#	"methods": "nfe_umt.utils.jinja_methods",
#	"filters": "nfe_umt.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "nfe_umt.install.before_install"
# after_install = "nfe_umt.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "nfe_umt.uninstall.before_uninstall"
# after_uninstall = "nfe_umt.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "nfe_umt.utils.before_app_install"
# after_app_install = "nfe_umt.utils.after_app_install"

# Integration Cleanup
# ------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "nfe_umt.utils.before_app_uninstall"
# after_app_uninstall = "nfe_umt.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "nfe_umt.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
#	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
#	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
#	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
#	"all": [
#		"nfe_umt.tasks.all"
#	],
#	"daily": [
#		"nfe_umt.tasks.daily"
#	],
#	"hourly": [
#		"nfe_umt.tasks.hourly"
#	],
#	"weekly": [
#		"nfe_umt.tasks.weekly"
#	],
#	"monthly": [
#		"nfe_umt.tasks.monthly"
#	],
# }

# Testing
# -------

# before_tests = "nfe_umt.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
#	"frappe.desk.doctype.event.event.get_events": "nfe_umt.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
#	"Task": "nfe_umt.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["nfe_umt.utils.before_request"]
# after_request = ["nfe_umt.utils.after_request"]

# Job Events
# ----------
# before_job = ["nfe_umt.utils.before_job"]
# after_job = ["nfe_umt.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
#	{
#		"doctype": "{doctype_1}",
#		"filter_by": "{filter_by}",
#		"redact_fields": ["{field_1}", "{field_2}"],
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_2}",
#		"filter_by": "{filter_by}",
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_3}",
#		"strict": False,
#	},
#	{
#		"doctype": "{doctype_4}"
#	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
#	"nfe_umt.auth.validate"
# ]
