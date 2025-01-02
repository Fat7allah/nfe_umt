import frappe
from frappe.utils import today, add_years

def get_context(context):
    if frappe.session.user == 'Guest':
        frappe.local.flags.redirect_location = '/login'
        raise frappe.Redirect
        
    context.member = get_member_info()
    
def get_member_info():
    """Get member information for logged in user"""
    member = frappe.db.get_value('Member',
        {'email': frappe.session.user},
        ['name', 'full_name', 'profession', 'institution', 'region'],
        as_dict=1
    )
    return member

@frappe.whitelist()
def create_card_request():
    """Create a new membership card request"""
    if not frappe.session.user or frappe.session.user == 'Guest':
        frappe.throw('يرجى تسجيل الدخول للمتابعة')
        
    member = frappe.db.get_value('Member', {'email': frappe.session.user}, 'name')
    if not member:
        frappe.throw('لم يتم العثور على معلومات العضوية')
        
    # Check if member has any pending card requests
    existing_request = frappe.db.exists('Membership Card',
        {
            'member': member,
            'status': 'غير المؤداة',
            'membership_date': ['>=', today()]
        }
    )
    
    if existing_request:
        frappe.throw('لديك طلب بطاقة عضوية معلق')
        
    try:
        # Generate new card number
        last_card = frappe.db.get_value('Membership Card',
            {'member': member},
            'card_number',
            order_by='creation desc'
        )
        
        new_number = 1
        if last_card:
            try:
                new_number = int(last_card.split('-')[-1]) + 1
            except:
                pass
                
        card_number = f"{member}-{new_number:04d}"
        
        # Create new membership card
        card = frappe.get_doc({
            'doctype': 'Membership Card',
            'member': member,
            'membership_date': today(),
            'expiry_date': add_years(today(), 1),
            'card_number': card_number,
            'status': 'غير المؤداة'
        })
        card.insert()
        
        # Send email notification to admin
        send_admin_notification(card)
        
        return {'message': 'تم تقديم طلب البطاقة بنجاح'}
        
    except Exception as e:
        frappe.throw('حدث خطأ أثناء تقديم الطلب: ' + str(e))
        
def send_admin_notification(card):
    """Send email notification to admin"""
    try:
        member = frappe.get_doc('Member', card.member)
        
        subject = f"طلب بطاقة عضوية جديد - {member.full_name}"
        message = f"""
        تم تقديم طلب بطاقة عضوية جديد:
        
        الإسم: {member.full_name}
        المهنة: {member.profession}
        المؤسسة: {member.institution}
        الإقليم: {member.region}
        رقم البطاقة: {card.card_number}
        
        يرجى مراجعة الطلب من خلال نظام إدارة العضوية.
        """
        
        frappe.sendmail(
            recipients=['admin@nfe.ma'],
            subject=subject,
            message=message
        )
        
    except:
        pass # Don't let email errors affect the request process
