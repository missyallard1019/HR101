$(document).ready(function() {
	
	var pagename = $('main').attr('id');
	var pagelinkid = '#' + pagename + 'link';
	var mobilelinkid = '#' + pagename + 'link2';
	
	$(pagelinkid).attr('class', 'font-bold text-gray-500 hover:text-gray-900');
	$(mobilelinkid).attr('class', 'font-bold block px-3 py-2 rounded-md text-base font-medium text-gray-700 hover:text-gray-900 hover:bg-gray-50');
	
	$('#open_menu').click(function() {
		toggleMobileMenu();
	});
	
	$('#close_menu').click(function() {
		toggleMobileMenu();
	});
	
	$('#edit_profile_button').click(function() {
		toggleProfileEdit();
	});
		
		

});

function toggleMobileMenu() {
	var menu = document.getElementById("mobile_menu");
	if (menu.style.display === "none") {
		menu.style.display = "block";
	} else {
		menu.style.display = "none";
	}
}

function toggleProfileEdit() {
	var profile = document.getElementById("profile_complete");
	var form = document.getElementById("edit_profile_form");

	profile.style.display = "none";
	form.style.display = "block";
}
