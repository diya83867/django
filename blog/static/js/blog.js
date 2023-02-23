function googleTranslateElementInit() {
    new google.translate.TranslateElement(
        {
            pageLanguage: "en",
            layout: google.translate.TranslateElement.InlineLayout.SIMPLE,
        },
        "google_translate_element"
    );
}

$("#google_translate_element").bind("DOMNodeInserted", function (event) {
    $(".goog-te-menu-value span:first").html("Translate");
    $(".goog-te-menu-frame.skiptranslate").load(function () {
        setTimeout(function () {
            $(".goog-te-menu-frame.skiptranslate")
            .contents()
            .find(".goog-te-menu2-item-selected .text")
            .html("Translate");
        }, 100);
    });
}
);

$(".hide").click(function () {
    var id = $(this).attr("r_id");
    $(".form-class" + id).toggle();
});

$("#showPass").click(function() {
    if ($(this).is(":checked")) {
        $("#password").attr("type", "text");
    }
    else {
        $("#password").attr("type", "password");
    }
})