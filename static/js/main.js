$(function(){
  let nav = $('.globalNav');
  nav.clone().appendTo('#js_nav');
  
   $('#header_nav li').hover(function () {
    $("ul:not(:animated)", this).slideDown();
   }, function () {
    $("ul.dropdown", this).slideUp();
   });
});

$(function(){
   let pageTop = $('#page-top');
   pageTop.hide();
   $(window).scroll(function () {
      if ($(this).scrollTop() > 100) {
         pageTop.fadeIn();
      } else {
         pageTop.fadeOut();
      }
   });
   pageTop.click(function () {
      $('body, html').animate({ scrollTop: 0 }, 500);
      return false;
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