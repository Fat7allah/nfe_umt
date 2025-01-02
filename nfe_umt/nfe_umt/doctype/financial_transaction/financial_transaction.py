import frappe
from frappe.model.document import Document
from frappe.utils import getdate, flt

class FinancialTransaction(Document):
    def validate(self):
        self.validate_amount()
        self.validate_reference()
        
    def validate_amount(self):
        if flt(self.amount) <= 0:
            frappe.throw("المبلغ يجب أن يكون أكبر من صفر")
            
    def validate_reference(self):
        if self.reference_type and not self.reference_name:
            frappe.throw("الرجاء تحديد اسم المرجع")
        elif self.reference_name and not self.reference_type:
            frappe.throw("الرجاء تحديد نوع المرجع")
            
        if self.reference_type and self.reference_name:
            if not frappe.db.exists(self.reference_type, self.reference_name):
                frappe.throw(f"المرجع {self.reference_name} غير موجود")
                
    def on_submit(self):
        self.update_membership_card()
                
    def update_membership_card(self):
        if self.reference_type == "Membership Card" and self.reference_name:
            card = frappe.get_doc("Membership Card", self.reference_name)
            if self.transaction_type == "مدخول":
                card.status = "المؤداة"
            else:
                card.status = "غير المؤداة"
            card.save()
