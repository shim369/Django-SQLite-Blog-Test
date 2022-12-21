$(function(){
	let nav = $('.globalNav');
	nav.clone().appendTo('#js_nav');
	let iconNav = $('.iconNav');
	iconNav.clone().appendTo('#js_nav');
});

$(function(){
   let $body = $('body');
   $('#js_btn').on('click', ()=>{
   $body.toggleClass('side-open');
   });
   $('#js_nav').on('click', ()=>{
   $body.removeClass('side-open');
   });
});

function PageTopAnime() {
    var scroll = $(window).scrollTop();
    if (scroll >= 200){
      $('#page-top').removeClass('right-move');
      $('#page-top').addClass('left-move');
    }else{
      if(
        $('#page-top').hasClass('left-move')){
        $('#page-top').removeClass('left-move');
        $('#page-top').addClass('right-move');
      }
    }
}

$(window).scroll(()=>{
  PageTopAnime();
});

$('#page-top').click(()=>{
    $('body,html').animate({
        scrollTop: 0
    }, 500);
    return false;
});