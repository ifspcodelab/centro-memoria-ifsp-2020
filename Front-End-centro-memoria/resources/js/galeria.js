$(document).ready(function(){

	var owl = $('.owl-carousel');
	
	owl.owlCarousel({
					margin: 10,
					nav: true,
					loop: true,
					responsive: {
					  0: {
						items: 1
					  },
					  600: {
						items: 3
					  },
					  1000: {
						items: 5
					  }
					}
				  });
				  
	$(".click").click(function () {
		$(".detalhes").addClass("hide");
		
		codigo = $(this).attr('id');
		
		$("div[id='detalhe-"+codigo+"']").removeClass("hide");
    });
	
});


