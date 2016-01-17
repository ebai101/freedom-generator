$(function() {
	$('#generate').click(function() {
		$.getJSON($SCRIPT_ROOT + '/get_text', function(data) {
			$('.text').text(data.text);
		});
	});
});