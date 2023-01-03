$(function(){
	let nav = $('.l-header__list');
	nav.clone().appendTo('.l-header__menu');
	let iconNav = $('.l-header__icons');
	iconNav.clone().appendTo('.l-header__menu');
});

$(function(){
   let $body = $('body');
   $('.l-header__menu-btn').on('click', ()=>{
   $body.toggleClass('side-open');
   });
   $('.l-header__menu').on('click', ()=>{
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