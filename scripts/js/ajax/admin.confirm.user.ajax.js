$(document).ready(function(){
	$(".confirm-user-btn").bind("click", function(){confirmationUser($(this))});
	$(".remove-user").bind("click", function(){removeUser($(this))});
	$(".declined .delete-user").bind("click", function(){deleteUser($(this))});
});


function confirmUser(user){
	var data_action = user.attr("data-action");
	var user_id = user.attr("data-id");
	var action = "confirm";
	var state = user.text().toLowerCase();
	$.ajax("/admin", {
		type: "POST",
		data: {action:action, data_action:data_action, user_id:user_id, state:state},
		success: handleConfirmResponse
	});
}


function handleConfirmResponse(data){
	var response = $.parseJSON(data);
    if (response.status == "confirmed"){
    	$(".confirm-user-btn.confirm."+response.user_id).html("Confirmed");    	
    	$(".confirm-user-btn.confirm."+response.user_id).addClass("btn-primary");
    	$(".confirm-user-btn.decline."+response.user_id).removeClass("btn-primary");
    	$(".confirm-user-btn.decline."+response.user_id).html("Decline");  
    }
    else if (response.status == "declined"){
    	$(".confirm-user-btn.decline."+response.user_id).html("Declined");
    	$(".confirm-user-btn.decline."+response.user_id).addClass("btn-primary");
    	$(".confirm-user-btn.confirm."+response.user_id).removeClass("btn-primary");
    	$(".confirm-user-btn.confirm."+response.user_id).html("Confirm");  
    }
    timedRefresh(500);
}


function removeUser(user){	
	var answer = confirm("Are you sure you want to remove this "+ user.attr("data-profile").toLowerCase()+"?");
	if (answer){
		var user_id = user.attr("data-id");
		var action = "remove";
		$.ajax("/admin", {
			type: "POST",
			data: {action:action, user_id:user_id},
			success: handleRemoveResponse
		});
	}
	else{
		// alert("Ok!")
	}
}

function deleteUser(user){	
	var answer = confirm("Are you sure you want to permanently delete this "+ user.attr("data-profile").toLowerCase()+"?");
	if (answer){
		var user_id = user.attr("data-id");
		var action = "delete_user";
		$.ajax("/admin", {
			type: "POST",
			data: {action:action, user_id:user_id},
			success: handleRemoveResponse
		});
	}
	else{
		// alert("Ok!")
	}
}


function handleRemoveResponse(data){
	var response = $.parseJSON(data);
	if (response.value == true){
		timedRefresh(500);		
	}
	else{
		alert("Unable to remove user. Please try again");
	}

}


function timedRefresh(timeoutPeriod) {
	setTimeout("location.reload(true);",timeoutPeriod);
}


function confirmationUser(user) {
	var data_action = user.attr("data-action");
	var answer = confirm("Are you sure you want to "+data_action+" this request?");
	if (answer){
		confirmUser(user);
	}
	else{
		// alert("Ok!")
	}
}