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
});

