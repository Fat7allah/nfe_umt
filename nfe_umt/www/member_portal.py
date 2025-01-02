import frappe

def get_context(context):
    if frappe.session.user == 'Guest':
        frappe.local.flags.redirect_location = '/login'
        raise frappe.Redirect
        
    context.member = get_member_info()
    context.cards = get_membership_cards()
    context.positions = get_member_positions()
    
def get_member_info():
    """Get member information for logged in user"""
    member = frappe.db.get_value('Member',
        {'email': frappe.session.user},
        ['name', 'full_name', 'profession', 'institution', 'region'],
        as_dict=1
    )
    return member

def get_membership_cards():
    """Get membership cards for the logged in member"""
    if not frappe.db.exists('Member', {'email': frappe.session.user}):
        return []
        
    member = frappe.db.get_value('Member', {'email': frappe.session.user}, 'name')
    cards = frappe.get_all('Membership Card',
        filters={'member': member},
        fields=['card_number', 'membership_date', 'expiry_date', 'status'],
        order_by='membership_date desc'
    )
    return cards

def get_member_positions():
    """Get organizational positions for the logged in member"""
    if not frappe.db.exists('Member', {'email': frappe.session.user}):
        return []
        
    member = frappe.db.get_value('Member', {'email': frappe.session.user}, 'name')
    
    # Get university structure positions
    uni_positions = frappe.get_all('University Structure',
        filters={'member': member},
        fields=['structure_type', 'position', 'sub_position', 'region']
    )
    
    # Get mutual structure positions
    mutual_positions = frappe.get_all('Mutual Structure',
        filters={'member': member},
        fields=['structure_type', 'position', 'sub_position']
    )
    
    return uni_positions + mutual_positions
