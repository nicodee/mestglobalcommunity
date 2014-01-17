$(document).ready(function(){	
	$(".iCheck-helper").click(
		fetchSearchResults
	);	
	$("#mentors").hide();
	$("#job-applicants").hide();
});


function fetchSearchResults(){
	var topics        = $("#search-button-data-topics").val();
	var sectors       = $("#search-button-data-sectors").val();
	var topic_count   = topics.length;
	var sector_count  = sectors.length;
	var action        = "largeSearch"; 
	$.ajax('/search', {
		type: "POST",
		data:{topics: topics, sectors: sectors, action: action},
		success: handleResponse
		});
}


function handleResponse(data){
	var mentorContainer      = [];
	var jobApplicantContainer = [];
	var user = $.parseJSON(data);

    if (user.length == 0){
    	$(".search-result-mentor ul").html("no result to show at the moment");
    	$(".search-result-job-applicant ul").html("no result to show at the moment");
		$("#mentors").hide();
		$("#job-applicants").hide();
		$("#no-of-mentors p").html("Mentors ("+mentorContainer.length+")");
		$("#no-of-applicants p").html("Job applicants ("+jobApplicantContainer.length+")");
    }

    else {
		user.forEach(function(item){
			var foundItem =[
						'<li class="span3 found-result-mentor"><figure><div>',
						'<img src="',item.image, 
						'" alt="img04"></div>',
						'<figcaption>',
						'<div><h3 class="name-mentor">',
						item.name,'</h3><span>',item.summary,
						'</span></div><a href="#myModal" class="user_id" data-user_id="',item.id,'" data-toggle="modal">Take a look</a></figcaption></figure></li>'
					  ].join("\n");
			if (item.profile == "Mentor"){
				mentorContainer.push(foundItem);
				$("#no-of-mentors").html("<a href='#mentors'><p>Mentors ("+mentorContainer.length+")</p></a>");
				$("#mentors").show();
			}

			else if(item.profile == "Job Applicant"){
				jobApplicantContainer.push(foundItem);
				$("#no-of-applicants").html("<a href='#job-applicants'>Job applicants ("+jobApplicantContainer.length+")</a>");
				$("#job-applicants").show();
			}

		});

		$(".search-result-mentor ul").html(mentorContainer.join("\n"));
		$(".search-result-job-applicant ul").html(jobApplicantContainer.join("\n"));
    }

	$(".user_id").click(
		function(){
			var user_id = $(this).attr("data-user_id");
			fetchFullProfile(user_id);
			fetchSearchResults();
		}
	);

	$(".fav-image").click(
		function(){
			var favorite_id     = $(this).attr("data-user_id").trim();
			var favorite_type   = $(this).attr("data-favorite-type").trim(); 
			var favorite_action = getFavoriteAction($(this));
			favorite(favorite_id, favorite_type, favorite_action);
		}
	);
}	

function getValue(favorite){
	favorite.success(
		function (data) {
			  return  data;
		}
	);
}

function fetchFullProfile(user_id){
	var user_id = user_id.trim();
	action      = "getFullProfile";
	$.ajax('/search', {
		type: "POST",
		data:{user_id: user_id, action: action},
		success: handleFullProfileResponse
		}
	);
}
var count = 0;
var new_comment  = 0;
var edit_comment = false 
var rated = false;

function handleFullProfileResponse(data) {
	$("#myModalLabel").html(data);
	$('.des').popover();
	drawChart();
	$('#rateit5').rateit({ max: 5, step: 0.5, backingfld: '#backing6' });
	$("#rateit5").rateit("value", Number($("#modal-pic").attr("rating")));

	$(".rateit").click(
		function(e){ 
			if (rated == false){
				var rating = $("#rateit-range-2").attr("aria-valuenow");
				rated = true;
				rate(rating,rated);
			}
		}
	);

	$("#comment-submit-button").bind('click', function () {
			submitComment($(this));
		}
	);	
	bindObjects();
}


function drawChart() {
  setTimeout(function(){google.load('visualization', '1', {'callback': drawChart, 'packages':['corechart']})}, 2000);
  function drawChart() {
    var data = google.visualization.arrayToDataTable([
      ['Task', 'Hours Contributed'],
		['Completed',     Number($("#piechart").attr("data-committed"))],
		['Hours Left',    Number($("#piechart").attr("data-left"))]
    ]);

    var options = {
      title: 'Hours I Have Contributed'
    };

    var chart = new google.visualization.PieChart(document.getElementById('piechart'));
    chart.draw(data, options);
  }
}	


