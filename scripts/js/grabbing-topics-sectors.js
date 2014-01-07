var target; var sector; $("#sectors input").on('ifChecked', function(event){ target = event.target; sector = target.parentNode.parentNode.getElementsByTagName('label')[0].innerHTML;});

var target; var value; var area; $("#topics input").on('ifChecked', function(event){ target = event.target; value = target.parentNode.parentNode.getElementsByTagName('label')[0].innerHTML; area = target.parentNode.parentNode.parentNode.parentNode.parentNode.getAttribute('id') });

