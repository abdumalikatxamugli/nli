(function($) {
    $("#id_location_type").change(function (event){
        if(event.target.value==='Map'){
            $('.field-longitude').hide();
            $('.field-latitude').hide();
            $('.field-location').show();
        }else{
            $('.field-longitude').show();
            $('.field-latitude').show();
            $('.field-location').hide();
        }
    });
    $('#id_location_type').val('Map');
    $('.field-longitude').hide();
    $('.field-latitude').hide();
    $('.field-location').show();
})(django.jQuery);