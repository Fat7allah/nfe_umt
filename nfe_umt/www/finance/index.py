import frappe
from frappe import _
from frappe.utils import flt

def get_context(context):
    context.no_cache = 1
    
    if frappe.session.user == 'Guest':
        frappe.local.flags.redirect_location = '/login'
        raise frappe.Redirect
        
    if not frappe.has_permission("Financial Transaction", "read"):
        frappe.throw(_("Not permitted"), frappe.PermissionError)
        
    context.total_income = get_total_income()
    context.total_expenses = get_total_expenses()
    context.balance = context.total_income - context.total_expenses
    
    context.card_status = get_card_status()
    context.recent_income = get_recent_transactions("مدخول")
    context.recent_expenses = get_recent_transactions("مصروف")
    
def get_total_income():
    result = frappe.db.sql("""
        SELECT COALESCE(SUM(amount), 0) as total
        FROM `tabFinancial Transaction`
        WHERE transaction_type = 'مدخول'
        AND docstatus = 1
    """, as_dict=1)
    return flt(result[0].total)
    
def get_total_expenses():
    result = frappe.db.sql("""
        SELECT COALESCE(SUM(amount), 0) as total
        FROM `tabFinancial Transaction`
        WHERE transaction_type = 'مصروف'
        AND docstatus = 1
    """, as_dict=1)
    return flt(result[0].total)
    
def get_card_status():
    branches = frappe.db.sql("""
        SELECT DISTINCT institution as name
        FROM `tabMember`
        WHERE enabled = 1
        ORDER BY institution
    """, as_dict=1)
    
    for branch in branches:
        stats = frappe.db.sql("""
            SELECT 
                COUNT(*) as total_cards,
                SUM(CASE WHEN mc.status = 'المؤداة' THEN 1 ELSE 0 END) as paid_cards,
                SUM(CASE WHEN mc.status = 'غير المؤداة' THEN 1 ELSE 0 END) as unpaid_cards,
                SUM(CASE WHEN mc.status = 'المؤداة' THEN ft.amount ELSE 0 END) as total_amount
            FROM `tabMember` m
            INNER JOIN `tabMembership Card` mc ON mc.member = m.name
            LEFT JOIN `tabFinancial Transaction` ft ON ft.reference_type = 'Membership Card' 
                AND ft.reference_name = mc.name
                AND ft.docstatus = 1
            WHERE m.institution = %s
            AND mc.docstatus = 1
        """, branch.name, as_dict=1)[0]
        
        branch.update({
            "total_cards": stats.total_cards or 0,
            "paid_cards": stats.paid_cards or 0,
            "unpaid_cards": stats.unpaid_cards or 0,
            "payment_rate": (stats.paid_cards / stats.total_cards * 100) if stats.total_cards else 0,
            "total_amount": stats.total_amount or 0
        })
    
    return branches
    
def get_recent_transactions(transaction_type, limit=5):
    return frappe.get_all(
        "Financial Transaction",
        filters={
            "transaction_type": transaction_type,
            "docstatus": 1
        },
        fields=["date", "name1", "amount"],
        order_by="date desc",
        limit=limit
    )
