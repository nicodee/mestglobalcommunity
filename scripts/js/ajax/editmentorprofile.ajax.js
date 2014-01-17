$(document).ready(function(){
	$('.modal #expertise span ul li').bind('click', function () {
		checkTopic($(this));
	});
	$('.modal #industries span ul li').bind('click', function () {
		checkSector($(this));
	});
	$("#submit-contribution").bind('click', function () {
		submitContribution();
	})
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
	$('#skills_container').html(data);
}

function submitContribution () {
	var company = $("#inputCompany").val();
	var description = $("#inputDescription").val();
	var hours = $("#inputHours").val();

	if (company && description && hours){
		var action = "add_contribution";
		var contribution = JSON.stringify({"company":company, "description": description, "hours": hours});
		$.ajax('/mentor', {
			type: "POST",
			data:{action: action, contribution: contribution},
			success: handleContributionResponse
		}
	);

	}		
	else {
		alert("Please enter all the fields before submitting the form.");	
	}		
}

function handleContributionResponse (data) {
	console.log(data);
	$("#contributionModal").html(data);
	$("#contributionModal").addClass("success");
	$("#contributionModal.success").on('hidden', function () {
		timedRefresh(500);
	});
}

function timedRefresh(timeoutPeriod) {
	setTimeout("location.reload(true);",timeoutPeriod);
}