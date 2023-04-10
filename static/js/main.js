$(document).ready(function() {
    $('input[type="file"]').change(function() {
        if ($(this).val()) {
            $('input[type="submit"]').attr('disabled', false);
        }
        else {
            $('input[type="submit"]').attr('disabled', true);
        }
    });
});
