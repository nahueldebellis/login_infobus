
(function ($) {
    "use strict";

    
    /*==================================================================
    [ Validate ]*/
    var input = $('.validate-input .input100');

    $('.validate-form').on('submit',function(){
        var check = true;

        for(var i=0; i<input.length; i++) {
            if(validate(input[i]) == false){
                showValidate(input[i]);
                check=false;
            }
        }

        return check;
    });


    function validate (input) {
        if($(input).val().trim().match(/.*/) == null) {
            return false;
        }
        else {
            if($(input).val().trim() == ''){
                return false;
            }
        }
    }

    
    

})(jQuery);