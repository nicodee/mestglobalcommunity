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
						// '<figcaption><img src="',item.data_fav_src,'" class="fav-image" data-user_id="',item.id,'"data-fav-status="',item.data_fav_status,'" data-favorite-type="',item.profile,'">',
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

function handleFullProfileResponse(data){
	var object = $.parseJSON(data);	
	user = object.user;
	// object.rated = false;

	$("#myModalLabel").html(user.user_profile);
	$("#mentor-profile-name").html(user.first_name+ ' '+user.last_name);
	$("#profile-brief-location span").html("<strong>Location:</strong> "+user.location);
	$("#profile-head #profile-brief-img #modal-pic").attr("src",object.user.picture);
	$("#modal-fav-image").attr("src", object.user.data_fav_src);
	$("#modal-pic").attr("data-user-id", object.user.user_id);
	$("#modal-pic").attr("data-fav-status", object.user.data_fav_status);
	$("#modal-pic").attr("data-favorite-type", object.user.user_profile);
	$("#rateit5").rateit("value",user.rating.value);
	$("#compose-message").attr("name", 'receiver_id');
	$("#compose-message").attr("value", object.user.user_id);
	$("#compose-message").attr("href", "/messages/compose/"+object.user.user_id);
	$("#profile-brief-schedule span").html("<strong>Time zone:</strong> "+object.program[0].time_zone);
	fetchComments(object);
	fetchSummary(object);
	fetchPosition(object); 
	fetchExpertise(object);
	fetchIndustries(object);
	// fetchSchedule(object);
	fetchEducation(object);
	fetchProgram(object);
	fetchSkills(object);
	fetchTopics(object);
	fetchSectors(object);
	fetchCommentBox(object);
	
	//event listener when an item is rated
	$(".rateit").click(
		function(e){ 
			if (rated == false){
				var rating = $("#rateit-range-2").attr("aria-valuenow");
				rated = true;
				rate(rating,rated);
			}
		}
	);
	
	//event listener for submitting new comments
	$("#comment-submit-button").click(
		function(){
			console.log(new_comment);
			if (new_comment == 0){
				new_comment = new_comment + 1;
				// var action     = "new";
				// var type       = "user";
				// var content    = $("#comment-textarea").val();
				// var entity_id  = $("#modal-pic").attr("data-user-id");
				// comment(action, type, content , entity_id, "");		
					submitComment($(this));
				}
		}
	);	
	//call to event listener for deleting and editing a comment item
	bindObjects();
	// $(".send-message").bind("click", function(){sendMessage(user.user_id)});
}

function sendMessage(user_id){
	// var action      = "send-message";
	// var receiver_id = user_id;
	// $.ajax('/messages', {
	// 	type: "POST",
	// 	data: {action: action, receiver_id: receiver_id}
	// 	success: handleSendMessageResponse
	// });
	console.log(user_id);
}

function handleSendMessageResponse(data){
	console.log(data);
}

//called when a comment is being submitted
function submitComment(comment_item){
	var action     = "new";
	var type       = "user";
	var content    = $("#comment-textarea").val();
	var entity_id  = $("#modal-pic").attr("data-user-id");
	comment(action, type, content , entity_id, "");	
	comment_item.off("click");
}

//event listener for editing and deleting comment items
function bindObjects(){
	$('.edit').bind("click", function(){ editComment( $(this) )} );
	$('.delete').bind("click", function(){ confirmDelete( $(this) )} );	
}

