import frappe

def get_context(context):
    if frappe.session.user == 'Guest':
        frappe.local.flags.redirect_location = '/login'
        raise frappe.Redirect
        
    context.member = get_member_info()
    
def get_member_info():
    """Get member information for logged in user"""
    member = frappe.db.get_value('Member',
        {'email': frappe.session.user},
        ['name', 'full_name', 'phone', 'email', 'institution', 'education_level'],
        as_dict=1
    )
    return member

@frappe.whitelist()
def update_member_info(full_name, phone, email, institution, education_level):
    """Update member information"""
    if not frappe.session.user or frappe.session.user == 'Guest':
        frappe.throw('يرجى تسجيل الدخول للمتابعة')
        
    member = frappe.db.get_value('Member', {'email': frappe.session.user}, 'name')
    if not member:
        frappe.throw('لم يتم العثور على معلومات العضوية')
        
    # Update member document
    doc = frappe.get_doc('Member', member)
    doc.full_name = full_name
    doc.phone = phone
    doc.email = email
    doc.institution = institution
    doc.education_level = education_level
    
    try:
        doc.save()
        
        # Update user document if email changed
        if email != frappe.session.user:
            user = frappe.get_doc('User', frappe.session.user)
            user.email = email
            user.save()
            
        return {'message': 'تم تحديث المعلومات بنجاح'}
        
    except Exception as e:
        frappe.throw('حدث خطأ أثناء تحديث المعلومات: ' + str(e))
