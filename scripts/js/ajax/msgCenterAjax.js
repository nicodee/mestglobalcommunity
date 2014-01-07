$(document).ready(function(){
	initialize();
});

function initialize(){
// check all checkboxes in table
	if($('.checkall').length > 0) {
		$('.checkall').click(function(){
			var parentTable = $(this).parents('table');										   
			var ch = parentTable.find('.checkbox');										 
			if($(this).is(':checked')) {
					//check all rows in table
					ch.each(function(){ 
						$(this).attr('checked',true);
						$(this).parent().addClass('checked');	//used for the custom checkbox style
						$(this).parents('tr').addClass('selected'); // to highlight row as selected
					});
			}
			else {	
					//uncheck all rows in table
					ch.each(function(){ 
						$(this).attr('checked',false); 
						$(this).parent().removeClass('checked');	//used for the custom checkbox style
						$(this).parents('tr').removeClass('selected');
					});					
				}
		});
	}


	if($('.mailinbox').length > 0) {
			// star
			$('.msgstar').click(function(){
				if($(this).hasClass('starred')){
					$(this).removeClass('starred');
					favoriteMessage($(this).hasClass('starred'), $(this).attr('data-message-id'));
				}
				else{	
					$(this).addClass('starred');
					favoriteMessage($(this).hasClass('starred'), $(this).attr('data-message-id'));
				}
			});
			
			//add class selected to table row when checked
			$('.mailinbox tbody input:checkbox').bind("click", function(){
				if($(this).is(':checked'))
					$(this).parents('tr').addClass('selected');
				else
					$(this).parents('tr').removeClass('selected');
			});
			
			// trash
			if($('.delete').length > 0) {
				$('.delete').bind("click", function(){
					var c = false;
					var cn = 0;
					var o = new Array();
					$('.mailinbox input:checkbox').each(function(){
						if($(this).is(':checked')) {
							c = true;
							o[cn] = $(this);
							cn++;
						}
					});

					if(!c) {
		            alert('No selected message');	
			        } 
			        else {
			            var msg = (o.length > 1)? 'messages' : 'message';
			            if(confirm('Delete '+o.error_length+' '+msg+'?')) {
							for(var a=0;a<cn;a++) {
								if ($(o[a]).attr('data-message-id')){
									$(o[a]).parents('tr').remove();	
									var msg_id = $(o[a]).attr('data-message-id');
									console.log(msg_id);
									deleteMessage(msg_id);
								}
							}
						}
					}
				});
			}


			// mark as read
	        $('.mark_read').bind("click", function(){
				var c = false;
				var cn = 0;
				var o = new Array();
				$('.mailinbox input:checkbox').each(function(){
					if($(this).is(':checked')) {
				           c = true;
				           o[cn] = $(this);
				           cn++;
				       }
				});

				if(!c) {
		          alert('No selected message');	
				} 
				else {
					var msg = (o.length > 1)? 'messages' : 'message';
					if(confirm('Mark '+o.length+' '+msg+' to read')) {
						for(var a=0;a<cn;a++) {
							$(o[a]).parents('tr').removeClass('unread');
							if ($(o[a]).attr('data-message-id')){
								var msg_id = $(o[a]).attr('data-message-id');
								changeMessageReadStatus(msg_id, 'read');
							}
								
						}
					}
				}
			});

		   // make messages to unread
			$('.mark_unread').bind("click",function(){
				var c = false;
				var cn = 0;
				var o = new Array();
				$('.mailinbox input:checkbox').each(function(){
					if($(this).is(':checked')) {
						c = true;
						o[cn] = $(this);
						cn++;
					}
				});

				if(!c) {
				    alert('No selected message');	
				} 
				else {
					var msg = (o.length > 1)? 'messages' : 'message';
					if(confirm('Mark '+o.length+' '+msg+' to unread')) {
						for(var a=0;a<cn;a++) {
							$(o[a]).parents('tr').addClass('unread');
							if ($(o[a]).attr('data-message-id')){
								var msg_id = $(o[a]).attr('data-message-id');
								changeMessageReadStatus(msg_id, 'unread');
							}
						}
					}
				}
			});
	}

	$("#compose-msg-send").bind("click" ,function(){createMessage()} );	
	$("#compose-msg-cancel").bind("click" ,function(){backToMsgCenter()} );	
	$(".title").bind("click" ,
		function(){
			displayMessage($(this)) ;
		 }
	);
};

function backToMsgCenter(){
	setTimeout(
		function() {
            window.location='/messages';
        }, 200);
}