//dialogue box that pops up to confirm deletion of a comment
function confirmDelete(comment_object){
	if( confirm("This comment will be permanently deleted. Do you want to proceed?") ){
		deleteComment(comment_object);
		$("#new-comment-container").show();
	}	
	else{
		alert("Go back.");
	}	
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
	// alert(comment_id);
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

function fetchCommentBox(object){
	if (object.logged_user_comment == 0){
		$("#new-comment-container").show();
		new_comment = 0;
	}
	else{
		$("#new-comment-container").hide();
		new_comment = 1;
	}
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

//handling server response for new comment
function handleCommentResponse(data){
	var comment = $.parseJSON(data);
	if ( (comment.status == true) &&(comment.comment_action == "new") &&(new_comment == 1)){
		var html = ['<div class="row-fluid ',comment.commentor_id,
					'" id="comment-item" data-comment-id="',comment.comment_id,
					'" data-commentor-id="',comment.commentor_id,
					'">','<div class="row-fluid">',
					'<div class="span9 pull-left" id="commentor-name"><p>',
					comment.commentor,'</p></div>',
					'<div class="span3 pull-right"><img src="scripts/img/delete_comment.png" class="delete" data-commentor-id="',
					comment.commentor_id,'"><img src="scripts/img/edit.png" class="edit" data-commentor-id="',
					comment.commentor_id,'"></div>','</div>','<input type="hidden" id="',
					comment.comment_id,'">',
					// comment.comment_id,'"><div class="',comment.comment_id,
					// '" id="received_rating" data-rateit-min="0" data-rateit-ispreset="true" data-rateit-readonly="true"></div>',
					'<div class="row-fluid" id="comment-rating"></div><div class="comment-content"><span>',
					comment.content,'</span></div></div>'].join("");

		$("#comments-container").append(html);	
		var backing ="#"+comment.comment_id;
		console.log(comment.comment_id);
		// var rating    = "."+comment.comment_id;
		// $(rating).rateit({ max: 5, step: 0.5, backingfld: backing });
		// var value = $("#rateit-range-2").attr("aria-valuenow");
		// $(rating).rateit("value", value);
		$("#comment-textarea").val("");
		$("#new-comment-container").hide();
		new_comment = new_comment - 1;
	}

	else if( (comment.status == true) &&(comment.comment_action == "edit") ){
		var commentor_id = comment.commentor_id;
		var comment_item = $("."+commentor_id);
		var content      = comment.content;
		comment_item.find(".comment-content").text(content);
		$("#comment-textarea").val("");
	}

	console.log(new_comment);	
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
	// console.log(data);
	rated = false;
	// console.log(rated);
}

// fetching comments made on a particular item
function fetchComments(object){
	var comments = object.comments_received;
	comments.sort(sort_by('created', true, parseInt));
	$("#comments-container").html('');
	comments.forEach(function(comment){
		var html = ['<div class="row-fluid ',comment.commentor_id,
					'" id="comment-item" data-comment-id="',comment.comment_id,
					'" data-commentor-id="',comment.commentor_id,'">',
					'<div class="row-fluid">',
					'<div class="span9 pull-left" id="commentor-name"><p>',
					comment.commentor,'</p></div>',
					'<div class="span3 pull-right"><img src="scripts/img/delete_comment.png" class="delete" data-commentor-id="',
					comment.commentor_id,'"><img src="scripts/img/edit.png" class="edit" data-commentor-id="',
					comment.commentor_id,'"></div>','</div>',
					'<input type="hidden" id="',comment.comment_id,
					'">',
					// '"><div class="',comment.comment_id,
					// '" id="received_rating" data-rateit-min="0" data-rateit-ispreset="true" data-rateit-readonly="true"></div>',
					'<div class="row-fluid" id="comment-rating"></div><div class="comment-content"><span>',
					comment.content,'</span></div></div>'].join("");

		$("#comments-container").append(html);	
		// var backing ="#"+comment.comment_id;
		// var rating  = "."+comment.comment_id;
		// $(rating).rateit({ max: 5, step: 0.5, backingfld: backing });
		// $(rating).rateit("value", comment.rating.value);
	});
}


function fetchSummary(object){
	if(object.user.summary != null){
		$("#profile-summary-content p").html(object.user.summary);
	}
	else{
		$("#profile-summary-content p").html(object.program[0].mini_bio);
	}
}


function fetchPosition(object){
	var positions = object.positions; 
	console.log(object);
	if (object.positions.length == 0){
		var educations = object.educations;
		educations.sort(sort_by('end_date', false, parseInt));
		var school = "<strong>Education:</strong> " +educations[0].school_name;
		$("#profile-company-position p").html(school);
		$("#profile-resume-list").html('');
		$("#profile-resume").hide();
		console.log("error");
	}
	else{		
		positions.forEach(
			function(item){
				if (item.is_current == "True"){			
					var positionHtml = item.title + " at "+item.company;
					$("#profile-company-position p").html(positionHtml);
				}
			});

		positions.sort(sort_by('start_date', false, parseInt));
		var positionsContainer = [];
		positions.forEach(function(item){
			positionsContainer.push(positionItem(item));
		});
		var positionHtml = positionsContainer.join("");
		if (positionsContainer.length != 0){
			$("#profile-resume-list").html(positionHtml);
		}	
		$("#profile-resume").show();
	}
}


function positionItem(position){
	var positionContainer = [];
	var resumeStart       = '<div class="row-fluid" id="profile-resume-item"><div class="row-fluid" id="resume-position-details">';
	positionContainer.push(resumeStart);

	var role              = '<p id="position-title">' + position.title + '</p>';
	positionContainer.push(role);

	var company           = '<p id="position-company">' + position.company + '</p>';
	positionContainer.push(company);

	var end_date ;
	if (position.is_current == "True"){
		end_date = "Present";
	}
	else{
		end_date = position.end_date;
	}
	var duration          = '<p id="position-duration-description"><span id="position-duration">'+ position.start_date +" - "+ end_date+'</span></p>';
	positionContainer.push(duration);

	if (position.summary != "None"){
		var description	      = '<p id="position-description">'+position.summary+'</p></div></div></div>';
		positionContainer.push(description);
	}
	return positionContainer.join("");
}


function fetchExpertise(object){
	var expertise = object.topics;
}


function fetchIndustries(object){
	var industries = object.sectors;
}


function fetchProgram(object){
	var program = object.program;
}


// function fetchSchedule(object){
// 	var schedules = object.schedules;
// 	var schedulesContainer = [];
// 	schedules.forEach(function(item){
// 		schedulesContainer.push(scheduleItem(item));
// 	});
// 	console.log(schedules);
// }


function fetchEducation(object){
	var educations = object.educations;
	educations.sort(sort_by('end_date', false, parseInt));
	var educationsContainer = [];
	educations.forEach(function(item){
		educationsContainer.push(eduItem(item));
	});
	var schoolHtml = educationsContainer.join("");
	if (educationsContainer.length != 0){
		$("#profile-education-list").html(schoolHtml);
		$("#profile-education").show()
	}	
	else{
		$("#profile-education-list").html("");
		$("#profile-education").hide();
	}
}


// function scheduleItem(schedule){
// 	var scheduleItem = [];
// 	var container    = '<ul class="schedule-item">';
// 	scheduleItem.push(container);

// 	// var time_zone    = '<li class="time-zone">' + schedule.time_zone + '</li>';
// 	var time_zone    = '<li class="time">' + schedule.time_zone;
// 	scheduleItem.push(time_zone);

// 	// var start_time   = '<li class="start-time">' + schedule.start_time + '</li>';
// 	var start_time   = ' ' + schedule.start_time;
// 	scheduleItem.push(start_time);

// 	var to           = ' - ';
// 	scheduleItem.push(to);

// 	var end_time     = schedule.end_time + '</li>';
// 	scheduleItem.push(end_time);

// 	// var when         = '<li>&nbsp;on&nbsp;</li>';
// 	// scheduleItem.push(when);

// 	var days         = tagDays(schedule.days);
// 	scheduleItem.push(days);

// 	scheduleItem.push("</ul>");

// 	$("#profile-brief-schedule span").html(scheduleItem.join(""));
// }

// function tagDays(daysString){
// 	var day_container = [];
// 	var days_list     = daysString.split(", ");

// 	days_list.forEach(
// 		function(item){
// 			var day = '<li class="day">'+item+'</li>';
// 			day_container.push(day);
// 		}
// 	);

// 	return day_container.join("");
// }


function eduItem(school){
	var schoolItem = [];
	var container  = '<div class="row-fluid" id="profile-education-item"><div class="row-fluid" id="education-school-details">';
	schoolItem.push(container);

	var schoolName = '<p id="education-school"> '+school.school_name+' <p>';
	schoolItem.push(schoolName);

	if (school.field_of_study != "None"){
		var fieldOfStudy = '<p id="education-school-degree">'+school.field_of_study+'<p>';
		schoolItem.push(fieldOfStudy);
	}	

	var duration = '<p id="education-school-duration-description"><span id="education-school-duration">' + school.start_date + ' - ' + school.end_date + '</span></p></div></div>';
	schoolItem.push(duration);
	return schoolItem.join("");
}


function fetchSkills(object){
	var skillsContainer = [];
	var skills = object.skills;
	skills.forEach(function(item){
		skillsContainer.push('<li>'+item.name+'</li>');
	});
	var skillsDisplay = skillsContainer.join("");
	if(skillsContainer.length>0){
		$("#profile-brief-skills-tags span").html("<ul>"+skillsDisplay+"</ul>");
	}
}


// function mycomparator(a,b) {
//   return parseInt(a.end_date) - parseInt(b.end_date);
// }

var sort_by = function(field, reverse, primer){
   var key = function (x) {return primer ? primer(x[field]) : x[field]};

   return function (a,b) {
	  var A = key(a), B = key(b);
	  return ( (A < B) ? -1 : ((A > B) ? 1 : 0) ) * [-1,1][+!!reverse];                  
   }
}

function fetchTopics(object){
	var topicsContainer = [];
	var topics= object.topics;
	topics.forEach(function(item){
		topicsContainer.push('<li>'+item.value+'</li>');
	});
	var topicsDisplay = topicsContainer.join("");
	if(topicsContainer.length>0){
		$("#expertise span").html('<ul>'+topicsDisplay+'</ul>');
	}
}


function fetchSectors(object){
	var sectorsContainer = [];
	var sectors = object.sectors;
	sectors.forEach(function(item){
		sectorsContainer.push('<li>'+item.value+'</li>');
	});
	var sectorsDisplay = sectorsContainer.join("");
	if(sectorsContainer.length>0){
		$("#industries span").html('<ul>'+sectorsDisplay+'</ul>');
	}
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

