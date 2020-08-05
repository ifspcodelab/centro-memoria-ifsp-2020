$(document).ready(function(){


	//quando em tela pequena aparece o botão para o menu
	$(document).on('click', ".bt-itens", function(){
		$("nav .itens").slideToggle();
	});

	//faz a verificação da altura da página pra encolher o menu
	$(document).on('scroll', function() {
		scrollFunction();
	});

});

function scrollFunction() {
	if (document.documentElement.scrollTop > 200) {
		$('header').addClass('menor');
		
	} else {
		$('header').removeClass('menor');
		
	}
}
