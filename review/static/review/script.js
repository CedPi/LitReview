$(document).ready(function () {

    $(".dropdown-trigger").dropdown();

    $(".ticket-row").hover(function () {
        let elt = $(this).find(".ticket-row__actions");
        if (elt.css('visibility') == 'hidden')
            elt.css('visibility', 'visible')
        else if (elt.css('visibility') == 'visible')
            elt.css('visibility', 'hidden');
    });

    $(".review-row").hover(function () {
        let elt = $(this).find(".review-row__actions");
        if (elt.css('visibility') == 'hidden')
            elt.css('visibility', 'visible')
        else if (elt.css('visibility') == 'visible')
            elt.css('visibility', 'hidden');
    });

    $(".modal-trigger").click(function () {
        let title = $(this).attr("data-title");
        let post_type = $(this).attr("data-post-type");
        let modal = $("#modal_delete")
        let p0 = modal.find("p")[0];
        let delete_btn = modal.find(".delete-btn");
        p0.innerHTML = "Vous êtes sur le point de supprimer votre " + post_type + " concernant <b>" + title + "</b>";
        delete_btn.attr("href", $(this).attr('data-delete-url'));
        $("#modal_delete").openModal();
    });

    $(".yellow").click(function () {
        let target_id = $(this).attr("data-href");
        let target = $(target_id);
        $('html, body').animate({
            scrollTop: $(target).offset().top
        }, 400)
    });

    $(".toggle-visible").click(function () {
        let parent = $(this).parent().parent();
        $(".review-row__headline").slideUp();
        $(".review-row__body").slideUp();
        let head = parent.find(".review-row__headline");
        let body = parent.find(".review-row__body");
        $(head).slideToggle();
        $(body).slideToggle();
    });
})