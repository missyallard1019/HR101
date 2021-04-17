document.addEventListener('DOMContentLoaded', function() {
	
	let topics = document.querySelectorAll('.show_topic_posts');
	topics.forEach((btn) => {
		btn.addEventListener("click", (event) => {
			togglePosts(btn.id);
		});
	});
	
	$('#edit_post').click(function() {
		toggleEditPost();
	});

});

function togglePosts(topic_id) {
	var topic = document.getElementById(topic_id);
	var topicposts = document.getElementById(topic.id + "posts");
	var replyblock = document.getElementById(topic.id + "reply");
	var reply = document.getElementById("reply_field");
	
	if (topicposts.style.display === "none") {
		topicposts.style.display = "block";
		replyblock.style.display = "block";
		$(".placeholder_field").attr('placeholder', "Type your reply");
	} else {
		topicposts.style.display = "none";
		replyblock.style.display = "none";
	}
}

function toggleEditPost() {
	var post = document.getElementById("current_post");
	var form = document.getElementById("edit_post_form");
	var reply = document.getElementById("reply_field");
	var old_comment = $("#post_message").val();

	post.style.display = "none";
	form.style.display = "block";
	reply.style.display = "none";
	$(".placeholder_field").val(old_comment);
}