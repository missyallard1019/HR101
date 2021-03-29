document.addEventListener('DOMContentLoaded', function() {
	
	let topics = document.querySelectorAll('.show_topic_posts');
	topics.forEach((btn) => {
		btn.addEventListener("click", (event) => {
			togglePosts(btn.id);
		});
	});


});

function togglePosts(topic_id) {
	var topic = document.getElementById(topic_id);
	var topicposts = document.getElementById(topic.id + "posts");
	var replyblock = document.getElementById(topic.id + "reply");
	
	console.log(topicposts);
	
	if (topicposts.style.display === "none") {
		topicposts.style.display = "block";
		replyblock.style.display = "block";
	} else {
		topicposts.style.display = "none";
		replyblock.style.display = "none";
	}
}