// $(document).ready(function() {
// $(".arrow-down").click(function() {
//      $('html, body').animate({
//          scrollTop: $(".service-headline").offset().top
//      }, 1000);
//  });
// });

// var subheadline = [
//     'A',' ','C', 'r','e',
//     'a','t','i','v','e',' ', 'p',
//     'r','o','g','r','a','m','m','e','r'
// ]
// var index = 0;
// setInterval(function(){
//         $('#aboutmesubheadline').append(subheadline[index++]);
// }, 100)

var windowSize = $(window).width();

if (windowSize < 500) {
    $('.logo-bar').hide();
}
else{
    $('.logo-bar').show();
}

var bangotra = ['B','a','n','g','o','t','r','a']
var  i=0;
setInterval(function(){
        $('.last-name').append(bangotra[i++]);
}, 150)

var fullstackdeveloper = ['F','u','l','l','-',
                        's','t','a','c','k',
                        'D','e','v','e','l','o','p','e','r']
// var  i=0;
// setInterval(function(){
//     $('.last-name').append(bangotra[i++]);
// }, 200)
