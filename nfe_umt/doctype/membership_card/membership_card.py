import frappe
from frappe.model.document import Document
from frappe.utils import getdate, add_years

class MembershipCard(Document):
    def validate(self):
        self.validate_dates()
        self.validate_card_number()
        
    def validate_dates(self):
        """Validate membership dates"""
        if getdate(self.membership_date) > getdate(self.expiry_date):
            frappe.throw("تاريخ الانتهاء يجب أن يكون بعد تاريخ الإنخراط")
            
        # Set expiry date to one year from membership date if not set
        if not self.expiry_date:
            self.expiry_date = add_years(getdate(self.membership_date), 1)
            
    def validate_card_number(self):
        """Validate card number format and uniqueness"""
        if not self.card_number:
            frappe.throw("رقم البطاقة مطلوب")
            
        # Check if card number exists for another card
        if frappe.db.exists("Membership Card", {
            "card_number": self.card_number,
            "name": ("!=", self.name)
        }):
            frappe.throw("رقم البطاقة موجود مسبقا")
            
    def before_insert(self):
        """Set default values before insert"""
        if not self.membership_date:
            self.membership_date = frappe.utils.today()
            
    def on_update(self):
        """Update member's active card status"""
        frappe.db.set_value("Member", self.member, "active_card", self.name if self.status == "المؤداة" else None)
        
    def has_website_permission(self, ptype, user=None, verbose=False):
        """Check if user has permission to access this document on the website"""
        if not user:
            return False
            
        if "System Manager" in frappe.get_roles(user):
            return True
            
        member = frappe.db.get_value("Member", self.member, "email")
        return user == member
