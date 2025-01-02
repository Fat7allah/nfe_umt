import frappe
from frappe.model.document import Document

class UniversityStructure(Document):
    def validate(self):
        self.validate_member()
        self.validate_position()
        
    def validate_member(self):
        """Validate member has active membership"""
        active_card = frappe.db.get_value("Member", self.member, "active_card")
        if not active_card:
            frappe.throw("العضو يجب أن يكون لديه بطاقة عضوية نشطة")
            
    def validate_position(self):
        """Validate position based on structure type"""
        executive_positions = [
            "الكاتب الوطني",
            "نائب الكاتب الوطني",
            "الكاتب العام",
            "نائب الكاتب العام",
            "أمين المال",
            "نائب أمين المال",
            "مستشار",
            "مكلف بمهمة"
        ]
        
        regional_positions = [
            "الكاتب الجهوي",
            "نائب الكاتب الجهوي",
            "الكاتب العام",
            "نائب الكاتب العام",
            "أمين المال",
            "نائب أمين المال",
            "مستشار",
            "مكلف بمهمة"
        ]
        
        local_positions = [
            "الكاتب المحلي",
            "نائب الكاتب المحلي",
            "الكاتب العام",
            "نائب الكاتب العام",
            "أمين المال",
            "نائب أمين المال",
            "مستشار",
            "مكلف بمهمة"
        ]
        
        if self.structure_type == "المكتب التنفيذي" and self.position not in executive_positions:
            frappe.throw("المنصب غير متوافق مع المكتب التنفيذي")
            
        elif self.structure_type in ["المكاتب الجهوية", "المكاتب الإقليمية"] and self.position not in regional_positions:
            frappe.throw("المنصب غير متوافق مع المكتب الجهوي/الإقليمي")
            
        elif self.structure_type == "المكاتب المحلية" and self.position not in local_positions:
            frappe.throw("المنصب غير متوافق مع المكتب المحلي")
            
    def on_update(self):
        """Update member's role in the organization"""
        self.update_member_role()
        
    def update_member_role(self):
        """Update member's organizational role"""
        member = frappe.get_doc("Member", self.member)
        if self.structure_type == "المكتب التنفيذي":
            member.organizational_role = "عضو المكتب التنفيذي"
        elif self.structure_type == "المكاتب الجهوية":
            member.organizational_role = "عضو المكتب الجهوي"
        elif self.structure_type == "المكاتب الإقليمية":
            member.organizational_role = "عضو المكتب الإقليمي"
        elif self.structure_type == "المكاتب المحلية":
            member.organizational_role = "عضو المكتب المحلي"
        member.save()
