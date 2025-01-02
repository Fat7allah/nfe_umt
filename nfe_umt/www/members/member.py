import frappe

def get_context(context):
    context.no_cache = 1
    
    if frappe.session.user == 'Guest':
        frappe.local.flags.redirect_location = '/login'
        raise frappe.Redirect
        
    member_name = frappe.form_dict.member
    
    if not member_name:
        frappe.local.flags.redirect_location = '/members'
        raise frappe.Redirect
        
    context.doc = frappe.get_doc('Member', member_name)
    context.membership_cards = get_membership_cards(member_name)
    
def get_membership_cards(member_name):
    return frappe.get_all('Membership Card',
        fields=['card_number', 'start_date', 'end_date', 'status'],
        filters={
            'member': member_name,
            'docstatus': 1
        },
        order_by='start_date desc'
    )
