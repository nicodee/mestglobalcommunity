$(document).ready(function () {	
	$(".delete-job").bind("click", function () {removeJob($(this))});
	$(".job-item").bind("click", function () {viewJob($(this).attr("data-job-id"))});
	$(".edit-job").bind("click", function () {editJob($(this))});
})

function timedRefresh(timeoutPeriod) {
	setTimeout("location.reload(true);",timeoutPeriod);
}

function removeJob(job){
	var answer = confirm("Are you sure you want to remove this job posting");
	if(answer){
		var job_id     = job.attr("data-job-id");
		var action     = "remove";
		$.ajax("jobs",{
			type: "POST",
			data:{action: action, job_id: job_id},
			success: handleRemoveJobResponse
		})
	}
}

function handleRemoveJobResponse (data) {
	var result = $.parseJSON(data);
	if (result.status == true){
		timedRefresh(500);
	}	
	else{
		alert("Unable to delete job item");
	}
}

function viewJob (job) {
	var job_id = job;
	var action = "view";
	$.ajax("/jobs", {
		type: "POST",
		data: {action:action, job_id: job_id},
		success: handleViewJobResponse
	})
}

function handleViewJobResponse (data) {
	$("#content").html(data);
	$(".delete-job").bind("click", function () {removeJob($(this))});
}

function editJob(job){
	var job_id = job.attr("data-job-id");	
	var action = "edit";
	$.ajax("/jobs", {
		type: "POST",
		data: {action:action, job_id: job_id},
		success: handleEditJobResponse
	})
}

function handleEditJobResponse (data) {	
	$("#content").html(data);
	$(".save-edited-job").bind("click", function () {saveEditedJob($(this))});
}

function saveEditedJob (job) {
	var jobObject = JSON.stringify(getEditedJobObject(job));
	var action    = "save-edited-job";
	$.ajax("/jobs", {
		type: "POST",
		data: { action:action, edited_job:jobObject},
		success: handleSavedEditResponse
	})
}

function getEditedJobObject (job) {
	var error_count = 0;
	var jobObject = {};
	jobObject.job_id    = job.attr("data-job-id");
	jobObject.job_title = $(".edit .title").val();
	jobObject.hiring_company = $(".edit .hiring-company").val();
	jobObject.deadline = $(".edit .deadline").val();
	jobObject.description = $(".edit .description").val();
	jobObject.requirements = $(".edit .requirements").val();

	for (var key in jobObject) {
	  if (jobObject.hasOwnProperty(key) && jobObject[key] == "") {
	    error_count++;
	  }
	}

	if(error_count >0){
		alert("All fields are required!");
	}
	else{
		return jobObject;
	}	
}

function handleSavedEditResponse (data) {
	var result = JSON.parse(data);
	if (result.status == true){
		alert("Job posting successfully edited.");
		setTimeout(viewJob(result.job_id),2000);			
	}
	else{
		var answer = confirm("There was an error editing the job posting. Try again later.");
		if(answer){
			timedRefresh(500);				
		}
	}
}

function timedRefresh(timeoutPeriod) {
	setTimeout("location.reload(true);",timeoutPeriod);
}