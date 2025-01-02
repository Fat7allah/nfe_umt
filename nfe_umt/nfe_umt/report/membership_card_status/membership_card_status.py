import frappe
from frappe import _

def execute(filters=None):
    columns = get_columns()
    data = get_data(filters)
    return columns, data

def get_columns():
    return [
        {
            "fieldname": "institution",
            "label": _("المؤسسة/الفرع"),
            "fieldtype": "Data",
            "width": 200
        },
        {
            "fieldname": "total_cards",
            "label": _("مجموع البطائق"),
            "fieldtype": "Int",
            "width": 120
        },
        {
            "fieldname": "paid_cards",
            "label": _("البطائق المؤداة"),
            "fieldtype": "Int",
            "width": 120
        },
        {
            "fieldname": "unpaid_cards",
            "label": _("البطائق غير المؤداة"),
            "fieldtype": "Int",
            "width": 120
        },
        {
            "fieldname": "payment_rate",
            "label": _("نسبة الأداء (%)"),
            "fieldtype": "Percent",
            "width": 120
        }
    ]

def get_data(filters):
    data = []
    
    # Get all unique institutions
    institutions = frappe.db.sql("""
        SELECT DISTINCT m.institution
        FROM `tabMember` m
        INNER JOIN `tabMembership Card` mc ON mc.member = m.name
        WHERE mc.docstatus = 1
        ORDER BY m.institution
    """, as_dict=1)
    
    for inst in institutions:
        # Get card statistics for each institution
        stats = frappe.db.sql("""
            SELECT 
                COUNT(*) as total_cards,
                SUM(CASE WHEN mc.status = 'المؤداة' THEN 1 ELSE 0 END) as paid_cards,
                SUM(CASE WHEN mc.status = 'غير المؤداة' THEN 1 ELSE 0 END) as unpaid_cards
            FROM `tabMember` m
            INNER JOIN `tabMembership Card` mc ON mc.member = m.name
            WHERE mc.docstatus = 1 AND m.institution = %s
        """, inst.institution, as_dict=1)[0]
        
        # Calculate payment rate
        payment_rate = (stats.paid_cards / stats.total_cards * 100) if stats.total_cards > 0 else 0
        
        data.append({
            "institution": inst.institution,
            "total_cards": stats.total_cards,
            "paid_cards": stats.paid_cards,
            "unpaid_cards": stats.unpaid_cards,
            "payment_rate": payment_rate
        })
    
    return data
