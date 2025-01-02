import frappe
from frappe.model.document import Document
from frappe.utils import getdate

class FederationStructure(Document):
    def validate(self):
        self.validate_dates()
        self.validate_position()
        self.validate_member_uniqueness()
        
    def validate_dates(self):
        if self.end_date and getdate(self.start_date) > getdate(self.end_date):
            frappe.throw("تاريخ النهاية يجب أن يكون بعد تاريخ البداية")
            
    def validate_position(self):
        if self.structure_type == "المكتب التنفيذي":
            self.validate_executive_office()
        elif self.structure_type in ["المكاتب الجهوية", "المكاتب الإقليمية", "المكاتب المحلية"]:
            self.validate_regional_office()
            
    def validate_executive_office(self):
        if self.position == "الكاتب الوطني":
            existing = frappe.db.exists("Federation Structure", {
                "structure_type": "المكتب التنفيذي",
                "position": "الكاتب الوطني",
                "is_active": 1,
                "name": ("!=", self.name)
            })
            if existing:
                frappe.throw("يوجد كاتب وطني نشط بالفعل")
                
    def validate_regional_office(self):
        if not self.office_type:
            frappe.throw("اسم المكتب مطلوب")
            
    def validate_member_uniqueness(self):
        existing = frappe.db.exists("Federation Structure", {
            "member": self.member,
            "structure_type": self.structure_type,
            "office_type": self.office_type,
            "is_active": 1,
            "name": ("!=", self.name)
        })
        if existing:
            frappe.throw("العضو لديه بالفعل منصب نشط في نفس المكتب")
