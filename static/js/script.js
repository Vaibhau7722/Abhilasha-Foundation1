// Custom JavaScript for Abhilasha Foundation

$(document).ready(function() {
    // Animate cards on scroll
    $(window).scroll(function() {
        $('.card').each(function() {
            var bottom_of_element = $(this).offset().top + $(this).outerHeight();
            var bottom_of_window = $(window).scrollTop() + $(window).height();

            if (bottom_of_window > bottom_of_element) {
                $(this).animate({'opacity':'1','margin-top':'0px'}, 1000);
            }
        });
    });

    // Form validation
    $('form').submit(function(e) {
        var isValid = true;
        $(this).find('input[required], textarea[required]').each(function() {
            if ($(this).val() === '') {
                isValid = false;
                $(this).addClass('is-invalid');
            } else {
                $(this).removeClass('is-invalid');
            }
        });
        if (!isValid) {
            e.preventDefault();
            alert('Please fill in all required fields.');
        }
    });
});