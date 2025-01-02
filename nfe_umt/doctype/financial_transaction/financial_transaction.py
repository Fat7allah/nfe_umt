import frappe
from frappe.model.document import Document
from frappe.utils import getdate

class FinancialTransaction(Document):
    def validate(self):
        self.validate_amount()
        self.validate_related_documents()
        
    def validate_amount(self):
        """Validate transaction amount"""
        if self.amount <= 0:
            frappe.throw("المبلغ يجب أن يكون أكبر من صفر")
            
    def validate_related_documents(self):
        """Validate related member and card"""
        if self.related_member:
            if not frappe.db.exists("Member", self.related_member):
                frappe.throw("العضو المرتبط غير موجود")
                
        if self.related_card:
            if not frappe.db.exists("Membership Card", self.related_card):
                frappe.throw("البطاقة المرتبطة غير موجودة")
                
            # Validate card belongs to related member
            if self.related_member:
                card_member = frappe.db.get_value("Membership Card", self.related_card, "member")
                if card_member != self.related_member:
                    frappe.throw("البطاقة المرتبطة لا تنتمي للعضو المحدد")
                    
    def on_submit(self):
        """Update related documents on submission"""
        if self.related_card and self.transaction_type == "مدخول":
            self.update_card_status()
            
    def update_card_status(self):
        """Update membership card status"""
        card = frappe.get_doc("Membership Card", self.related_card)
        card.status = "المؤداة"
        card.save()
        
    @frappe.whitelist()
    def get_balance_report(start_date=None, end_date=None):
        """Get financial balance report"""
        filters = {}
        if start_date:
            filters["date"] = [">=", getdate(start_date)]
        if end_date:
            filters["date"] = ["<=", getdate(end_date)]
            
        income = frappe.db.get_all(
            "Financial Transaction",
            filters={"transaction_type": "مدخول", **filters},
            fields=["sum(amount) as total"]
        )[0].total or 0
        
        expenses = frappe.db.get_all(
            "Financial Transaction",
            filters={"transaction_type": "مصروف", **filters},
            fields=["sum(amount) as total"]
        )[0].total or 0
        
        return {
            "income": income,
            "expenses": expenses,
            "balance": income - expenses
        }