function createMessage(){
	var msg_type    = $('#msg-select select').find(":selected").text();
	var msg_subject = $("#msg-subject-input").val();
	var msg_content = $(".nicEdit-main").html();
	checkMessageCredibility(msg_type, msg_subject, msg_content);
}


function checkMessageCredibility(msg_type, msg_subject, msg_content){
	// console.log(msg_content);
	msg = [];
	error = [];
	getMsgType(msg_type);
	getMsgSubject(msg_subject);
	getMsgContent(msg_content);
	// console.log(msg.length);
	// console.log(error.length);
	determineProgress(msg,error);
	// console.log(msg);
}

function getMsgType(msg_type){
	if(msg_type){	
		msg.push({"type":msg_type});	
	}
	else if(!msg_type){
		error.push({"type":"Type of message"});
	}
}

function getMsgSubject(msg_subject){
	if(msg_subject){		
		msg.push({"subject": msg_subject});
	}
	else if(!msg_subject){
		error.push({"subject":"Subject section cannot be blank"});
	}
}

function getMsgContent(msg_content){
	var receiver_id = $("#msg-receiver-input").attr("data-receiver-id").trim();
	var notification_email = $("#msg-sender-notify").val().trim();
	var text = $(".nicEdit-main").text();
	if(text){	
		msg.push({"content": msg_content});
		msg.push({"receiver_id": receiver_id});
		msg.push({"notification_email": notification_email});
	}
	else if(!text){
		error.push({"content": "Content section cannot be blank"});
	}
}

function determineProgress(msg, error){
	msg_length   = msg.length;
	error_length = error.length;
	// console.log(error);
	if(error_length > 0){
		var errorMessage = [];
		error.forEach(
			function(item){
				var key= Object.keys(item);
				errorMessage.push(item[key] + "\n");
			});
		alert(errorMessage);
	}
	else{
		sendMessage(msg);
		// console.log(msg);
	}
}


function sendMessage(msg){
	$(".sending-message").show();
	$(".sending-message").find(".close").hide();
	var action  = "sendMessageAjax";
	var message = JSON.stringify(msg);
	$.ajax("/compose", {
		type: "POST",
		data:{action:action, message: message},
		success: handleResponseMessage
	});
}


function handleResponseMessage(data){
	// var message = $.parseJSON(data);
	// console.log(message);
	console.log(data);
	result  = "True";
	if (result == "True"){
		$(".sending-message").find(".close").show();
		$(".sending-message").hide();
		$(".alert-success").show();
		window.setTimeout(function(){
			$(".alert-success").fadeOut(9000);
		}, 9000);
		$(".nicEdit-main").attr("contenteditable", "false");
		$("#compose-msg-send").attr("disabled", "")
	}
}


function displayMessage(msg_id){
	var message_id  = msg_id.attr("data-message-id");
	var read_status = checkReadStatus(message_id);
	var action      = "displayMessageContent";

	$.ajax('/messages',{
		type: "POST",
		data: {action:action, message_id: message_id, read_status: read_status},
		success: handleResponseDisplayMessage
	});
}


function checkReadStatus(message_id){
	var msg = $("#"+message_id);
	if (msg.hasClass('unread')){
		msg.addClass('read');	
		msg.removeClass('unread');
		return "read";
	}
	else if(msg.hasClass('read')){
		// console.log(false);
	}
}


function handleResponseDisplayMessage(data){
	var message = data;
	$(".hideit").hide();	
	$("#opened-message").html(message).show();
	var content = $("#read-msg-content").attr("data-msg-content");
	$("#read-msg-content").html(content);
	$("#read-msg-content ").css("height", "auto");
	$(".opened-msg-option").tooltip();
	$("#opened-message #go-to-inbox").click(function(){hideOpenedMessage()});
	$("#opened-message #reply-message").click(function(){replyMessage()});
	$("#opened-message #delete-opened-message").click(
		function(){
			var msg_id = $(this).attr('data-id');
			deleteMessage(msg_id);
			$(".message-item#"+msg_id).remove();
			hideOpenedMessage();
		}
	);
	
}


function replyMessage(){
	var replyBox = $("#compose-msg");
	// $("#opened-message").html(replyBox);
	$('#opened-message').hide();
	replyBox.show();
	$("#msg-sender-notify").val($("#mail-tabs").attr("data-user-email"));
	var msg_id = $(".opened-message-title").attr("data-id").trim();
	var to_name = $(".opened-message-sender-name").text();
	var subject = $(".opened-message-subject").text();
	$("#msg-recipient-input").val(to_name);
	$("#msg-recipient-input").attr("data-id", msg_id);
	getMessageSubject(subject);
	nicTextArea();
	$(".send-reply-message").click(function(){sendReplyMessage(msg_id);});
	$(".cancel-reply-message").click(function(){cancelReply()});
	$(".reply-msg-option").tooltip();
}

