var getLocation = function(href) {
    var l = document.createElement("a");
    l.href = href;
    return l;
};

// TODO: update this and make it better
$(document).ready(function () {
    var links = $("#navLinks a.nav-link");
    let my_url = getLocation(window.location.href).pathname;
    console.log(my_url);
    for (let link of links) {
        let url_to = $(link).attr("href");
        console.log("href");
        if (my_url === url_to) {
            $(link).addClass("active");
        }
    }
});