app_name = "nfe_umt"
app_title = "NFE UMT"
app_publisher = "NFE"
app_description = "National Federation of Education Management System"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "admin@nfe.ma"
app_license = "MIT"
app_version = "0.0.1"

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
