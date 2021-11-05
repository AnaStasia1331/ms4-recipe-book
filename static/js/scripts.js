/*!
* Start Bootstrap - Agency v7.0.5 (https://startbootstrap.com/theme/agency)
* Copyright 2013-2021 Start Bootstrap
* Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-agency/blob/master/LICENSE)
*/

window.addEventListener('DOMContentLoaded', event => {

    // Navbar shrink function
    var navbarShrink = function () {
        const navbarCollapsible = document.body.querySelector('#mainNav');
        if (!navbarCollapsible) {
            return;
        }
        if (window.scrollY === 0) {
            navbarCollapsible.classList.remove('navbar-shrink');
        } else {
            navbarCollapsible.classList.add('navbar-shrink');
        }

    };

    // Shrink the navbar 
    navbarShrink();

    // Shrink the navbar when page is scrolled
    document.addEventListener('scroll', navbarShrink);

    // Collapse responsive navbar when toggler is visible
    const navbarToggler = document.body.querySelector('.navbar-toggler');
    const responsiveNavItems = [].slice.call(
        document.querySelectorAll('#navbarResponsive .nav-link')
    );
    responsiveNavItems.map(function (responsiveNavItem) {
        responsiveNavItem.addEventListener('click', () => {
            if (window.getComputedStyle(navbarToggler).display !== 'none') {
                navbarToggler.click();
            }
        });
    });

    // Overwrite the default attributes of filestyle() in bootstrap-filestyle plugin 
    $('#id_image').filestyle({
        size : 'lg',
        btnClass: 'btn-warning',
        text: 'Upload'
    });

    // const filterByCourse = function() {
    //     var sel = $('input[type=checkbox]:checked').map(function(_, el) {
    //         return $(el).val();
    //     }).get();
    //     console.log(sel)
    //     console.log(sel.length == 0)
    //     $('.container').find(".card").parent().show();
    //     if (sel.length == 0) {
    //         // $('.container').find(".card").parent().css('display', '');
    //         // $('.container').find(".card").parent().show();
    //     } else {
    //         let filter = "";
    //         for (var i = 0; i < sel.length; i++) {
    //             console.log(sel[i])
    //             filter += `.card:not(:contains('${sel[i]}')), `;
    //             console.log(filter)
    //         }
    //         console.log(filter)
    //         filter = filter.slice(0,-2);
    //         console.log(filter)
    //         $('.container').find(filter).parent().hide();
    //     }
    // }

    // $('#checkbox1').click(filterByCourse)
    // $('#checkbox2').click(filterByCourse)
    // $('#checkbox3').click(filterByCourse)
    // $('#checkbox4').click(filterByCourse)
    // $('#checkbox5').click(filterByCourse)
    // $('#checkbox6').click(filterByCourse)

});
