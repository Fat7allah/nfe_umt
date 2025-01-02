import frappe
from frappe.model.document import Document

class Member(Document):
    def validate(self):
        self.validate_email()
        self.validate_phone()
        
    def validate_email(self):
        if self.email:
            if not frappe.utils.validate_email_address(self.email):
                frappe.throw("البريد الإلكتروني غير صالح")
                
    def validate_phone(self):
        if not self.phone or len(self.phone) < 10:
            frappe.throw("رقم الهاتف غير صالح")
            
    def after_insert(self):
        self.create_user()
        
    def create_user(self):
        if self.email:
            if not frappe.db.exists("User", self.email):
                user = frappe.get_doc({
                    "doctype": "User",
                    "email": self.email,
                    "first_name": self.name1,
                    "send_welcome_email": 1,
                    "roles": [{"role": "NFE Member"}]
                })
                user.insert(ignore_permissions=True)
                
    def on_update(self):
        self.update_user()
                
    def update_user(self):
        if self.email:
            user = frappe.get_doc("User", self.email)
            user.first_name = self.name1
            user.enabled = self.enabled
            user.save(ignore_permissions=True)
