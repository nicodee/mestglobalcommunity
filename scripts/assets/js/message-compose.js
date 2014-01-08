$(document).ready(function(){
	CKEDITOR.instances.message.on('change', function() { checkMessageType()});
	$("#submit-message").bind('click', function () {
		validateform();
	});
	$("#email-type").on("change",function(){ checkMessageType()});
});

function checkMessageType() {
	var checked = $(".hideShow.active input[type=checkbox]:checked");
	var unchecked = $(".hideShow.active input[type=checkbox]");
	var msg_type = $("#email-type").val();
	if (msg_type == "default"){
		alert("Please select a type of message.");
		determineErrorClass(false);
		return false;
	}	
	else if (msg_type == "other"){
		determineErrorClass(true);
		return true;
	}
	else {
		determineErrorClass(checked.length == unchecked.length);
		return (checked.length == unchecked.length);
	}
}

function determineErrorClass (argument) {
	if (argument == true) {
		$("#email-type").removeClass("parsley-error-list");
		$(".hideShow.active input:checkbox:not(:checked)").parent().removeClass("parsley-error-list");
		$(".hideShow.active input[type=checkbox]:checked").parent().removeClass("parsley-error-list");
	}
	else {
		$("#email-type").addClass("parsley-error-list");
		$(".hideShow.active input:checkbox:not(:checked)").parent().addClass("parsley-error-list");
		$(".hideShow.active input[type=checkbox]:checked").parent().removeClass("parsley-error-list");
	}
	$(".hideShow.active input:checkbox:not(:checked)").bind("click", function () { 
		$(this).parent().removeClass("parsley-error-list");
		checkMessageType();
	});	
}


function validateform () {
	$('#message-form').parsley('validate');
	var form = $('#message-form').parsley('isValid') && validateMessage(CKEDITOR.instances.message.getData()) && checkMessageType();
	if(form){
		submitform(form);
	};
}

function strip (html) {
   var tmp = document.createElement("DIV");
   tmp.innerHTML = html;
   return tmp.textContent || tmp.innerText || "";
}

function validateMessage (message) {
	length = strip(message).length;
	if (length == 0) {
		alert("Message content can't be blank");
		return false;
	}
	else {
		return true;
	}
}

function submitform (form) {
	if (form == true){
		$("#final-message").val(CKEDITOR.instances.message.getData());
		$("#message-form").submit();
	}
}
		