//called when a comment is being submitted
function submitComment(comment_item){
	var action     = "new";
	var type       = "user";
	var content    = $("#comment-textarea").val();
	var entity_id  = $("#modal-pic").attr("data-user-id");
	comment(action, type, content , entity_id, "");	
	// comment_item.off("click");
}

//event listener for editing and deleting comment items
function bindObjects(){
	$('.edit').bind("click", function(){ editComment( $(this) )} );
	$('.delete').bind("click", function(){ confirmDelete( $(this) )} );	
}

// dialogue box that pops up to confirm deletion of a comment
function confirmDelete(comment_object){
	if( confirm("This comment will be permanently deleted. Do you want to proceed?") ){
		deleteComment(comment_object);
		$("#new-comment-container").show();
	}	
	// else{
	// 	alert("Go back.");
	// }	
}

function deleteComment(comment_object){
	var commentor_id = comment_object.attr("data-commentor-id").trim();	
	var comment_item = $("."+commentor_id);
	var comment_id   = comment_item.attr("data-comment-id");
	comment_item.remove();
	var action    = "delete";
	var type      = "user";
	var entity_id = $("#modal-pic").attr("data-user-id");
	comment(action, type, "", entity_id, comment_id);
};


function editComment(comment_object){
	$("#new-comment-container").show();
	var commentor_id = comment_object.attr("data-commentor-id").trim();
	var comment_item = $("."+commentor_id);
	var comment_id   = comment_item.attr("data-comment-id");
	var content      = comment_item.find(".comment-content").text().trim();
    $("#comment-textarea").val(content);
    $("#comment-submit-button").attr("id", "comment-edit-button");
	$("#comment-edit-button").click(
		function(){
			var action         = "edit";
			var type           = "user";
			var new_content    = $("#comment-textarea").val();
			var entity_id      = $("#modal-pic").attr("data-user-id");
			comment(action, type, new_content , entity_id, comment_id);	
			$("#new-comment-container").hide();
			$("#comment-edit-button").attr("id", "comment-submit-button");
		}
	);	
}


//making ajax call to server for new comment
function comment(comment_action, type, content, entity_id, comment_id){
	var action  = "comment"
	var comment = JSON.stringify({ 
								"content":content,
								"entity_id":entity_id, 
								"type":type, 
								"comment_action":comment_action,
								"comment_id": comment_id
							});
	console.log(new_comment);
	$.ajax("/search",{
		type: "POST",
		data: { action: action, comment: comment},
		success: handleCommentResponse
	});
}


function handleCommentResponse (data) {
	console.log(data);
	fetchFullProfile($("#modal-pic").attr("data-user-id"));
}


//making ajax call to confirm rating 
function rate(rating,rated){
	var rating_id     = $("#modal-pic").attr("data-user-id").trim();
	var rating_type   = $("#modal-pic").attr("data-favorite-type").trim(); 
	var rating_value  = rating; 
	var action = "rate";
	$.ajax("/search",{
		type: "POST",
		data: {action:action, rating_id: rating_id, rating_type: rating_type, rating_value: rating_value},
		success: handleRateResponse
	})
}

//handling rating response from server
function handleRateResponse(data){
	rated = false;
}




























function favorite(favorite_id, favorite_type, favorite_action){
	var action = "favorite";
	$.ajax("/search",{
		type: "POST",
		data: { action: action, 
				favorite_action: favorite_action, 
				favorite_id: favorite_id,
				favorite_type: favorite_type},
		success: handleFavoriteResponse
	});
}


function  handleFavoriteResponse(data){
		var result = $.parseJSON(data);
		if (result.message == true){
			$("#no-of-favorites").html("My Favorites (" +result.value+")");
		}
}


function getFavoriteAction(object){
	var status = object.attr("data-fav-status").trim();
	if (status == "true"){
		object.attr("src", "scripts/img/unlike.png");
		object.attr("data-fav-status", "false");
		return "unlike";
	}
	else if(status == "false"){
		object.attr("src", "scripts/img/like.png");
		object.attr("data-fav-status", "true");
		return "like";
	}
}

