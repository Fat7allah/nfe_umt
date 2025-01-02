frappe.ready(function() {
    // Initialize tooltips
    $('[data-toggle="tooltip"]').tooltip();
    
    // Handle form submissions with AJAX
    $('.nfe-form').on('submit', function(e) {
        e.preventDefault();
        var form = $(this);
        var submitBtn = form.find('button[type="submit"]');
        var originalText = submitBtn.text();
        
        // Disable submit button and show loading state
        submitBtn.prop('disabled', true).text('جاري المعالجة...');
        
        // Get form data
        var formData = {};
        form.serializeArray().forEach(function(item) {
            formData[item.name] = item.value;
        });
        
        // Make API call
        frappe.call({
            method: form.data('method'),
            args: formData,
            callback: function(r) {
                if (!r.exc) {
                    // Show success message
                    frappe.show_alert({
                        message: r.message || 'تمت العملية بنجاح',
                        indicator: 'green'
                    });
                    
                    // Handle redirect if specified
                    if (form.data('redirect')) {
                        setTimeout(function() {
                            window.location.href = form.data('redirect');
                        }, 2000);
                    }
                }
                // Reset button state
                submitBtn.prop('disabled', false).text(originalText);
            },
            error: function(r) {
                // Show error message
                frappe.show_alert({
                    message: 'حدث خطأ أثناء المعالجة',
                    indicator: 'red'
                });
                // Reset button state
                submitBtn.prop('disabled', false).text(originalText);
            }
        });
    });
    
    // Handle dynamic form fields
    $('[data-depends-on]').each(function() {
        var field = $(this);
        var dependsOn = field.data('depends-on');
        var dependentField = $('[name="' + dependsOn + '"]');
        
        function toggleField() {
            var value = dependentField.val();
            var condition = field.data('depends-value');
            
            if (value === condition) {
                field.show();
            } else {
                field.hide();
            }
        }
        
        dependentField.on('change', toggleField);
        toggleField(); // Initial state
    });
    
    // Handle file uploads
    $('.nfe-file-upload').on('change', function() {
        var input = $(this);
        var filename = input.val().split('\\').pop();
        input.next('.custom-file-label').text(filename);
    });
    
    // Handle confirmation dialogs
    $('[data-confirm]').on('click', function(e) {
        e.preventDefault();
        var link = $(this);
        
        frappe.confirm(
            link.data('confirm'),
            function() {
                window.location.href = link.attr('href');
            }
        );
    });
    
    // Handle tabs
    $('.nfe-tabs').on('click', '.nav-link', function(e) {
        e.preventDefault();
        var tab = $(this);
        
        // Update active states
        tab.parent().siblings().find('.nav-link').removeClass('active');
        tab.addClass('active');
        
        // Show corresponding content
        var target = $(tab.data('target'));
        target.siblings('.tab-pane').removeClass('show active');
        target.addClass('show active');
    });
    
    // Handle search functionality
    $('.nfe-search-input').on('keyup', function() {
        var searchTerm = $(this).val().toLowerCase();
        var target = $($(this).data('search-target'));
        
        target.find('tr').each(function() {
            var row = $(this);
            var text = row.text().toLowerCase();
            
            if (text.indexOf(searchTerm) === -1) {
                row.hide();
            } else {
                row.show();
            }
        });
    });
    
    // Handle print functionality
    $('.nfe-print-btn').on('click', function() {
        var printArea = $($(this).data('print-target')).html();
        var originalContents = $('body').html();
        
        $('body').html(printArea);
        window.print();
        $('body').html(originalContents);
    });
});
