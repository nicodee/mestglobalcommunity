$(document).ready(function(){
	// CKEDITOR.instances.message.on('change', function() {console.log(CKEDITOR.instances.message.getData())});
	// CKEDITOR.instances['message'].on('change', function() {alert('test 1 2 3')});
	// CKEDITOR.instances.message.getData()
	CKEDITOR.instances.message.on('change', function() {
		checkMessageType(CKEDITOR.instances.message.getData());
	});
});

function checkMessageType(argument) {
	var checked = $(".hideShow.active input[type=checkbox]:checked");
	var unchecked = $(".hideShow.active input[type=checkbox]");
	var difference = checkDifference(checked.length, unchecked.length);
	// console.log(difference);
	if(difference == false) {
		determineError(checked, unchecked);
	}
}

function checkDifference (checked, unchecked) {
	return (checked > 0 && unchecked > 0 && checked == unchecked);
}

function determineError (checked, unchecked) {
	
}