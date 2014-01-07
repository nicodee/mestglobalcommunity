$(document).ready(function () {
	$(".unsubscribe").bind("click", function (){ unsubscribe($(this))});
	$(".delete").bind("click", function(){ deleteSubscriber($(this))});
});

function unsubscribe (subscriber) {
	var subscriber_id = subscriber.attr("data-subscriber-id");
	var answer   = confirm("Do you want to remove this member from the mailing list?");
	if (answer){
		var action = "unsubscribe";
		$.ajax("/admin/mailinglist",{
			type: "POST",
			data: {action:action, subscriber_id:subscriber_id},
			success: handleResponse
		})
	}	
}

function deleteSubscriber (subscriber) {
	var subscriber_id = subscriber.attr("data-subscriber-id");
	var answer   = confirm("Do you want to delete this account?");
	if (answer){
		var action = "delete";
		$.ajax("/admin/mailinglist",{
			type: "POST",
			data: {action:action, subscriber_id:subscriber_id},
			success: handleResponse
		})
	}	
}

function handleResponse  (data) {
	timedRefresh(500);
}

function timedRefresh(timeoutPeriod) {
	setTimeout("location.reload(true);",timeoutPeriod);
}