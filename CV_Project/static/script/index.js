$(document).ready(function() {
$(".arrow-down").click(function() {
     $('html, body').animate({
         scrollTop: $(".service-headline").offset().top
     }, 1000);
 });
});

