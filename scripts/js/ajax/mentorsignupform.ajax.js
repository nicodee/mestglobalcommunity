var current ;
fillEmailSummary();

$('#submit-form').click(
    function(){
        var length_topics  = $("#topics .checked .iCheck-helper");
        var length_sectors = $("#sectors .checked .iCheck-helper");

        if (length_topics.length == 0 && length_sectors.length == 0){
            alert("Please choose an area of expertise");   
            return false;
        }

        else{
                var program_data = JSON.stringify(populate_user_data());
                var user_data    = JSON.parse(getUserData());
                var userdata     = JSON.stringify(user_data);
                current          = $(this);
                makeAjaxCall(program_data, userdata);

                return false;
        }
    }
);

function fillEmailSummary(){
    var userdata = JSON.parse(getUserData());
    $("#email").val(userdata.emailAddress);
    if(userdata.summary != undefined){
        $("#summary-text").val(userdata.summary);
    }
}


function checks() {

}

function getUserData() {
    return $("#userdata").val();
}

function populate_user_data() {
    var program_type     = getProgram();  
    var email            = getEmail(); 
    var time_zone        = getTimeZone();
    var summary          = getSummary();
    var topics           = getTopics();
    var sectors          = getSectors();
    var referrals        = getReferrals();

    user_data= {
        "program_type": program_type,
        "email": email,
        "time_zone": time_zone,
        "mini_bio": summary,
        "topic": topics,
        "sector": sectors, 
        "referral": referrals
    } 
    return user_data;
}

//returns selected program
function getProgram() {
    return $('#programs :selected').attr('data-value');
}

//returns email address 
function getEmail() {
    return $("#email").val();
}

//returns a list of users time zone
function getTimeZone() {
    var time_zone = $("#DropDownTimezone>option:selected").val();
    return time_zone;
}

//returns short bio of user
function getSummary() {
    return $("#summary-text").val();
}

//returns a list of selected topics
function getTopics() {
    var topics = [];
    $("#topics .checked .iCheck-helper").each(
        function (){
            var topic             = {};
            var topic_container   = $(this).parent().find("input");
            topic['criteria']     = topic_container.attr("data-expertise");
            topic['value']        = topic_container.attr("data-value");
            topics.push(topic);
        });
    return topics;
}

//returns a list of selected sectors
function getSectors() {
    var sectors = [];
    $("#sectors .checked .iCheck-helper").each(
        function(){
            var sector      = {};
            var value       = $(this).parent().find("input").attr("data-value");
            sector["value"] = value;
            sectors.push(sector);  
        });
    return sectors;
}

//returns a list of referrals
function getReferrals() {
    var referrals = [];
    $("#method-of-referral .checked .iCheck-helper").each(
        function(){
            var referral = {};
            var parent = $(this).parent().parent();
            var value  = parent.find('label').text();
            referral['method'] = value;
            if ((value == "Conference") || (value == "other")){
                var specified= parent.find('input[type="text"]').val();
                referral['value'] = specified;
            }
            referrals.push(referral);
        });
    return referrals;
}

function makeAjaxCall(program, user_data) {
    alert("Please wait a while. Your form is being submitted.");
    $('#submit-form').attr('disabled', 'disabled');
    $(".last.previous.action-button").attr('disabled', 'disabled');
    $(".last.previous.action-button").addClass('disabled');
    $('#submit-form').addClass('disabled');
    $('#submit-form').val("Submitting");
    $(".fa-4x.fa.fa-cog.fa-spin").css("display", "block");
    var action = "submit_application";
    $.ajax('/signupmentor', {
        type: "POST",
        data:{user_data: user_data, program: program, action: action},
        success: handleResponse
    });
    return false;
}

function handleResponse(data){
    var result  = JSON.parse(data);
    var status = result.message;
    $(".submit-buttons-input").show();
    $(".submitting").remove(); 
    if (status == "success"){
        moveOn(result);
    }
    else if(status == "error"){
        $( "#duplicate-user" ).dialog({
          height: 140,
          modal: true
        });
        setTimeout(function() {
            window.location='/home';
        }, 2000);
    }
}



function moveOn(result){
    var name = result.firstname + " " + result.lastname; 
    var html = "Thank you "+name+".<br>Your application will be reviewed shortly.<br>If you have any questions, please contact <strong>info@meltwater.org</strong>";

    if(result.message=='success'){  
        $("#success_msg").html(html);  
        current_fs = current.parent();
        next_fs = current.parent().next();
        $("#progressbar li").eq($("fieldset").index(next_fs)).addClass("active");
        next_fs.show();
        current_fs.animate({opacity: 0}, {
            step: function(now, mx) {
                scale = 1 - (1 - now) * 0.2;
                left = (now * 50)+"%";
                opacity = 1 - now;
                current_fs.css({'transform': 'scale('+scale+')'});
                next_fs.css({'left': left, 'opacity': opacity});
            }, 
            duration: 800, 
            complete: function(){
                current_fs.hide();
                animating = false;
            }, 
            easing: 'easeInOutBack'
        });
        return false;
    }
    else {
        return false;
    }
}

