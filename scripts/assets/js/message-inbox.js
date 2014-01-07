$(document).ready(
	function(){
		init();
});

function init() {
	/**
		Binds a message in the inbox to the click event.
		This calls the readMessage function which fetches the full message
	**/
	$(".mail-item").bind('click', function(){
		readMessage($(this));
	});

	$(".mass").bind('click', function(){
		checkSelection($(this).attr("data-action"));
	});
}

function readMessage (argument) {
	makeActive(argument);
	var message_id = argument.attr("data-msg-id");
	var action = "display-message";
	$.ajax('/messages/inbox',{
		type: "POST",
		data: {action:action, message_id: message_id},
		success: handleResponseDisplayMessage
	});
}

function makeActive (argument) {
	if (argument.hasClass('active') == false) {
		$('.mail-item.active').removeClass('active');
		argument.addClass('active');
	}
	checkReadState(argument); //checks if message is read or not	
}

function checkReadState (argument) {
	if (argument.hasClass('unread') == true) {
		markRead(argument);
	}
}

function markRead (argument) {
	var message_id = argument.attr('data-msg-id');
	argument.removeClass('unread');
	argument.addClass('read');
	changeMessageReadStatus(message_id, "read");
}

function markUnead (argument) {
	var message_id = argument.attr('data-msg-id');
	argument.removeClass('read');
	argument.addClass('unread');	
	changeMessageReadStatus(message_id, "unread");
}

function deleteMessage(argument) {
	var msg_id = argument.attr('data-msg-id');
	argument.remove();
	var action = "delete-message";
	$.ajax('/messages/inbox',{
		type: "POST",
		data: {action: action, message_id: msg_id},
		success: handleDeleteMessageResponse
	});
}


function checkSelection (argument) {
	var msgs = $(".mail-item input[type=checkbox]:checked");
	if (msgs.length <= 0) {
		alert("No selected message.");
	}
	else if (argument == "delete") {
		confirmLoop(msgs, argument);
	}
	else {
		loop(msgs, argument);
	}
}

function loop(msgs, argument) {
	msgs.each( function() {
		$(this).attr('checked', false);
		var msg_item = $(this).parents().eq(3);

		if (argument == "mark-as-read"){
			markRead(msg_item);
		}

		else if (argument == "mark-as-unread"){
			markUnead(msg_item);
		}

		else if (argument == "delete"){
			deleteMessage(msg_item);
		}
	});
}

function confirmLoop(msgs, argument) {
	var r=confirm("Are you sure you want to delete all selected messages?");
	if (r==true) {
	  	loop(msgs, argument);
	}	
	else {
		uncheckMsgs(msgs);
	}
}

function uncheckMsgs(msgs){
	msgs.each( function() {
		$(this).attr('checked', false);
	});	
}

function deleteSingleMsg (argument) {
	if (confirm("Are you sure you want to delete this message?") == true){
		var msg_id = argument.attr("data-msg-id");
		$(".mail-item").each( function () {
			if ($(this).attr("data-msg-id") == msg_id){
				deleteMessage($(this));
				$(".mail-content-options-holder").remove();
				$(".mail-content").remove();
			}
		});		
	}
}

function changeMessageReadStatus(message_id, status) {
	var action = "change-status";
	$.ajax('/messages/inbox', {
		type: "POST",
		data: { action: action, message_id: message_id, status: status},
		success: handleChangeMessageReadStatusResponse
	});
}

function handleChangeMessageReadStatusResponse(argument) {
	// body...
}

function handleDeleteMessageResponse (argument) {
	timedRefresh(500);
}

function displayMessage(argument) {
	var inbox_type = $(".mail-categories.mail-nav.category").attr("data-category");
	var message_id = argument.attr("data-msg-id");
	var action = "displayMessageContent";
	$.ajax('/messages/inbox',{
		type: "POST",
		data: {action:action, message_id: message_id, category: inbox_type},
		success: handleResponseDisplayMessage
	});
}

function handleResponseDisplayMessage (argument) {
	$(".mail-content-holder").html(argument);
	var msg_content = $(".mail-body").attr("data-msg-content");
	$(".mail-body").html(msg_content);
	$(".mail-body").attr("data-msg-content", "");
	$(".mail-content-options.delete").bind('click', function(){
		deleteSingleMsg($(this));
	});
}

function timedRefresh(timeoutPeriod) {
	setTimeout("location.reload(true);",timeoutPeriod);
}