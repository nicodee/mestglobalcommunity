$(document).ready(function() {
	$(".subscribe").bind("click", function(){ subscribe($(this))});
})

function subscribe(subscriber){
	var name = $(".subscriber-name").val();
	var email = $(".subscriber-email").val();

	action = "subscribe";

    if (validateEmail(email, name) == true){
		$.ajax("/admin/mailinglist", {
			type: "POST",
			data:{action:action, email:email, name:name},
			success: handleSubscribeResponse
		})
    }
    else {
    	alert("Please enter a valid email address.");
    }
}

function handleSubscribeResponse (data) {
	var result = $.parseJSON(data);

	if (result.status == true){
		alert("Thank you for subscribing.");
		$(".subscriber-name").val("");
		$(".subscriber-email").val("");
	}
	else{
		alert("Something went wrong.");
	}
}

function validateEmail(email, name) { 
    var re = /^(([^<>()[\]\\.,;:\s@\"]+(\.[^<>()[\]\\.,;:\s@\"]+)*)|(\".+\"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    if (name != ""){
	    return re.test(email);
    }
    else{
    	alert("Please enter your name.");
    }
} 