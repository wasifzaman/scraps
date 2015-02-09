$(document).ready(function() {
	$('.cycle').hide();

	$('.thumb').click(function() {
		if ($('.zoomed').is(':visible')) {
			$('.zoomed').hide();
			$('.zoomed_img').remove();
		}
		
		$('.zoomed').show();
		$('.zoomed').append('<img class="zoomed_img" src="' + $(this).attr('src') + '"/>');
		$('.zoomed').click(function() {
			$('.zoomed_img').remove();
			$(this).hide();
		});
	});

	$('.cycle_nav').click(function() {
		$('.snow').hide();
		$('.cycle').show();
	});

	$('.snow_nav').click(function() {
		$('.cycle').hide();
		$('.snow').show();
	});
});