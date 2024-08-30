/*
  Turno/Turma: 3º ANO - Informática - Matutino
  Grupo: PineApple
  Discentes:

    -- Eduarda Negreiros Silva;
    -- Filipe Silva Rodrigues de Almeida;
    -- Karla Sophia Polgar Rocha;
    -- Théo Tavernard da Rocha Machado;
    -- Victor Lopes Rios.

*/



$(document).ready(function (){
    const hamburguer = document.querySelector(".hamburguer");
    const nav = document.querySelector(".nav");
    
    hamburguer.addEventListener("click", () => nav.classList.toggle("actived"));
    
    $(window).on('scroll', function () {
        const header = $('header');
        const scrollPosition = $(window).scrollTop() - header.outerHeight();

        let activeSectionIndex = 0;

        if (scrollPosition <= 0) {
            header.css('box-shadow', 'none');

        } else {
            header.css('box-shadow', '5px 1px 5px rgba(0, 0, 0, 0.5)');

        }

        sections.each(function(i) {
            const section = $(this);
            // const sectionTop = section.offset().top - 96 500;
            const sectionTop = section.offset().top - 400;
            const sectionBottom = sectionTop + section.outerHeight();

            if (scrollPosition >= sectionTop && scrollPosition < sectionBottom) {
                activeSectionIndex = i;
                return false;
            }

        });

        navItems.removeClass('active');
        $(navItems[activeSectionIndex]).addClass('active');


    });


});