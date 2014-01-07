$(document).scroll(function(){
    var elem = $('.subnav');
    if (!elem.attr('data-top')) {
        if (elem.hasClass('navbar-fixed-top'))
            return;
         var offset = elem.offset()
        elem.attr('data-top', offset.top);
    }
    if (elem.attr('data-top') - elem.outerHeight() <= $(this).scrollTop() - $(elem).outerHeight())
        elem.addClass('navbar-fixed-top');
    else
        elem.removeClass('navbar-fixed-top');
});