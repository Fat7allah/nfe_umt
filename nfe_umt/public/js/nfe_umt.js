frappe.provide('nfe_umt');

// Custom Scripts for Member DocType
frappe.ui.form.on('Member', {
    refresh: function(frm) {
        // Add custom buttons
        if(frm.doc.docstatus === 1) {
            frm.add_custom_button(__('إنشاء بطاقة إنخراط'), function() {
                frappe.new_doc('Membership Card', {
                    member: frm.doc.name
                });
            });
        }
        
        // Add dynamic help
        frm.set_intro(__('أدخل معلومات العضو الأساسية هنا.'));
    },
    
    validate: function(frm) {
        // Custom validations
        if(frm.doc.email && !validate_email(frm.doc.email)) {
            frappe.throw(__('البريد الإلكتروني غير صالح'));
        }
    }
});

// Custom Scripts for Membership Card DocType
frappe.ui.form.on('Membership Card', {
    refresh: function(frm) {
        // Add custom buttons for payment
        if(frm.doc.docstatus === 1 && frm.doc.status === 'غير المؤداة') {
            frm.add_custom_button(__('تسجيل الدفع'), function() {
                create_payment_entry(frm);
            });
        }
    }
});

// Helper function to create payment entry
function create_payment_entry(frm) {
    frappe.new_doc('Financial Transaction', {
        transaction_type: 'مدخول',
        reference_type: 'Membership Card',
        reference_name: frm.doc.name,
        name1: frm.doc.member_name,
        amount: 100 // Default amount, can be configured
    });
}

// Custom Scripts for Financial Transaction DocType
frappe.ui.form.on('Financial Transaction', {
    refresh: function(frm) {
        // Add print button
        if(frm.doc.docstatus === 1) {
            frm.add_custom_button(__('طباعة إيصال'), function() {
                frappe.show_alert({
                    message: __('جاري طباعة الإيصال...'),
                    indicator: 'green'
                });
            });
        }
    },
    
    validate: function(frm) {
        // Validate amount
        if(frm.doc.amount <= 0) {
            frappe.throw(__('المبلغ يجب أن يكون أكبر من صفر'));
        }
    }
});

// Utility Functions
nfe_umt.utils = {
    format_currency: function(value) {
        return frappe.format(value, {fieldtype: 'Currency'});
    },
    
    format_date: function(date) {
        return frappe.datetime.str_to_user(date);
    },
    
    show_success: function(message) {
        frappe.show_alert({
            message: __(message),
            indicator: 'green'
        });
    },
    
    show_error: function(message) {
        frappe.show_alert({
            message: __(message),
            indicator: 'red'
        });
    }
};
