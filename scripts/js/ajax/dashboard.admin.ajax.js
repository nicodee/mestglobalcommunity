$(document).ready(
	function () {
		// $("#add-job-btn").bind("click", function () {checkJobDetails();});
		// $(".job-item").bind("click", function () {removeJob($(this))});
		$("#uploadresource").submit(
			function(e) {
				e.preventDefault();
				checkBox(this);
		});
	}
)

// var job_error = [];


// function checkJobDetails(){
// 	var job          = {};
// 	job.title        = getJobTitle();
// 	job.company      = getHiringCompany();
// 	job.description  = getJobDescription();
// 	job.requirements = getJobRequirements();
// 	job.deadline     = getJobDeadline();
// 	job.status       = "Available";
// 	job.url          = getJobUrl();
	
// 	if (job_error.length == 0){
// 		uploadJob(job);
// 		console.log(job_error.length);
// 	}
// 	else{
// 		alert("Error creating job! Some fields were empty.");
// 		// console.log(job_error.length);
// 		job_error = [];
// 	}	
// }


// function getJobTitle () {
// 	var job_title = $("#new-job-title").val();
// 	if (job_title == ""){
// 		job_error.push({title:"Job title"});
// 	}
// 	else{
// 		return job_title;
// 	}
// }


// function getHiringCompany (argument) {
// 	var hiring_company = $("#new-job-company").val();
// 	if (hiring_company == ""){
// 		job_error.company = "Hiring company";
// 	}
// 	else{
// 		return hiring_company;
// 	}
// }


// function getJobDescription (argument) {
// 	var job_description = $("#new-job-description").val();
// 	if (job_description == ""){
// 		job_error.push({description:"Job description"});
// 	}
// 	else{
// 		return job_description;
// 	}
// }


// function getJobRequirements (argument) {
// 	var job_requirements = $("#new-job-requirements").val();
// 	if (job_requirements == ""){
// 		job_error.push({requirements:"Requirements"});
// 	}
// 	else{
// 		return job_requirements;
// 	}
// }


// function getJobDeadline (argument) {
// 	var job_deadline = $("#new-job-deadline").val();
// 	if (job_deadline == ""){
// 		job_error.push({deadline:"Deadline"});
// 	}
// 	else{
// 		return job_deadline;
// 	}
// }

// function getJobUrl (argument) {
// 	var job_url = $("#new-job-url").val();
// 	if (job_url == ""){
// 		job_error.push({url:"Link to job"});
// 	}
// 	else{
// 		return job_url;
// 	}
// }

// function uploadJob(new_job){
// 	var new_job = JSON.stringify(new_job);
// 	var action  = "new_job";
// 	$.ajax("/jobs",{
// 		type: "POST",
// 		data:{action: action, job: new_job},
// 		success: handleNewJobResponse
// 	}) 
// }


// function handleNewJobResponse (data){
// 	console.log($.parseJSON(data));
// 	timedRefresh(500);
// }

// function timedRefresh(timeoutPeriod) {
// 	setTimeout("location.reload(true);",timeoutPeriod);
// }

// function removeJob(job){
// 	var answer = confirm("Are you sure you want to remove this job posting");
// 	if(answer){
// 		var job_id     = job.attr("data-job-id");
// 		var action     = "delete";
// 		$.ajax("jobs",{
// 			type: "POST",
// 			data:{action: action, job_id: job_id},
// 			success: handleRemoveJobResponse
// 		})
// 	}
// }

// function handleRemoveJobResponse (data) {
// 	var result = $.parseJSON(data);
// 	if (result.status == true){
// 		timedRefresh(500);
// 	}	
// 	else{
// 		alert("Unable to delete job item");
// 	}
// }




function checkBox(form){
	var industry  = [];
	var expertise = [];
	$("#upload-resource .checkbox input").each(function(){ 
		if (this.checked == true){
			console.log(this.getAttribute("data-type"));
			var type = this.getAttribute("data-type");
			if (type == "industry"){
				industry.push(getindustry(this));
			} 
			else if(type == "expertise"){
				expertise.push(getExpertise(this));
			}
		} 
	});

	industry.forEach(function(item){
		console.log(item);
	})
	expertise.forEach(function(item){
		console.log(item);
	})

	$("#tags-resource-industry").val(JSON.stringify(industry));
	$("#tags-resource-expertise").val(JSON.stringify(expertise));
	form.submit()
}

function sortResourceTags (resource, type) {
	


}

function getindustry (resource) {
	value = resource.getAttribute("data-value");
	return {"value": value}
}

function getExpertise(resource) {
	value    = resource.getAttribute("data-value");
	criteria = resource.getAttribute("data-expertise");
	return {"criteria": criteria, "value": value}
}