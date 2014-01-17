$(document).ready(function(){

	// $("#sectors").find('input').each(function(){
	// var self = $(this),
	//   label = self.next(),
	//   label_text = label.text();

	// label.remove();
	// self.iCheck({
	//   checkboxClass: 'icheckbox_line-purple',
	//   radioClass: 'iradio_line-purple',
	//   insert: '<div class="icheck_line-icon"></div>' + label_text
	// });

	// });
	$('#sectors input').iCheck({
					checkboxClass: 'icheckbox_flat-purple',
					radioClass: 'iradio_flat-purple'
	});
	$('#topics input').iCheck({
					checkboxClass: 'icheckbox_flat-pink',
					radioClass: 'iradio_flat-pink'
	});
	// $("#topics").find('input').each(function(){
	// var self = $(this),
	//   label = self.next(),
	//   label_text = label.text();

	// label.remove();
	// self.iCheck({
	//   checkboxClass: 'icheckbox_line-red',
	//   radioClass: 'iradio_line-red',
	//   insert: '<div class="icheck_line-icon"></div>' + label_text
	// });
	// });

	// $('#topics input').iCheck('check');
	// $('#sectors input').iCheck('check');

	$("#search-results-tags").find('input').each(function(){
	var self = $(this),
	  label = self.next(),
	  label_text = label.text();

	label.remove();
	self.iCheck({
	  checkboxClass: 'icheckbox_line-green',
	  radioClass: 'iradio_line-green',
	  insert: '<div class="icheck_line-icon"></div>' + label_text
	});
	});
//////////////////////////////////////////////////////////

	// $(".accordion-toggle").click(function(){
	// 	var $icon = $(this).find("#icon");
	// 	if ($icon.hasClass("icon-chevron-up")){
	// 		$icon.removeClass("icon-chevron-up");	
	// 		$icon.addClass("icon-chevron-down");
	// 	}
	// 	else if ($icon.hasClass("icon-chevron-down")){
	// 		$icon.removeClass("icon-chevron-down");	
	// 		$icon.addClass("icon-chevron-up");
	// 	}		
	// });
   /////////////////////////////////////////////////////////////////////////

	$('.viewport').mouseenter(function(e) {
        $(this).children('a').children('img').animate({ height: '299', left: '0', top: '0', width: '450'}, 100);
        $(this).children('a').children('span').fadeIn(200);
    }).mouseleave(function(e) {
        $(this).children('a').children('img').animate({ height: '332', left: '-20', top: '-20', width: '500'}, 100);
        $(this).children('a').children('span').fadeOut(200);
    });

     ///////////////////////////////////////////////////////////////
    //hiding and showing search options 
    $(".tab-content").show();
    var sector_nav = "disabled";
    var topic_nav = "disabled";
    $('#topic-nav').click(function (e) {
    	// if($("#topic-nav").hasClass("active")){
    		// $(".tab-content").css("display","");
    		// $(this).dblclick();
    		if(topic_nav=="disabled"){
    			sector_nav = "disabled";
    			topic_nav = "active";
    			// console.log(topic_nav);
    			$(".tab-content").show();
    			// console.log($(".tab-content"));
    		}
    		else if(topic_nav=="active"){
    			topic_nav = "disabled";
    			console.log(topic_nav);
    			$(".tab-content").css("display","none");
    			$("#topic-nav").removeAttr("class");	
    			// removeActive("#topic-nav");
    		}

	});


    $('#sector-nav a').click(function () {
    	if(sector_nav=="disabled"){
    			topic_nav  = "disabled"; 
    			sector_nav = "active";
    			// console.log(topic_nav);
    			$(".tab-content").show();
    			// console.log($(".tab-content"));
    		}
    		else if(sector_nav=="active"){
    			sector_nav= "disabled";
    			// console.log(topic_nav);
    			$(".tab-content").css("display","none");
    			$("#topic-nav").removeAttr("class");	
    			// removeActive("#topic-nav");
    		}
	});



	var sectors= [];
   	$("#sectors .iCheck-helper").click( function(){
   		var query_sectors = $("#search-button-data-sectors");
   		if($(this).hasClass("sector")){
   			var firstParent = $(this).parent();
  			var secondParent = firstParent.parent();
  			sectors.forEach(function(item) {
		  		if(item.value == secondParent.text()){
					var item_index = sectors.indexOf(item); // Find the index
					if(item_index!=-1) sectors.splice(item_index, 1);
		  			// console.log(sectors.indexOf(item));
		  			// var jsonData = JSON.stringify(sectors);
		  			// console.log(jsonData);
		  		}
			});
  			$(this).removeClass("sector");
   	        $(this).removeClass("search-results-tags");
   	        $("#sectors ul").append(secondParent[0]);
   		}
   		else {

	   		var sector= {};

	   		var list_div = $(this).parent();
	   		var list_item = list_div.parent();
	   		var search_results_tags = $("#search-results-tags ul span");
	   		$(this).addClass("sector");
	   	    $(this).addClass("search-results-tags");
	   		search_results_tags.append(list_item);

	   		sector["value"] = list_item.text();
	   		sectors.push(sector);
   		}
   		var jsonData = JSON.stringify(sectors);
	   		query_sectors.attr("value", jsonData);
			console.log(jsonData);

   	});

   	var criterias=[ 
				   	"analytics",
				   	"business-development",
   					"design",
   					"human-resources",
   					"legal",
   					"technology",
   					"operations",
   					"marketing" ,
   					"finance-accounting",
				   	"project-management",
   					"sales",
   					"mest-strike-force",
   					"list-tech"
   					];
   	var special_criterias=['1','2','3' 
					];


	var topics = [];
  	$("#topics .iCheck-helper").click( function(){
  		var query_topics = $("#search-button-data-topics");
	   	if($(this).hasClass("topic")){
	   		for (var i = criterias.length - 1; i >= 0; i--) {
	   			if($(this).hasClass(criterias[i])){
	   				// console.log(criterias[i]);
	   				var criteria =criterias[i];
	   				var firstParent = $(this).parent();
		  			var secondParent = firstParent.parent();

		  			topics.forEach(function(item) {
				  		if(item.value == secondParent.text()){
							var item_index = topics.indexOf(item); // Find the index
							if(item_index!=-1) topics.splice(item_index, 1);
				  			// console.log(topics.indexOf(item));
				  			// var jsonData = JSON.stringify(topics);
				  			// console.log(jsonData);
				  		}
					});

		  			$(this).removeClass("topic");
		  			$(this).removeClass(criteria);
		   	        $(this).removeClass("search-results-tags");
		   	        var tag = "#"+criteria+" ul span";
		   	        $(tag).append(secondParent[0]);
	   			}
	   		};



   		}
   		else{
	  	    var topic                  = {};
	  	    var search_results_tags    = $("#search-results-tags ul span");
			var list_firstParent       = $(this).parent();
			var list_secondParent      = list_firstParent.parent();///what i'm actually looking for
			var list_thirdParent       = list_secondParent.parent();
			var list_fourthParent      = list_thirdParent.parent();
			var list_fifthParent       = list_fourthParent.parent();
			var criteria               = list_fifthParent[0].getAttribute("id");
			// var criteria               = list_fifthParent[0].firstElementChild.innerText.toLowerCase();
			var value                  = list_secondParent.text();
			$(this).addClass("topic");
	   	    $(this).addClass("search-results-tags");
			search_results_tags.append(list_secondParent);
			if ((criteria == special_criterias[0])|| (criteria == special_criterias[1]) || (criteria == special_criterias[2])){
				newCriteria = criteria.split(" ");
				criteria = newCriteria[0]+"-"+newCriteria[1];
	   	    	$(this).addClass(criteria);
				topic["criteria"] = criteria;
			}
			else if (criteria == special_criterias[3]){
				newCriteria = criteria.split("/");
				criteria = newCriteria[0]+"-"+newCriteria[1];			
	   	   		$(this).addClass(criteria);
				topic["criteria"] = criteria;
			}
			else {
				$(this).addClass(criteria);
				topic["criteria"] = criteria;

			}
			
			topic["value"]    = value;
			topics.push(topic);
			
   		}
			var jsonData = JSON.stringify(topics);
			query_topics.attr("value",jsonData);
			console.log(jsonData);


   	});


	// $("#search-button").click(
	// 	function(){
	// 			var query = $("<input>").attr("type", "hidden").attr("name", "mydata").attr("id","mydata").val(JSON.stringify(sectors));
	// 			$('#search-button-form').append($(query));
	// });

});
