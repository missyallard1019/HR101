document.addEventListener('DOMContentLoaded', function() {
	
	// 2. This code loads the IFrame Player API code asynchronously.
	var tag = document.createElement('script');

	tag.src = "https://www.youtube.com/iframe_api";
	var firstScriptTag = document.getElementsByTagName('script')[0];
	firstScriptTag.parentNode.insertBefore(tag, firstScriptTag);

	// 3. This function creates an <iframe> (and YouTube player)
	//    after the API code downloads.
	var player;

	function onYouTubeIframeAPIReady() {
		player = new YT.Player('player', {
		  height: '315',
		  width: '560',
		  videoId: '{{ chapter.video_embed }}',
		  playerVars: {
			'autoplay': 0,
			'showinfo': 0,
			'rel': 0
		  },
		  events: {
			'onStateChange': onPlayerStateChange
		  }
		});
	}

	var done = false;
	var button = document.getElementById("submit_next");

	function onPlayerStateChange(event) {
		console.log(event);
		if (event.data == 0) {
			console.log("Video Complete");
			button.setAttribute("class", "w-full flex items-center justify-right px-8 py-3 border border-transparent text-base font-medium rounded-md text-white bg-abiomed-teal hover:bg-blue-royal md:py-4 md:text-lg md:px-10");
			button.disabled = false;
		}
	}

});