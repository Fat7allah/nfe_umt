import frappe
from frappe.model.document import Document

class MutualStructure(Document):
    def validate(self):
        self.validate_member()
        self.validate_structure_limits()
        self.validate_position()
        
    def validate_member(self):
        """Validate member has active membership"""
        active_card = frappe.db.get_value("Member", self.member, "active_card")
        if not active_card:
            frappe.throw("العضو يجب أن يكون لديه بطاقة عضوية نشطة")
            
    def validate_structure_limits(self):
        """Validate structure member limits"""
        structure_limits = {
            "المكتب التنفيذي": 10,
            "المجلس الإداري": 50,
            "الجمع العام": 260,
            "لجنة المراقبة": 5,
            "الثلث الخارج": 86
        }
        
        current_count = frappe.db.count("Mutual Structure", {
            "structure_type": self.structure_type,
            "name": ("!=", self.name)
        })
        
        if current_count >= structure_limits.get(self.structure_type, 0):
            frappe.throw(f"تم تجاوز الحد الأقصى لعدد الأعضاء في {self.structure_type}")
            
    def validate_position(self):
        """Validate position based on structure type"""
        if self.structure_type == "المكتب التنفيذي" and not self.position:
            frappe.throw("المنصب مطلوب لأعضاء المكتب التنفيذي")
            
        executive_positions = [
            "الرئيس",
            "نائب الرئيس",
            "الكاتب العام",
            "نائب الكاتب العام",
            "أمين المال",
            "نائب أمين المال",
            "مستشار"
        ]
        
        if self.structure_type == "المكتب التنفيذي" and self.position not in executive_positions:
            frappe.throw("المنصب غير متوافق مع المكتب التنفيذي")
            
    def on_update(self):
        """Update member's role in the mutual"""
        self.update_member_role()
        
    def update_member_role(self):
        """Update member's mutual role"""
        member = frappe.get_doc("Member", self.member)
        if self.structure_type == "المكتب التنفيذي":
            member.mutual_role = f"عضو المكتب التنفيذي - {self.position}"
        elif self.structure_type == "المجلس الإداري":
            member.mutual_role = "عضو المجلس الإداري"
        elif self.structure_type == "لجنة المراقبة":
            member.mutual_role = "عضو لجنة المراقبة"
        member.save()
