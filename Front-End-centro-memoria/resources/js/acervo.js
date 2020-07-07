function contains(text_one, text_two) {
    if (text_one.indexOf(text_two) != -1) {
        return true;
    }
}

$("#myInput").keyup(function() {
    var searchName = $("#myInput").val().toLowerCase();
    $(".title").each(function() {
        if (!contains($(this).text().toLowerCase(), searchName)) {
            $(this).hide();
        } else {
            $(this).show();
        }
    });
});