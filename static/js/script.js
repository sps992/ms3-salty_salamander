 // jQuery

$(document).ready(function(){
    $('.sidenav').sidenav();

    $('.carousel.carousel-slider').carousel({
    fullWidth: true,
    indicators: true
    });

    $('select').formSelect();

  $("#do-better").click(function() {
    $([document.documentElement, document.body]).animate({
        scrollTop: $("#recipe-container").offset().top
    }, 1000);
});
  
});
