window.addEventListener('load', function () {
    $(".dt").click(function () {
        $(".dd").slideToggle();
    });
    $(window).scroll(function () {
        console.log($(document).scrollTop());
        toggleTool();

        function toggleTool() {
            if ($(document).scrollTop() >= 600) {
                $(".ding").fadeIn();
                var dong = 865.9722595214844 + ($(document).scrollTop() - 600);
                // console.log(dong);
                $(".xcar").css("top", dong);
            } else {
                $(".ding").fadeOut();
            }
        }
        if ($(document).scrollTop() >= 681 && $(document).scrollTop() <= 1001) {

            $(".mok1").parent().css("background", "pink");
            $(".mok1").parent().siblings().css("background", "");

        } else if ($(document).scrollTop() >= 1002 && $(document).scrollTop() <= 1401) {
            $(".mok2").parent().css("background", "pink");
            $(".mok2").parent().siblings().css("background", "");
        } else if ($(document).scrollTop() >= 1402) {
            $(".mok3").parent().css("background", "pink");
            $(".mok3").parent().siblings().css("background", "");
        }
    });
    $(".xs").click(function () {
        $("body, html").stop().animate({
            scrollTop: 0
        });
        $("body, html").scrollTop(0);
    });
    $(".mok1").click(function () {
        $("body, html").stop().animate({
            scrollTop: 681
        });
    });
    $(".mok2").click(function () {
        $("body, html").stop().animate({
            scrollTop: 1083
        });
    });
    $(".mok3").click(function () {
        $("body, html").stop().animate({
            scrollTop: 1481
        });
    });
});