document.addEventListener('DOMContentLoaded', function() {
	
	let topics = document.querySelectorAll('.show_topic_posts');
	
	topics.forEach((btn) => {
		btn.addEventListener("click", (event) => {
			togglePosts(btn.id);
		});
	});
	
	let edits = document.querySelectorAll('.show_edit_form');
	
	edits.forEach((btn) => {
		btn.addEventListener("click", (event) => {
			toggleEditPost(btn.id);
		});
	});

});

function togglePosts(topic_id) {
	var topic = document.getElementById(topic_id);
	var topicposts = document.getElementById(topic.id + "posts");
	var replyblock = document.getElementById(topic.id + "reply");
	
	if (topicposts.style.display === "none") {
		topicposts.style.display = "block";
		replyblock.style.display = "block";
		$(".placeholder_field").attr('placeholder', "Type your reply");
	} else {
		topicposts.style.display = "none";
		replyblock.style.display = "none";
	}
}

function toggleEditPost(post_id) {
	var post = document.getElementById("current_post" + post_id);
	var form = document.getElementById("edit_post_form" + post_id);
	var old_comment = $("#post_message" + post_id).val();

	post.style.display = "none";
	form.style.display = "block";
	$(".reply_form").hide();
	$(".placeholder_field").val(old_comment);
}