$(document).ready(function(){
	$('.modal #expertise span ul li').bind('click', function () {
		checkTopic($(this));
	});
	$('.modal #industries span ul li').bind('click', function () {
		checkSector($(this));
	});
	$('#myModal').on('hidden', function () {
	    refreshTopics();
	});
	$('#sectorModal').on('hidden', function () {
	    refreshTopics();
	});
});

function checkTopic(object){
	edit(object,'topic');
}

function checkSector(object){
	edit(object,'sector');
}

function getState (object) {
	state = object.hasClass('selected');
	if (state == true){
		object.removeClass('selected');
		return 'delete';
	}
	else{
		object.addClass('selected');
		return 'add';		
	}
}

function edit(object, arg) {
	criteria = object.attr('data-topic-criteria');
	action_to_perform = getState(object);
	value = object.text().trim();
	action = "edit_profile";

	$.ajax('/mentor', {
		type: "POST",
		data:{criteria: criteria, action: action, value: value, action_to_perform: action_to_perform, type: arg},
		success: handleEditProfileResponse
		}
	);
}
function handleEditProfileResponse (data) {
}

function refreshTopics(){
	$.ajax('/mentor', {
		type: 'POST',
		data: {action: 'topics'},
		success: handleRefreshTopics
	});
}

function handleRefreshTopics(data){
	$('#full-profile-content-right').html(data);
}