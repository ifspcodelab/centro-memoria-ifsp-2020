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

function searchFunc() {
    var input, filter, ul, li, a, i;
    input = document.getElementById('myInput');
    filter = input.value.toUpperCase();
    ul = document.getElementById('ulId');
    li = ul.getElementsByTagName('li');

    for (i = 0; i < li.length; i++) {
        a = li[i].getElementsByTagName('a')[0];
        if (a.innerHTML.toUpperCase().indexOf(filter) > -1) {
            li[i].style.display = "";
        } else {
            li[i].style.display = 'none';
        }
    }
}