$(document).ready(
	function () {
		$("#uploadresource").submit(
			function(e) {
				e.preventDefault();
				checkBox(this);
		});
	}
)

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

console.log("hello");