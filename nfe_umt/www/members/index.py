import frappe

def get_context(context):
    context.no_cache = 1
    
    if not frappe.session.user == 'Guest':
        context.members = get_members()
    else:
        frappe.local.flags.redirect_location = '/login'
        raise frappe.Redirect
        
def get_members():
    return frappe.get_all('Member',
        fields=['name', 'name1', 'profession', 'institution', 'region', 'enabled'],
        filters={'enabled': 1},
        order_by='name1 asc'
    )
