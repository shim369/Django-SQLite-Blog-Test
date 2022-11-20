$(function(){
  let nav = $('.globalNav');
  nav.clone().appendTo('#js_nav');
  
   $('#header_nav li').hover(function () {
    $("ul:not(:animated)", this).slideDown();
   }, function () {
    $("ul.dropdown", this).slideUp();
   });
});

$(function () {
   let $body = $('body');
   $('#js_btn').on('click', function () {
   $body.toggleClass('side-open');
   });
   $('#js_nav').on('click', function () {
   $body.removeClass('side-open');
   });
});

$(function () {
   $('#page-top').on('click', ()=>{
      $('body,html').animate({ scrollTop: 0 }, 1000);
      return false;   
   });
});