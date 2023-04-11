$(document).ready(function() {
    $('input[type="file"]').change(function() {
        if ($(this).val()) {
            $('button[type="submit"]').attr('disabled', false);
        }
        else {
            $('button[type="submit"]').attr('disabled', true);
        }
    });
});
