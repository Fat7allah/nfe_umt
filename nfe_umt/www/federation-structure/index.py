import frappe
from frappe import _

def get_context(context):
    context.no_cache = 1
    
    if frappe.session.user == 'Guest':
        frappe.local.flags.redirect_location = '/login'
        raise frappe.Redirect
        
    context.structure_types = [
        {"key": "executive", "label": "المكتب التنفيذي"},
        {"key": "regional", "label": "المكاتب الجهوية"},
        {"key": "local", "label": "المكاتب المحلية"},
        {"key": "members", "label": "أعضاء الفروع"}
    ]
    
    context.executive_members = get_executive_members()
    context.regional_offices = get_regional_offices()
    context.local_offices = get_local_offices()
    context.branch_members = get_branch_members()
    
def get_executive_members():
    executive_members = {
        "national_secretary": [],
        "general_secretary": [],
        "treasurer": [],
        "advisors": []
    }
    
    members = frappe.get_all(
        "Federation Structure",
        filters={
            "structure_type": "المكتب التنفيذي",
            "is_active": 1
        },
        fields=["member", "position"]
    )
    
    for member in members:
        member_doc = frappe.get_doc("Member", member.member)
        member_info = {
            "member_name": member_doc.name1,
            "profession": member_doc.profession,
            "institution": member_doc.institution
        }
        
        if member.position == "الكاتب الوطني":
            executive_members["national_secretary"].append(member_info)
        elif member.position == "الكاتب العام":
            executive_members["general_secretary"].append(member_info)
        elif member.position == "أمين المال":
            executive_members["treasurer"].append(member_info)
        elif member.position in ["مستشار", "مكلف بمهمة"]:
            executive_members["advisors"].append(member_info)
            
    return executive_members

def get_regional_offices():
    offices = []
    
    regional_structures = frappe.get_all(
        "Federation Structure",
        filters={
            "structure_type": "المكاتب الجهوية",
            "is_active": 1
        },
        fields=["office_type", "member", "position"],
        order_by="office_type"
    )
    
    current_office = None
    
    for structure in regional_structures:
        if not current_office or current_office["name"] != structure.office_type:
            if current_office:
                offices.append(current_office)
            current_office = {
                "name": structure.office_type,
                "secretary": None,
                "treasurer": None,
                "members": []
            }
            
        member_doc = frappe.get_doc("Member", structure.member)
        member_info = {
            "member_name": member_doc.name1,
            "position": structure.position,
            "profession": member_doc.profession,
            "institution": member_doc.institution
        }
        
        if structure.position == "الكاتب الجهوي":
            current_office["secretary"] = member_info
        elif structure.position == "أمين المال":
            current_office["treasurer"] = member_info
        else:
            current_office["members"].append(member_info)
            
    if current_office:
        offices.append(current_office)
        
    return offices

def get_local_offices():
    # Similar to get_regional_offices but for local offices
    return []

def get_branch_members():
    members = []
    
    branch_members = frappe.get_all(
        "Federation Structure",
        filters={
            "structure_type": "أعضاء الفروع",
            "is_active": 1
        },
        fields=["member"]
    )
    
    for branch_member in branch_members:
        member_doc = frappe.get_doc("Member", branch_member.member)
        members.append({
            "member_name": member_doc.name1,
            "profession": member_doc.profession,
            "institution": member_doc.institution
        })
        
    return members
