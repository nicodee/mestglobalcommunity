//changes ui of checkbox inputs
$(document).ready(function(){
				$('#topics input').iCheck({
					checkboxClass: 'icheckbox_flat-aero',
					radioClass: 'iradio_flat-aero'
				});
				$('#method-of-referral input[type="checkbox"]').iCheck({
					checkboxClass: 'icheckbox_flat-aero',
					radioClass: 'iradio_flat-aero'
				});
				$('#sectors input').iCheck({
					checkboxClass: 'icheckbox_flat-aero',
					radioClass: 'iradio_flat-aero'
				});
				$(".available-days").tagit();
				var input = $(".tagit-new");
				input.remove();
});
		
//calls 'fetchTime()' on clicking the '#add-new-button'			
$('#add-new-button').click(fetchTime);


//populates '#days-available' div with individual time schedules
function fetchTimeDetails(timeItem){
	var timeItem =timeItem;
	// console.log(timeItem);
	var days = {
			'Monday':'Mon', 
			'Tuesday':'Tue', 
			'Wednesday':'Wed', 
			'Thursday':'Thur', 
			'Friday':'Fri', 
			'Saturday':'Sat', 
			'Sunday':'Sun'
		};
	var availabelDays = [];

	$('.tagit-label').each(function(){
		var tag = $(this);
		availabelDays.push(days[$(this)[0].innerHTML]);
	});
	timeItem['days']=availabelDays;
	if(timeItem['days'].length == 0){
		alert('No day chosen!');
	}
	else {
		var dayString = timeItem['days'].join(", ");
		var timeZone = $('#DropDownTimezone :selected').val();
		$('#days-available').append('<ul class="dailySchedule fs-subtitle"><li class="time-zone">('+timeZone+')</li><li class="start-time">'+timeItem['startTime']+'</li><li>-</li><li class="end-time">'+timeItem['endTime']+'</li><li>&nbsp;on&nbsp;</li><li class="days">'+dayString+'</li><li><img src=\"scripts/img/delete.png\" class=\"delete\"></li></ul>');
		// var list = [];
		// $(".dailySchedule").each(function(){ list.push( $(this).text());});
		// console.log(list);
		populateAvailableDays();
		$('.delete').click(function(){
			deleteItem($(this));
		});
	}
}

//returns 12 hour format of time input
function returnTime(time){
	if(time == ""){
		return false;	 
	}
	else{
		timeArray  = time.split(':');
		var excess = timeArray[0] - 12;
		var second = getSecondPartTime(timeArray[1]);
		if(timeArray[0] == 0){
			return [[12,second].join(":"),'am'].join("");
		}
		else if (excess>0){
			if(excess==12 || excess==0){
				return [[excess,second].join(":"),'am'].join("");
			}
			else{
				return [[excess,second].join(":"),'pm'].join("");
			}
		}
		else{
			return [[timeArray[0],second].join(":"),'am'].join("");
		}
	}
}

function getSecondPartTime(second){
	if (second > 0){
		return second;
	}
	else{
		return "00";
	}
}
//function to grab time entered by user
function fetchTime(){
	var oldTime   = $.timePicker("#available-time-start").getTime();
	var newTime   = $.timePicker("#available-time-end").getTime();
	var startTime = oldTime.getUTCHours() + ":" + oldTime.getUTCMinutes();
	var endTime   = newTime.getUTCHours() + ":" + newTime.getUTCMinutes();
	if (startTime == "" || endTime == ""){
		alert('Please pick a valid time!')
	}
	else{
		startTime = returnTime(startTime);
		endTime   = returnTime(endTime);
		timeItem  = {'startTime':startTime, 'endTime':endTime};
		fetchTimeDetails(timeItem); 
	}
}


//dialogue box for confirmation before deleting a time schedule
function deleteItem(item){
	$( "#dialog-confirm" ).dialog({
        resizable: false,
        height:200,
        width:400,
        modal: true,
        buttons: {
          "Delete": function() {
            $( this ).dialog( "close" );
            var firstParent  = item.parent();
			var secondParent = firstParent.parent();
			secondParent.remove();
          },
          Cancel: function() {
            $( this ).dialog( "close" );
          }
        }
    });
}

//repopulating list of days for time schedule 
function populateAvailableDays(){
	$(".available-days").remove()
	$("#method-of-contact-two div").append("<ul id='available-days' class='available-days'><li>Monday</li><li>Tuesday</li><li>Wednesday</li><li>Thursday</li><li>Friday</li><li>Saturday</li><li>Sunday</li></ul>")
	$(".available-days").tagit()
	$(".tagit-new").remove()
}

jQuery(function() {
		    
    // An example how the two helper functions can be used to achieve 
    // advanced functionality.
    // - Linking: When changing the first input the second input is updated and the
    //   duration is kept.
    // - Validation: If the second input has a time earlier than the firs input,
    //   an error class is added.
    
    // Use default settings
    $("#available-time-start, #available-time-end").timePicker();

    // Store time used by duration.
	var oldTime = $.timePicker("#available-time-start").getTime();
    
    // Keep the duration between the two inputs.
    $("#available-time-start").change(function() {
		if ($("#available-time-end").val()) { // Only update when second input has a value.
			// Calculate duration.
			var duration = ($.timePicker("#available-time-end").getTime() - oldTime);
			var time = $.timePicker("#available-time-start").getTime();
			// Calculate and update the time in the second input.
			$.timePicker("#available-time-end").setTime(new Date(new Date(time.getTime() + duration)));
			oldTime = time;	
		}
    });
    // Validate.
    $("#available-time-end").change(function() {
		if($.timePicker("#available-time-start").getTime() >= $.timePicker(this).getTime()) {
			$(this).addClass("error");
		}
		else {
			$(this).removeClass("error");
		}
    });
		    
});

$("#programs").change(function()
    {
        var id=$(this).val();
        var programDetail = "#"+id;
        $('#program-details p').addClass('hidden-program');
        $(programDetail).removeClass('hidden-program');
        // alert(id); return false;

    });