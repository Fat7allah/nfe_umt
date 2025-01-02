import frappe
from frappe.model.document import Document
from frappe.utils import today

class Member(Document):
    def validate(self):
        self.validate_phone()
        self.validate_email()
        
    def validate_phone(self):
        """Validate phone number format"""
        if not self.phone or len(self.phone) < 10:
            frappe.throw("رقم الهاتف غير صحيح")
            
    def validate_email(self):
        """Validate email format if provided"""
        if self.email and not frappe.utils.validate_email_address(self.email):
            frappe.throw("البريد الإلكتروني غير صحيح")
            
    def after_insert(self):
        """Create user account for member"""
        if self.email:
            self.create_user()
            
    def create_user(self):
        """Create a user account for the member"""
        if not frappe.db.exists("User", self.email):
            user = frappe.get_doc({
                "doctype": "User",
                "email": self.email,
                "first_name": self.full_name,
                "send_welcome_email": 1,
                "roles": [{"role": "NFE Member"}]
            })
            user.insert(ignore_permissions=True)
            
    def has_website_permission(self, ptype, user=None, verbose=False):
        """Check if user has permission to access this document on the website"""
        if not user:
            return False
        
        if "System Manager" in frappe.get_roles(user):
            return True
            
        return user == self.email
