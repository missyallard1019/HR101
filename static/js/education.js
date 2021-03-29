document.addEventListener('DOMContentLoaded', function() {
	var x = document.getElementById("next_button").disabled;
	console.log(x);
	
	$('#video_frame').click(function() {
		document.getElementById("next_button").disabled = false;
	});

});


function advanceProgress(video) {
	var chapterid = 
	
}