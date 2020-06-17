$(document).ready(function() {
    $('.gallery').on('click', function() {
        //alert('teste');
        $('.imagepreview').attr('src', $(this).find('img').attr('src'));
        $('#modelId').modal('show');
    });
    window.onclick = function(event) {
        if (event.target != ".modal") {
            $(".modal").hide();
            $(".modal-backdrop.fade.show").hide();
        }
    }

});