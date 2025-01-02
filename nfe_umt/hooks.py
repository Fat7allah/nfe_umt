app_name = "nfe_umt"
app_title = "NFE UMT"
app_publisher = "NFE"
app_description = "National Federation of Education Management System"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "admin@nfe.ma"
app_license = "MIT"
app_version = "0.0.1"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
app_include_css = "/assets/nfe_umt/css/nfe_umt.css"
app_include_js = "/assets/nfe_umt/js/nfe_umt.js"

# include js, css files in header of web template
web_include_css = "/assets/nfe_umt/css/nfe_umt.css"
web_include_js = "/assets/nfe_umt/js/nfe_umt.js"

# Portal Menu Items
portal_menu_items = [
    {
        "title": "الأعضاء",
        "route": "/members",
        "reference_doctype": "Member",
        "role": "NFE Member"
    },
    {
        "title": "بطاقات الإنخراط",
        "route": "/membership-cards",
        "reference_doctype": "Membership Card",
        "role": "NFE Member"
    },
    {
        "title": "هيكلة الجامعة",
        "route": "/federation-structure",
        "role": "NFE Member"
    },
    {
        "title": "هيكلة التعاضدية",
        "route": "/mutual-structure",
        "role": "NFE Member"
    },
    {
        "title": "التقرير المالي",
        "route": "/finance",
        "role": "NFE Admin"
    }
]

# Website Route Rules
website_route_rules = [
    {"from_route": "/members", "to_route": "members"},
    {"from_route": "/membership-cards", "to_route": "membership-cards"},
    {"from_route": "/federation-structure", "to_route": "federation-structure"},
    {"from_route": "/mutual-structure", "to_route": "mutual-structure"},
    {"from_route": "/finance", "to_route": "finance"}
]

# Website Menu Items
website_menu_items = [
    {
        "label": "الرئيسية",
        "url": "/",
        "right": True
    },
    {
        "label": "الأعضاء",
        "url": "/members",
        "right": True
    },
    {
        "label": "هيكلة الجامعة",
        "url": "/federation-structure",
        "right": True
    },
    {
        "label": "هيكلة التعاضدية",
        "url": "/mutual-structure",
        "right": True
    },
    {
        "label": "اتصل بنا",
        "url": "/contact",
        "right": True
    }
]

# DocType Event Handlers
doc_events = {
    "Member": {
        "after_insert": "nfe_umt.nfe_umt.doctype.member.member.after_insert",
        "on_update": "nfe_umt.nfe_umt.doctype.member.member.on_update"
    },
    "Membership Card": {
        "on_submit": "nfe_umt.nfe_umt.doctype.membership_card.membership_card.on_submit",
        "on_cancel": "nfe_umt.nfe_umt.doctype.membership_card.membership_card.on_cancel"
    },
    "Financial Transaction": {
        "on_submit": "nfe_umt.nfe_umt.doctype.financial_transaction.financial_transaction.on_submit",
        "on_cancel": "nfe_umt.nfe_umt.doctype.financial_transaction.financial_transaction.on_cancel"
    }
}
