 // jQuery

$(document).ready(function(){
    $('.sidenav').sidenav();

    $('.carousel.carousel-slider').carousel({
    fullWidth: true,
    indicators: true
    });

    $('select').formSelect();

    $('#recipe_description').val('');
  M.textareaAutoResize($('recipe_description'));
  
});