function getMessageSubject(subject){
	var new_subject = subject.split("Re:");
	if (new_subject.length > 1){
		new_subject = new_subject[1];
		console.log(new_subject);
	}
	else {
		new_subject = new_subject[0];
		console.log(new_subject);
	}
	$("#msg-subject-input").val("Re: "+new_subject);
}

function hideOpenedMessage(){
	$("#opened-message").hide();
	$(".hideit").show();
}


function cancelReply(){
	$(".hideit").show();
	$("#compose-msg").css("display", "none");
	$(".nicEdit-main").html("");
	$("#send-reply-message").removeAttr("disabled");
	area2.removeInstance('new_message');
}


function favoriteMessage(starred, message_id){
	var action = 'star';
	$.ajax('/messages',{
		type: 'POST',
		data: {action:action, status:starred, message_id: message_id},
		success: handleFavoriteMessageResponse
	});
}


function handleFavoriteMessageResponse(data){
	// console.log(data);
}


function changeMessageReadStatus(message_id, status){
	var action = "changeMessageReadStatus";
	$.ajax('/messages', {
		type: "POST",
		data: { action: action, message_id: message_id, status: status},
		success: handleChangeMessageReadStatusResponse
	});
}


function handleChangeMessageReadStatusResponse(data){
	// console.log(data);
}


function deleteMessage(msg_id){
	var action = "delete-message";
	$.ajax('/messages',{
		type: "POST",
		data: {action: action, message_id: msg_id},
		success: handleDeleteMessageResponse
	});
}


function handleDeleteMessageResponse(data){
	console.log(data);
	var msg_count = $(".message-item");
	if (msg_count.length == 0){
		$(".hideit.inbox-header tr").html("<th class='head0 aligncenter' colspan='6' >You have no new messages</th>");
	}
}
		

function nicTextArea() { 
	area2 = new nicEditor({fullPanel : true}).panelInstance('new_message')
}


function sendReplyMessage(msg_id){
	$(".sending-message").show();
	$(".sending-message").find(".close").hide();
	var action         = 'sendReplyMessage';
	var msg_id         = msg_id;
	var subject        = $("#msg-subject-input").val();
	var recipient_name = $("#msg-recipient-input").val();
	var msg            = $('.nicEdit-main').text().trim();
	var msg_raw        = $('.nicEdit-main').html();
	var notify         = $("#msg-sender-notify").val();

	$.ajax('/messages', {
		type: 'POST',
		data: {action: action, msg_id:msg_id, subject:subject, recipient_name: recipient_name, msg: msg, msg_raw: msg_raw, notify: notify},
		success: handleSendReplyMessageResponse
	})
}


function handleSendReplyMessageResponse(data){
	result  = data;
	if (data == "True"){
		$(".sending-message").find(".close").show();
		$(".sending-message").hide();
		$(".alert-success").show();
		window.setTimeout(function(){
		$(".alert-success").fadeOut(9000);
		}, 2200);
		$(".nicEdit-main").attr("contenteditable", "false");
		$("#send-reply-message").attr("disabled", "");
	}
	else if (data == "False"){
		$(".alert-success").show();
		window.setTimeout(function(){
		$(".alert-success").fadeOut(9000);
		}, 2200);
	}
}


$(".display-inbox").click(
	function(){ 
		var inbox_category = $("#mail-select option:selected").attr("data-msg-type");
		var message_type   = $(this).attr("data-msg-type");
		
		showCurrentMsg($(this));
		
		fetchCurrentMsg(inbox_category, message_type);
	}
);

$("#mail-select").change(
	function(){
		var inbox_category = $("#mail-select option:selected").attr("data-msg-type");
		var message_type   = $(".display-inbox.active").attr("data-msg-type");
		
		fetchCurrentMsg(inbox_category, message_type);
	}
);


function showCurrentMsg(current){
	var previousInbox = $("#mail .grouped.hideit li .active");
	previousInbox.removeClass("active");
	current.addClass("active");
}


function fetchCurrentMsg(inbox_category, message_type){
	var action = "messages";
	$.ajax("/messages",{
		type: "POST",
		data: {action:action, inbox_category: inbox_category, message_type: message_type},
		success: handleCurrentResponse
	});
}


function handleCurrentResponse(data){
	$(".mailinbox").html(data);
	$('.checkall').off("click");
	$('.delete').off("click");
	$('.mark_read').off("click");
	$('.mark_unread').off("click");
	initialize();
}