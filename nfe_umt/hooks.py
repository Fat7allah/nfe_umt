app_name = "nfe_umt"
app_title = "الجامعة الوطنية للتعليم"
app_publisher = "NFE"
app_description = "نظام إدارة الجامعة الوطنية للتعليم"
app_icon = "octicon octicon-organization"
app_color = "blue"
app_email = "support@nfe.ma"
app_license = "MIT"

# Document Events
doc_events = {
    "Member": {
        "after_insert": "nfe_umt.nfe_umt.doctype.member.member.after_member_insert",
        "on_update": "nfe_umt.nfe_umt.doctype.member.member.on_member_update",
    },
    "Membership Card": {
        "before_insert": "nfe_umt.nfe_umt.doctype.membership_card.membership_card.before_card_insert",
        "on_update": "nfe_umt.nfe_umt.doctype.membership_card.membership_card.on_card_update",
    }
}

# Website Settings
website_context = {
    "favicon": "/assets/nfe_umt/images/favicon.ico",
    "splash_image": "/assets/nfe_umt/images/splash.png"
}

# Portal Settings
has_website_permission = {
    "Member": "nfe_umt.nfe_umt.doctype.member.member.has_website_permission",
}

portal_menu_items = [
    {"title": "بوابة الأعضاء", "route": "/member-portal", "reference_doctype": "Member"},
    {"title": "تحديث المعلومات", "route": "/update-profile", "reference_doctype": "Member"},
    {"title": "طلب بطاقة عضوية", "route": "/request-card", "reference_doctype": "Member"}
]

# Portal Home Page
website_route_rules = [
    {"from_route": "/member-portal", "to_route": "member_portal"},
    {"from_route": "/update-profile", "to_route": "update_profile"},
    {"from_route": "/request-card", "to_route": "request_card"}
]

# Custom CSS/JS
app_include_css = [
    "/assets/nfe_umt/css/nfe_umt.css"
]

app_include_js = [
    "/assets/nfe_umt/js/nfe_umt.js"
]

# Fixtures
fixtures = [
    {
        "doctype": "Role",
        "filters": [
            ["name", "in", ["NFE Manager", "NFE Member"]]
        ]
    },
    {
        "doctype": "Custom DocPerm",
        "filters": [
            ["role", "in", ["NFE Manager", "NFE Member"]]
        ]
    }
]
