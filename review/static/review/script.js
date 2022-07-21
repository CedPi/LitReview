$(document).ready(function () {

    let h = $(".custom-card__controls").css('height');
    // $(".custom-card__controls").offsetTop = 36;
    // alert(h);

    $(".dropdown-trigger").dropdown();

    $(".custom-card").hover(function () {
        let elt = $(this).find(".custom-card__controls");
        if (elt.css('visibility') == 'hidden')
            elt.css('visibility', 'visible')
        else if (elt.css('visibility') == 'visible')
            elt.css('visibility', 'hidden');
        // elt.toggle();
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
})