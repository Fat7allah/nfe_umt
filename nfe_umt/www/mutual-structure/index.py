import frappe
from frappe import _

def get_context(context):
    context.no_cache = 1
    
    if frappe.session.user == 'Guest':
        frappe.local.flags.redirect_location = '/login'
        raise frappe.Redirect
        
    context.executive_office = get_executive_office()
    context.administrative_council = get_administrative_council()
    context.monitoring_committee = get_monitoring_committee()
    
def get_executive_office():
    executive_office = {
        "president": None,
        "secretary": None,
        "members": []
    }
    
    members = frappe.get_all(
        "Mutual Structure",
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
            "position": member.position,
            "profession": member_doc.profession,
            "institution": member_doc.institution
        }
        
        if member.position == "الرئيس":
            executive_office["president"] = member_info
        elif member.position == "الكاتب العام":
            executive_office["secretary"] = member_info
        else:
            executive_office["members"].append(member_info)
            
    return executive_office

def get_administrative_council():
    members = []
    
    council_members = frappe.get_all(
        "Mutual Structure",
        filters={
            "structure_type": "المجلس الإداري",
            "is_active": 1
        },
        fields=["member"]
    )
    
    for council_member in council_members:
        member_doc = frappe.get_doc("Member", council_member.member)
        members.append({
            "member_name": member_doc.name1,
            "profession": member_doc.profession,
            "institution": member_doc.institution
        })
        
    return members

def get_monitoring_committee():
    members = []
    
    committee_members = frappe.get_all(
        "Mutual Structure",
        filters={
            "structure_type": "لجنة المراقبة",
            "is_active": 1
        },
        fields=["member"]
    )
    
    for committee_member in committee_members:
        member_doc = frappe.get_doc("Member", committee_member.member)
        members.append({
            "member_name": member_doc.name1,
            "profession": member_doc.profession,
            "institution": member_doc.institution
        })
        
    return members
