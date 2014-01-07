$(document).ready(function(){

	hideDiv();
	$("#first-mtg").show();
	$("#mail-selected").change(function(){
		hideDiv();
		showDiv(this);
	})
	
});	

function hideDiv(){
	$(".tip-carousel").hide();
}

function showDiv(tipDiv){
	var tipID = $("#" + tipDiv.id + " option:selected").val();
	$("#" + tipID).show();
}