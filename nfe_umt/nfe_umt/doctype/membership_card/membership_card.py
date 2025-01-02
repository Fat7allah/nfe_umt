import frappe
from frappe.model.document import Document
from frappe.utils import getdate

class MembershipCard(Document):
    def validate(self):
        self.validate_dates()
        self.validate_card_number()
        
    def validate_dates(self):
        if getdate(self.start_date) > getdate(self.end_date):
            frappe.throw("تاريخ الانتهاء يجب أن يكون بعد تاريخ الإنخراط")
            
    def validate_card_number(self):
        if not self.card_number:
            frappe.throw("رقم البطاقة مطلوب")
            
    def before_insert(self):
        self.check_existing_active_card()
        
    def check_existing_active_card(self):
        existing_card = frappe.db.exists(
            "Membership Card",
            {
                "member": self.member,
                "docstatus": 1,
                "end_date": (">", self.start_date)
            }
        )
        if existing_card:
            frappe.throw("يوجد بطاقة نشطة لهذا العضو")
