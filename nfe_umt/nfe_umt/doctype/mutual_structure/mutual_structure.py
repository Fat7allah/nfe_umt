import frappe
from frappe.model.document import Document
from frappe.utils import getdate

class MutualStructure(Document):
    def validate(self):
        self.validate_dates()
        self.validate_position()
        self.validate_member_count()
        
    def validate_dates(self):
        if self.end_date and getdate(self.start_date) > getdate(self.end_date):
            frappe.throw("تاريخ النهاية يجب أن يكون بعد تاريخ البداية")
            
    def validate_position(self):
        if self.structure_type == "المكتب التنفيذي":
            if not self.position:
                frappe.throw("المنصب مطلوب للمكتب التنفيذي")
            self.validate_executive_position()
            
    def validate_executive_position(self):
        if self.position == "الرئيس":
            existing = frappe.db.exists("Mutual Structure", {
                "structure_type": "المكتب التنفيذي",
                "position": "الرئيس",
                "is_active": 1,
                "name": ("!=", self.name)
            })
            if existing:
                frappe.throw("يوجد رئيس نشط بالفعل")
                
    def validate_member_count(self):
        structure_limits = {
            "المكتب التنفيذي": 10,
            "المجلس الإداري": 50,
            "الجمع العام": 260,
            "لجنة المراقبة": 5,
            "الثلث الخارج": 86
        }
        
        if self.is_active:
            current_count = frappe.db.count("Mutual Structure", {
                "structure_type": self.structure_type,
                "is_active": 1,
                "name": ("!=", self.name)
            })
            
            if current_count >= structure_limits.get(self.structure_type, 0):
                frappe.throw(f"تم تجاوز الحد الأقصى لعدد الأعضاء في {self.structure_type}")
