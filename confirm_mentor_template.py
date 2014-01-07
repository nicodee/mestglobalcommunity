template = '''<html>
<head>
<title>MEST Mentor Platform_email</title>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
<meta name="viewport"
content="width=320, target-densitydpi=device-dpi">
<style type="text/css">
/* Mobile-specific Styles */
@media only screen and (max-width: 660px) {
table[class=w0], td[class=w0] { width: 0 !important; }
table[class=w10], td[class=w10], img[class=w10] { width:10px !important; }
table[class=w15], td[class=w15], img[class=w15] { width:5px !important; }
table[class=w30], td[class=w30], img[class=w30] { width:10px !important; }
table[class=w60], td[class=w60], img[class=w60] { width:10px !important; }
table[class=w125], td[class=w125], img[class=w125] { width:80px !important; }
table[class=w130], td[class=w130], img[class=w130] { width:55px !important; }
table[class=w140], td[class=w140], img[class=w140] { width:90px !important; }
table[class=w160], td[class=w160], img[class=w160] { width:180px !important; }
table[class=w170], td[class=w170], img[class=w170] { width:100px !important; }
table[class=w180], td[class=w180], img[class=w180] { width:80px !important; }
table[class=w195], td[class=w195], img[class=w195] { width:80px !important; }
table[class=w220], td[class=w220], img[class=w220] { width:80px !important; }
table[class=w240], td[class=w240], img[class=w240] { width:180px !important; }
table[class=w255], td[class=w255], img[class=w255] { width:185px !important; }
table[class=w275], td[class=w275], img[class=w275] { width:135px !important; }
table[class=w280], td[class=w280], img[class=w280] { width:135px !important; }
table[class=w300], td[class=w300], img[class=w300] { width:140px !important; }
table[class=w325], td[class=w325], img[class=w325] { width:95px !important; }
table[class=w360], td[class=w360], img[class=w360] { width:140px !important; }
table[class=w410], td[class=w410], img[class=w410] { width:180px !important; }
table[class=w470], td[class=w470], img[class=w470] { width:200px !important; }
table[class=w580], td[class=w580], img[class=w580] { width:280px !important; }
table[class=w640], td[class=w640], img[class=w640] { width:300px !important; }
table[class*=hide], td[class*=hide], img[class*=hide], p[class*=hide], span[class*=hide] { display:none !important; }
table[class=h0], td[class=h0] { height: 0 !important; }
p[class=footer-content-left] { text-align: center !important; }
#headline p { font-size: 30px !important; }
.article-content, #left-sidebar{ -webkit-text-size-adjust: 90% !important; -ms-text-size-adjust: 90% !important; }
.header-content, .footer-content-left {-webkit-text-size-adjust: 80% !important; -ms-text-size-adjust: 80% !important;}
img { height: auto; line-height: 100%;}
}
/* Client-specific Styles */
#outlook a { padding: 0; } /* Force Outlook to provide a "view in browser" button. */
body { width: 100% !important; }
.ReadMsgBody { width: 100%; }
.ExternalClass { width: 100%; display:block !important; } /* Force Hotmail to display emails at full width */
/* Reset Styles */
/* Add 100px so mobile switch bar doesn't cover street address. */
body { background-color: #dedede; margin: 0; padding: 0; }
img { outline: none; text-decoration: none; display: block;}
br, strong br, b br, em br, i br { line-height:100%; }
h1, h2, h3, h4, h5, h6 { line-height: 100% !important; -webkit-font-smoothing: antialiased; }
h1 a, h2 a, h3 a, h4 a, h5 a, h6 a { color: blue !important; }
h1 a:active, h2 a:active, h3 a:active, h4 a:active, h5 a:active, h6 a:active { color: red !important; }
/* Preferably not the same color as the normal header link color. There is limited support for psuedo classes in email clients, this was added just for good measure. */
h1 a:visited, h2 a:visited, h3 a:visited, h4 a:visited, h5 a:visited, h6 a:visited { color: purple !important; }
/* Preferably not the same color as the normal header link color. There is limited support for psuedo classes in email clients, this was added just for good measure. */
table td, table tr { border-collapse: collapse; }
.yshortcuts, .yshortcuts a, .yshortcuts a:link,.yshortcuts a:visited, .yshortcuts a:hover, .yshortcuts a span {
color: black; text-decoration: none !important; border-bottom: none !important; background: none !important;
} /* Body text color for the New Yahoo. This example sets the font of Yahoo's Shortcuts to black. */
/* This most probably won't work in all email clients. Don't include code blocks in email. */
code {
white-space: normal;
word-break: break-all;
}
#background-table { background-color: #dedede; }
/* Webkit Elements */
#top-bar { border-radius:6px 6px 0px 0px; -moz-border-radius: 6px 6px 0px 0px; -webkit-border-radius:6px 6px 0px 0px; -webkit-font-smoothing: antialiased; background-color: #c7c7c7; color: #ededed; }
#top-bar a { font-weight: bold; color: #ffffff; text-decoration: none;}
#footer { border-radius:0px 0px 6px 6px; -moz-border-radius: 0px 0px 6px 6px; -webkit-border-radius:0px 0px 6px 6px; -webkit-font-smoothing: antialiased; }
/* Fonts and Content */
body, td { font-family: 'Helvetica Neue', Arial, Helvetica, Geneva, sans-serif; }
.header-content, .footer-content-left, .footer-content-right { -webkit-text-size-adjust: none; -ms-text-size-adjust: none; }
/* Prevent Webkit and Windows Mobile platforms from changing default font sizes on header and footer. */
.header-content { font-size: 12px; color: #ededed; }
.header-content a { font-weight: bold; color: #ffffff; text-decoration: none; }
#headline p { color: #444444; font-family: 'Helvetica Neue', Arial, Helvetica, Geneva, sans-serif; font-size: 36px; text-align: center; margin-top:0px; margin-bottom:30px; }
#headline p a { color: #444444; text-decoration: none; }
.article-title { font-size: 18px; line-height:24px; color: #b0b0b0; font-weight:bold; margin-top:0px; margin-bottom:18px; font-family: 'Helvetica Neue', Arial, Helvetica, Geneva, sans-serif; }
.article-title a { color: #b0b0b0; text-decoration: none; }
.article-title.with-meta {margin-bottom: 0;}
.article-meta { font-size: 13px; line-height: 20px; color: #ccc; font-weight: bold; margin-top: 0;}
.article-content { font-size: 13px; line-height: 18px; color: #444444; margin-top: 0px; margin-bottom: 18px; font-family: 'Helvetica Neue', Arial, Helvetica, Geneva, sans-serif; }
.article-content a { color: #2f82de; font-weight:bold; text-decoration:none; }
.article-content img { max-width: 100% }
.article-content ol, .article-content ul { margin-top:0px; margin-bottom:18px; margin-left:19px; padding:0; }
.article-content li { font-size: 13px; line-height: 18px; color: #444444; }
.article-content li a { color: #2f82de; text-decoration:underline; }
.article-content p {margin-bottom: 15px;}
.footer-content-left { font-size: 12px; line-height: 15px; color: #ededed; margin-top: 0px; margin-bottom: 15px; }
.footer-content-left a { color: #ffffff; font-weight: bold; text-decoration: none; }
.footer-content-right { font-size: 11px; line-height: 16px; color: #ededed; margin-top: 0px; margin-bottom: 15px; }
.footer-content-right a { color: #ffffff; font-weight: bold; text-decoration: none; }
#footer { background-color: #c7c7c7; color: #ededed; }
#footer a { color: #ffffff; text-decoration: none; font-weight: bold; }
#permission-reminder { white-space: normal; }
#street-address { color: #b0b0b0; white-space: normal; }
</style>
<!--[if gte mso 9]>
<style _tmplitem="715" >
.article-content ol, .article-content ul {
margin: 0 0 0 24px;
padding: 0;
list-style-position: inside;
}
</style>
<![endif]-->
<script type="text/javascript">var NREUMQ=NREUMQ||[];NREUMQ.push(["mark","firstbyte",new Date().getTime()]);</script>
</head>
<body>
<table id="background-table" border="0" cellpadding="0" cellspacing="0"
width="100%">
<tbody>
<tr>
<td align="center" bgcolor="#dedede">
<table class="w640" style="margin: 0pt 10px;" border="0"
cellpadding="0" cellspacing="0" width="640">
<tbody>
<tr>
<td class="w640" height="20" width="640"><br>
</td>
</tr>
<tr>
<td class="w640" width="640">
<table id="top-bar" class="w640" bgcolor="#ffffff"
border="0" cellpadding="0" cellspacing="0" width="640">
<tbody>
<tr>
<td class="w15" width="15"><br>
</td>
<td class="w325" align="left" valign="middle"
width="350">
<table class="w325" border="0" cellpadding="0"
cellspacing="0" width="350">
<tbody>
<tr>
<td class="w325" height="8" width="350"><br>
</td>
</tr>
</tbody>
</table>
<div class="header-content"><a
href="http://preview.createsend1.com/t/d-e-l-l-r/">Web Version</a><span
class="hide">&nbsp;&nbsp;| MEST Mentor Platform Confirmation<br>
</span></div>
<table class="w325" border="0" cellpadding="0"
cellspacing="0" width="350">
<tbody>
<tr>
<td class="w325" height="8" width="350"><br>
</td>
</tr>
</tbody>
</table>
</td>
<td class="w30" width="30"><br>
</td>
<td class="w255" align="right" valign="middle"
width="255">
<table class="w255" border="0" cellpadding="0"
cellspacing="0" width="255">
<tbody>
<tr>
<td class="w255" height="8" width="255"><br>
</td>
</tr>
</tbody>
</table>
<table border="0" cellpadding="0" cellspacing="0">
<tbody>
<tr>
<td valign="middle"><a
href="http://preview.createsend1.com/t/d-fb-l-l-t/" rel="cs_facebox"><img
src="https://img.createsend1.com/img/templatebuilder/like-glyph.png"
alt="Facebook icon" border="0" height="14" width="8"></a></td>
<td width="3"><br>
</td>
<td valign="middle">
<div class="header-content"><a target="_blank"
href="https://www.facebook.com/MESTghana" rel="cs_facebox">Like</a></div>
</td>
<td class="w10" width="10"><br>
</td>
<td valign="middle"><a
href="http://preview.createsend1.com/t/d-tw-l-l-d/"><img
src="https://img.createsend1.com/img/templatebuilder/tweet-glyph.png"
alt="Twitter icon" border="0" height="13" width="17"></a></td>
<td width="3"><br>
</td>
<td valign="middle">
<div class="header-content"><a target="_blank"
href="https://twitter.com/MESTghana">Tweet</a></div>
</td>
<td class="w10" width="10"><br>
</td>
<td valign="middle"><a
href="http://client.forwardtomyfriend.com/d-yhiku-Preview-k" lang="en"><img
src="https://img.createsend1.com/img/templatebuilder/forward-glyph.png"
alt="Forward icon" border="0" height="14" width="19"></a></td>
<td width="3"><br>
</td>
<td valign="middle">
<div class="header-content"><a
href="info@meltwater.org" lang="en">Forward</a></div>
</td>
</tr>
</tbody>
</table>
<table class="w255" border="0" cellpadding="0"
cellspacing="0" width="255">
<tbody>
<tr>
<td class="w255" height="8" width="255"><br>
</td>
</tr>
</tbody>
</table>
</td>
<td class="w15" width="15"><br>
</td>
</tr>
</tbody>
</table>
</td>
</tr>
<tr>
<td id="header" class="w640" align="center"
bgcolor="#ffffff" width="640">
<div style="text-align: center;" align="center"> <img
alt="header"
style="border: 0px solid ; display: inline; width: 640px; height: 206px;"
class="w640" src="http://blog.meltwater.org/wp-content/uploads/2013/12/win_header.png" label="Header Image"
id="customHeaderImage" align="top"> </div>
</td>
</tr>
<tr>
<td class="w640" bgcolor="#ffffff" height="30" width="640"><br>
</td>
</tr>
<tr id="simple-content-row">
<td class="w640" bgcolor="#ffffff" width="640">
<table class="w640" border="0" cellpadding="0"
cellspacing="0" width="640">
<tbody>
<tr>
<td class="w30" width="30"><br>
</td>
<td class="w580" width="580"> <repeater> <layout
label="Text only"> </layout></repeater>
<table class="w580" border="0" cellpadding="0"
cellspacing="0" width="580">
<tbody>
<tr>
<td class="w580" width="580">
<p class="article-title" align="left">Welcome
to the MEST Mentor Platform, *|username|*!<br>
</p>
<div class="article-content" align="left"><span
style="color: rgb(102, 102, 102);">Thank you for signing up to be a part of the MEST Mentor Platform. 
Whether you are interested in being a Subject Area Specialist, an MBA Consultant,
a Senior Advisor or an Expert in Residence, 
we really appreciate your offer to support MEST and MEST Incubator companies.
</span><br style="color: rgb(102, 102, 102);">
<br style="color: rgb(102, 102, 102);">
<span style="color: rgb(102, 102, 102);">
You have now been added to our database and 
we will reach out when your valuable skills are in demand!</span><br
style="color: rgb(102, 102, 102);">
<br>
</div>
</td>
</tr>
</tbody>
</table>
<layout label="Text with full-width image"> </layout>
<table style="width: 580px; height: 554px;"
class="w580" border="0" cellpadding="0" cellspacing="0">
<tbody>
<tr>
<td class="w580" width="580">
<p class="article-title" align="left"><a
href="http://mestghana.wpengine.com/incubator/portfolio/"
target="_blank">Our Portfolio </a><br>
</p>
</td>
</tr>
<tr>
<td style="text-align: center;" class="w580"
width="580"><a
href="http://mestghana.wpengine.com/incubator/portfolio/"><img
style="border: 0px solid ; width: 574px; height: 432px;"
alt="portfolio" label="Image" class="w580"
src="http://blog.meltwater.org/wp-content/uploads/2013/12/all-logos-portfolio.png"></a></td>
</tr>
<tr style="color: rgb(153, 153, 153);">
<td class="w580" width="580">
<div class="article-content" align="left">
<p><big><big><br>
</big></big></p>
<p><big><big>You're in good company :</big></big></p>
</div>
</td>
</tr>
</tbody>
</table>
<layout label="Text with right-aligned image"> </layout>
<table style="width: 580px; height: 374px;"
class="w580" border="0" cellpadding="0" cellspacing="0">
<tbody>
<tr>
<td class="w580" style="width: 580px;">
<p class="article-title" align="left">Senior
Advisor: Micheal Geer<br>
</p>
<table align="right" border="0" cellpadding="0"
cellspacing="0">
<tbody>
<tr>
<td class="w30" width="15"><br>
</td>
<td><img
style="border-radius:100px; border: 0px solid ; width: 200px; height: 200px;" alt="MG"
label="Image" class="w300"
src="http://mestglobalcommunity.appspot.com/scripts/img/michael_geer.jpg"></td>
</tr>
<tr>
<td class="w30" height="5" width="15"><br>
</td>
<td><br>
</td>
</tr>
</tbody>
</table>
<div class="article-content" align="left">
Micheal works with <a href='http://saya.im/'>Saya</a>, one of our 13 incubator companies.
<br>
<br>
He learned about the consumer internet while helping build <a href="http://badoo.com">Badoo</a>, 
a social network that is popular in Eastern Europe and South America. 
In addition to setting up Badoo's London office, he helped take the social network from 0 to 70 million users.
<br>
<br>
Micheal left Badoo in July 2010 to advise and mentor early stage startups, 
and joined the team at Dream Industries to build technology that 
empowers people to spread knowledge globally.
<br>
<br>
He believes technology, the exchange of knowledge, 
and simple user flows can dramatically improve people's lives. 
He works every day to make this happen.
<br>
<br>
</div>
</td>
</tr>
<tr>
<td class="w580" height="10" width="580"><br>
</td>
</tr>
</tbody>
</table>
<layout label="Text with left-aligned image"> </layout>
<table class="w580" border="0" cellpadding="0"
cellspacing="0" width="580">
<tbody>
<tr>
<td class="w580" width="580">
<p class="article-title" align="left">Expert in
Residence: Susannah Raub<br>
</p>
<table align="left" border="0" cellpadding="0"
cellspacing="0">
<tbody>
<tr>
<td><img
style="border-radius:100px; border: 0px solid ; width: 200px; height: 199px;" alt="SR"
label="Image" class="w300"
src="http://mestglobalcommunity.appspot.com/scripts/img/sraub.jpg"></td>
<td class="w30" width="15"><br>
</td>
</tr>
<tr>
<td><br>
</td>
<td class="w30" height="5" width="15"><br>
</td>
</tr>
</tbody>
</table>
<div class="article-content" align="left">
Susannah is a Silicon Valley-based Google engineer who spent a three month sabbatical at MEST in 2012.
<br>
<br>
While on the ground, she taught our Entrepreneurs in Training at 
the School and advised companies in the Incubator, 
and quickly become an invaluable resource to all.
<br>
<br>
</div>
</td>
</tr>
<tr>
<td class="w580" height="10" width="580"><br>
</td>
</tr>
</tbody>
</table>
<layout label="What happens next?"> </layout>
<table class="w580" border="0" cellpadding="0"
cellspacing="0" width="580">
<tbody>
<tr>
<td class="w580" width="580">
<p class="article-title" align="left">
What happens next?<br>
</p>
<div class="article-content" align="left">
Now that you're a member of the MEST Mentor Platform, our entrepreneurs will be able to look you up in our database and reach out with questions.
<br>
<br>
If you have any questions, kindly contact us at 
<a href="mailto:info@meltwater.org"><span style="font-size:15px;font-family:Arial;color:#1155cc;background-color:transparent;font-weight:normal;font-style:normal;font-variant:normal;text-decoration:underline;vertical-align:baseline;">info@meltwater.org</span></a>.
<br>
<br>
Regards,<br>
The MEST Team
</div>
</td>
</tr>
<tr>
<td class="w580" height="10" width="580"><br>
</td>
</tr>
</tbody>
</table>
<layout label="Two columns"></layout><layout
label="Image gallery"></layout></td>
<td class="w30" width="30"><br>
</td>
</tr>
</tbody>
</table>
</td>
</tr>
<tr>
<td class="w640" bgcolor="#ffffff" height="15" width="640"><br>
</td>
</tr>
<tr>
<td class="w640" width="640">
<table id="footer" class="w640" bgcolor="#c7c7c7" border="0"
cellpadding="0" cellspacing="0" width="640">
<tbody>
<tr>
<td class="w30" width="30"><br>
</td>
<td class="w580 h0" height="30" width="360"><br>
</td>
<td class="w0" width="60"><br>
</td>
<td class="w0" width="160"><br>
</td>
<td class="w30" width="30"><br>
</td>
</tr>
<tr>
<td class="w30" width="30"><br>
</td>
<td class="w580" valign="top" width="360"> <span
class="hide">
<p id="permission-reminder"
class="footer-content-left" align="left"><span>You're receiving this
because you signed up to be part of the MEST Mentor Platform.</span></p>
</span>
<p class="footer-content-left" align="left"><a
href="http://client.updatemyprofile.com/d-l-2AD73FFF-l-o" lang="en">Edit
your subscription</a> | <a
href="http://preview.createsend1.com/t/d-u-l-l-b/">Unsubscribe</a></p>
</td>
<td class="hide w0" width="60"><br>
</td>
<td class="hide w0" valign="top" width="160">
<p id="street-address" class="footer-content-right"
align="right"><span>MEST - Accra, Ghana and San Francisco, USA.</span></p>
</td>
<td class="w30" width="30"><br>
</td>
</tr>
<tr>
<td class="w30" width="30"><br>
</td>
<td class="w580 h0" height="15" width="360"><br>
</td>
<td class="w0" width="60"><br>
</td>
<td class="w0" width="160"><br>
</td>
<td class="w30" width="30"><br>
</td>
</tr>
</tbody>
</table>
</td>
</tr>
<tr>
<td class="w640" height="60" width="640"><br>
</td>
</tr>
</tbody>
</table>
</td>
</tr>
</tbody>
</table>
<img src="https://createsend1.com/t/d-o-l-l/o.gif"
style="border: 0pt none ! important; margin: 0pt ! important; padding: 0pt ! important; height: 1px ! important; width: 1px ! important;"
alt="" border="0" height="1" width="1">
<script type="text/javascript"> if (!NREUMQ.f) {NREUMQ.f=function() {NREUMQ.push(["load",new Date().getTime()]);var e=document.createElement("script"); e.type="text/javascript"; e.src=(("http:"===document.location.protocol)?"http:":"https:") + "//" + "js-agent.newrelic.com/nr-100.js"; document.body.appendChild(e);if(NREUMQ.a)NREUMQ.a();};NREUMQ.a=window.onload;window.onload=NREUMQ.f;};NREUMQ.push(["nrfj","beacon-1.newrelic.com","3cbe1f8970","140681","NlZWZUYFWUMEUxZZDA8ccF5AKlJEJl8MRBEOX1hURktjVQhADlEXBEAbQUYBQVkARw==",0,46,new Date().getTime(),"3CEBCC9EE80377CF","","","",""]);</script>
</body>
</html>'''

signup_template = ''' 
<html>
<head>
<title>MEST Mentor Platform_email</title>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
<meta name="viewport"
content="width=320, target-densitydpi=device-dpi">
<style type="text/css">
/* Mobile-specific Styles */
@media only screen and (max-width: 660px) {
table[class=w0], td[class=w0] { width: 0 !important; }
table[class=w10], td[class=w10], img[class=w10] { width:10px !important; }
table[class=w15], td[class=w15], img[class=w15] { width:5px !important; }
table[class=w30], td[class=w30], img[class=w30] { width:10px !important; }
table[class=w60], td[class=w60], img[class=w60] { width:10px !important; }
table[class=w125], td[class=w125], img[class=w125] { width:80px !important; }
table[class=w130], td[class=w130], img[class=w130] { width:55px !important; }
table[class=w140], td[class=w140], img[class=w140] { width:90px !important; }
table[class=w160], td[class=w160], img[class=w160] { width:180px !important; }
table[class=w170], td[class=w170], img[class=w170] { width:100px !important; }
table[class=w180], td[class=w180], img[class=w180] { width:80px !important; }
table[class=w195], td[class=w195], img[class=w195] { width:80px !important; }
table[class=w220], td[class=w220], img[class=w220] { width:80px !important; }
table[class=w240], td[class=w240], img[class=w240] { width:180px !important; }
table[class=w255], td[class=w255], img[class=w255] { width:185px !important; }
table[class=w275], td[class=w275], img[class=w275] { width:135px !important; }
table[class=w280], td[class=w280], img[class=w280] { width:135px !important; }
table[class=w300], td[class=w300], img[class=w300] { width:140px !important; }
table[class=w325], td[class=w325], img[class=w325] { width:95px !important; }
table[class=w360], td[class=w360], img[class=w360] { width:140px !important; }
table[class=w410], td[class=w410], img[class=w410] { width:180px !important; }
table[class=w470], td[class=w470], img[class=w470] { width:200px !important; }
table[class=w580], td[class=w580], img[class=w580] { width:280px !important; }
table[class=w640], td[class=w640], img[class=w640] { width:300px !important; }
table[class*=hide], td[class*=hide], img[class*=hide], p[class*=hide], span[class*=hide] { display:none !important; }
table[class=h0], td[class=h0] { height: 0 !important; }
p[class=footer-content-left] { text-align: center !important; }
#headline p { font-size: 30px !important; }
.article-content, #left-sidebar{ -webkit-text-size-adjust: 90% !important; -ms-text-size-adjust: 90% !important; }
.header-content, .footer-content-left {-webkit-text-size-adjust: 80% !important; -ms-text-size-adjust: 80% !important;}
img { height: auto; line-height: 100%;}
}
/* Client-specific Styles */
#outlook a { padding: 0; } /* Force Outlook to provide a "view in browser" button. */
body { width: 100% !important; }
.ReadMsgBody { width: 100%; }
.ExternalClass { width: 100%; display:block !important; } /* Force Hotmail to display emails at full width */
/* Reset Styles */
/* Add 100px so mobile switch bar doesn't cover street address. */
body { background-color: #dedede; margin: 0; padding: 0; }
img { outline: none; text-decoration: none; display: block;}
br, strong br, b br, em br, i br { line-height:100%; }
h1, h2, h3, h4, h5, h6 { line-height: 100% !important; -webkit-font-smoothing: antialiased; }
h1 a, h2 a, h3 a, h4 a, h5 a, h6 a { color: blue !important; }
h1 a:active, h2 a:active, h3 a:active, h4 a:active, h5 a:active, h6 a:active { color: red !important; }
/* Preferably not the same color as the normal header link color. There is limited support for psuedo classes in email clients, this was added just for good measure. */
h1 a:visited, h2 a:visited, h3 a:visited, h4 a:visited, h5 a:visited, h6 a:visited { color: purple !important; }
/* Preferably not the same color as the normal header link color. There is limited support for psuedo classes in email clients, this was added just for good measure. */
table td, table tr { border-collapse: collapse; }
.yshortcuts, .yshortcuts a, .yshortcuts a:link,.yshortcuts a:visited, .yshortcuts a:hover, .yshortcuts a span {
color: black; text-decoration: none !important; border-bottom: none !important; background: none !important;
} /* Body text color for the New Yahoo. This example sets the font of Yahoo's Shortcuts to black. */
/* This most probably won't work in all email clients. Don't include code blocks in email. */
code {
white-space: normal;
word-break: break-all;
}
#background-table { background-color: #dedede; }
/* Webkit Elements */
#top-bar { border-radius:6px 6px 0px 0px; -moz-border-radius: 6px 6px 0px 0px; -webkit-border-radius:6px 6px 0px 0px; -webkit-font-smoothing: antialiased; background-color: #c7c7c7; color: #ededed; }
#top-bar a { font-weight: bold; color: #ffffff; text-decoration: none;}
#footer { border-radius:0px 0px 6px 6px; -moz-border-radius: 0px 0px 6px 6px; -webkit-border-radius:0px 0px 6px 6px; -webkit-font-smoothing: antialiased; }
/* Fonts and Content */
body, td { font-family: 'Helvetica Neue', Arial, Helvetica, Geneva, sans-serif; }
.header-content, .footer-content-left, .footer-content-right { -webkit-text-size-adjust: none; -ms-text-size-adjust: none; }
/* Prevent Webkit and Windows Mobile platforms from changing default font sizes on header and footer. */
.header-content { font-size: 12px; color: #ededed; }
.header-content a { font-weight: bold; color: #ffffff; text-decoration: none; }
#headline p { color: #444444; font-family: 'Helvetica Neue', Arial, Helvetica, Geneva, sans-serif; font-size: 36px; text-align: center; margin-top:0px; margin-bottom:30px; }
#headline p a { color: #444444; text-decoration: none; }
.article-title { font-size: 18px; line-height:24px; color: #b0b0b0; font-weight:bold; margin-top:0px; margin-bottom:18px; font-family: 'Helvetica Neue', Arial, Helvetica, Geneva, sans-serif; }
.article-title a { color: #b0b0b0; text-decoration: none; }
.article-title.with-meta {margin-bottom: 0;}
.article-meta { font-size: 13px; line-height: 20px; color: #ccc; font-weight: bold; margin-top: 0;}
.article-content { font-size: 13px; line-height: 18px; color: #444444; margin-top: 0px; margin-bottom: 18px; font-family: 'Helvetica Neue', Arial, Helvetica, Geneva, sans-serif; }
.article-content a { color: #2f82de; font-weight:bold; text-decoration:none; }
.article-content img { max-width: 100% }
.article-content ol, .article-content ul { margin-top:0px; margin-bottom:18px; margin-left:19px; padding:0; }
.article-content li { font-size: 13px; line-height: 18px; color: #444444; }
.article-content li a { color: #2f82de; text-decoration:underline; }
.article-content p {margin-bottom: 15px;}
.footer-content-left { font-size: 12px; line-height: 15px; color: #ededed; margin-top: 0px; margin-bottom: 15px; }
.footer-content-left a { color: #ffffff; font-weight: bold; text-decoration: none; }
.footer-content-right { font-size: 11px; line-height: 16px; color: #ededed; margin-top: 0px; margin-bottom: 15px; }
.footer-content-right a { color: #ffffff; font-weight: bold; text-decoration: none; }
#footer { background-color: #c7c7c7; color: #ededed; }
#footer a { color: #ffffff; text-decoration: none; font-weight: bold; }
#permission-reminder { white-space: normal; }
#street-address { color: #b0b0b0; white-space: normal; }
</style>
<!--[if gte mso 9]>
<style _tmplitem="715" >
.article-content ol, .article-content ul {
margin: 0 0 0 24px;
padding: 0;
list-style-position: inside;
}
</style>
<![endif]-->
<script type="text/javascript">var NREUMQ=NREUMQ||[];NREUMQ.push(["mark","firstbyte",new Date().getTime()]);</script>
</head>
<body>
<table id="background-table" border="0" cellpadding="0" cellspacing="0"
width="100%">
<tbody>
<tr>
<td align="center" bgcolor="#dedede">
<table class="w640" style="margin: 0pt 10px;" border="0"
cellpadding="0" cellspacing="0" width="640">
<tbody>
<tr>
<td class="w640" height="20" width="640"><br>
</td>
</tr>
<tr>
<td class="w640" width="640">
<table id="top-bar" class="w640" bgcolor="#ffffff" border="0" cellpadding="0" cellspacing="0" width="640">
	<tbody>
	<tr>
	<td class="w15" width="15"><br>
	</td>
	<td class="w325" align="left" valign="middle"
	width="350">
	<table class="w325" border="0" cellpadding="0" cellspacing="0" width="350">
		<tbody>
		<tr>
		<td class="w325" height="8" width="350"><br>
		</td>
		</tr>
		</tbody>
	</table>
	<div class="header-content"><a
	href="http://preview.createsend1.com/t/d-e-l-l-r/">Web Version</a><span
	class="hide">&nbsp;&nbsp;| MEST Mentor Platform Confirmation<br>
	</span></div>
	<table class="w325" border="0" cellpadding="0" cellspacing="0" width="350">
		<tbody>
		<tr>
		<td class="w325" height="8" width="350"><br>
		</td>
		</tr>
		</tbody>
	</table>
	</td>
	<td class="w30" width="30"><br>
	</td>
	<td class="w255" align="right" valign="middle" width="255">
	<table class="w255" border="0" cellpadding="0" cellspacing="0" width="255">
		<tbody>
			<tr>
				<td class="w255" height="8" width="255"><br>
				</td>
			</tr>
		</tbody>
	</table>
	<table border="0" cellpadding="0" cellspacing="0">
		<tbody>
			<tr>
				<td valign="middle">
					<a href="http://preview.createsend1.com/t/d-fb-l-l-t/" rel="cs_facebox">
						<img src="https://img.createsend1.com/img/templatebuilder/like-glyph.png" 
						alt="Facebook icon" border="0" height="14" width="8">
					</a>
				</td>
				<td width="3">
					<br>
				</td>
				<td valign="middle">
					<div class="header-content">
						<a target="_blank" href="https://www.facebook.com/MESTghana" rel="cs_facebox">
							Like
						</a>
					</div>
				</td>
				<td class="w10" width="10">
					<br>
				</td>
				<td valign="middle">
					<a href="http://preview.createsend1.com/t/d-tw-l-l-d/">
						<img src="https://img.createsend1.com/img/templatebuilder/tweet-glyph.png" 
						alt="Twitter icon" border="0" height="13" width="17">
					</a>
				</td>
				<td width="3">
					<br>
				</td>
				<td valign="middle">
					<div class="header-content">
						<a target="_blank" href="https://twitter.com/MESTghana">
							Tweet
						</a>
					</div>
				</td>
				<td class="w10" width="10"><br>
				</td>
				<td valign="middle">
					<a href="http://client.forwardtomyfriend.com/d-yhiku-Preview-k" lang="en">
						<img src="https://img.createsend1.com/img/templatebuilder/forward-glyph.png"
						alt="Forward icon" border="0" height="14" width="19">
					</a>
				</td>
				<td width="3">
					<br>
				</td>
				<td valign="middle">
					<div class="header-content">
						<a href="info@meltwater.org" lang="en">
							Forward
						</a>
					</div>
				</td>
			</tr>
		</tbody>
	</table>
	<table class="w255" border="0" cellpadding="0" cellspacing="0" width="255">
		<tbody>
		<tr>
		<td class="w255" height="8" width="255"><br>
		</td>
		</tr>
		</tbody>
	</table>
	</td>
	<td class="w15" width="15"><br>
	</td>
	</tr>
	</tbody>
</table>
</td>
</tr>
<tr>
<td id="header" class="w640" align="center"
bgcolor="#ffffff" width="640">
<div style="text-align: center;" align="center"> <img
alt="header"
style="border: 0px solid ; display: inline; width: 640px; height: 206px;"
class="w640" src="http://blog.meltwater.org/wp-content/uploads/2013/12/win_header.png" label="Header Image"
id="customHeaderImage" align="top"> </div>
</td>
</tr>
<tr>
<td class="w640" bgcolor="#ffffff" height="30" width="640"><br>
</td>
</tr>
<tr id="simple-content-row">
<td class="w640" bgcolor="#ffffff" width="640">
<table class="w640" border="0" cellpadding="0"
cellspacing="0" width="640">
<tbody>
<tr>
<td class="w30" width="30"><br>
</td>
<td class="w580" width="580"> <repeater> <layout
label="Text only"> </layout></repeater>
<table class="w580" border="0" cellpadding="0" cellspacing="0" width="580">
	<tbody>
		<tr>
			<td class="w580" width="580">
				<div class="article-content" align="left">
					<span style="color: rgb(102, 102, 102);">
						Thank you for applying to be *|userprofile|* on the MEST Mentor Platform
					</span>
					<br	style="color: rgb(102, 102, 102);">
					<span style="color: rgb(102, 102, 102);">
						Your application will be reviewed shortly.
					</span>
					<br	style="color: rgb(102, 102, 102);">
					<span style="color: rgb(102, 102, 102);">
						If you have any questions, please contact <a href="mailto:info@meltwater.org">info@meltwater.org</a>
					</span>
				</div>
			</td>
		</tr>
		<tr>
			<td class="w580" width="580">
				<div class="article-content" align="left">
					<span style="color: rgb(102, 102, 102);">
						Regards,
						<br>
						The MEST Team
					</span>
				</div>
			</td>
		</tr>
	</tbody>
</table>
<layout label="Two columns"></layout><layout
label="Image gallery"></layout></td>
<td class="w30" width="30"><br>
</td>
</tr>
</tbody>
</table>
</td>
</tr>
<tr>
<td class="w640" bgcolor="#ffffff" height="15" width="640"><br>
</td>
</tr>
<tr>
<td class="w640" width="640">
<table id="footer" class="w640" bgcolor="#c7c7c7" border="0"
cellpadding="0" cellspacing="0" width="640">
<tbody>
<tr>
<td class="w30" width="30"><br>
</td>
<td class="w580 h0" height="30" width="360"><br>
</td>
<td class="w0" width="60"><br>
</td>
<td class="w0" width="160"><br>
</td>
<td class="w30" width="30"><br>
</td>
</tr>
<tr>
<td class="w30" width="30"><br>
</td>
<td class="w580" valign="top" width="360"> <span
class="hide">
<p id="permission-reminder"
class="footer-content-left" align="left"><span>You're receiving this
because you signed up to be part of the MEST Mentor Platform.</span></p>
</span>
<p class="footer-content-left" align="left"><a
href="http://client.updatemyprofile.com/d-l-2AD73FFF-l-o" lang="en">Edit
your subscription</a> | <a
href="http://preview.createsend1.com/t/d-u-l-l-b/">Unsubscribe</a></p>
</td>
<td class="hide w0" width="60"><br>
</td>
<td class="hide w0" valign="top" width="160">
<p id="street-address" class="footer-content-right"
align="right"><span>MEST - Accra, Ghana and San Francisco, USA.</span></p>
</td>
<td class="w30" width="30"><br>
</td>
</tr>
<tr>
<td class="w30" width="30"><br>
</td>
<td class="w580 h0" height="15" width="360"><br>
</td>
<td class="w0" width="60"><br>
</td>
<td class="w0" width="160"><br>
</td>
<td class="w30" width="30"><br>
</td>
</tr>
</tbody>
</table>
</td>
</tr>
<tr>
<td class="w640" height="60" width="640"><br>
</td>
</tr>
</tbody>
</table>
</td>
</tr>
</tbody>
</table>
<img src="https://createsend1.com/t/d-o-l-l/o.gif"
style="border: 0pt none ! important; margin: 0pt ! important; padding: 0pt ! important; height: 1px ! important; width: 1px ! important;"
alt="" border="0" height="1" width="1">
<script type="text/javascript"> if (!NREUMQ.f) {NREUMQ.f=function() {NREUMQ.push(["load",new Date().getTime()]);var e=document.createElement("script"); e.type="text/javascript"; e.src=(("http:"===document.location.protocol)?"http:":"https:") + "//" + "js-agent.newrelic.com/nr-100.js"; document.body.appendChild(e);if(NREUMQ.a)NREUMQ.a();};NREUMQ.a=window.onload;window.onload=NREUMQ.f;};NREUMQ.push(["nrfj","beacon-1.newrelic.com","3cbe1f8970","140681","NlZWZUYFWUMEUxZZDA8ccF5AKlJEJl8MRBEOX1hURktjVQhADlEXBEAbQUYBQVkARw==",0,46,new Date().getTime(),"3CEBCC9EE80377CF","","","",""]);</script>
</body>
</html>
'''
entrepreneur_template = ''' 
<html>
<head>
<title>MEST Mentor Platform_email</title>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
<meta name="viewport"
content="width=320, target-densitydpi=device-dpi">
<style type="text/css">
/* Mobile-specific Styles */
@media only screen and (max-width: 660px) {
table[class=w0], td[class=w0] { width: 0 !important; }
table[class=w10], td[class=w10], img[class=w10] { width:10px !important; }
table[class=w15], td[class=w15], img[class=w15] { width:5px !important; }
table[class=w30], td[class=w30], img[class=w30] { width:10px !important; }
table[class=w60], td[class=w60], img[class=w60] { width:10px !important; }
table[class=w125], td[class=w125], img[class=w125] { width:80px !important; }
table[class=w130], td[class=w130], img[class=w130] { width:55px !important; }
table[class=w140], td[class=w140], img[class=w140] { width:90px !important; }
table[class=w160], td[class=w160], img[class=w160] { width:180px !important; }
table[class=w170], td[class=w170], img[class=w170] { width:100px !important; }
table[class=w180], td[class=w180], img[class=w180] { width:80px !important; }
table[class=w195], td[class=w195], img[class=w195] { width:80px !important; }
table[class=w220], td[class=w220], img[class=w220] { width:80px !important; }
table[class=w240], td[class=w240], img[class=w240] { width:180px !important; }
table[class=w255], td[class=w255], img[class=w255] { width:185px !important; }
table[class=w275], td[class=w275], img[class=w275] { width:135px !important; }
table[class=w280], td[class=w280], img[class=w280] { width:135px !important; }
table[class=w300], td[class=w300], img[class=w300] { width:140px !important; }
table[class=w325], td[class=w325], img[class=w325] { width:95px !important; }
table[class=w360], td[class=w360], img[class=w360] { width:140px !important; }
table[class=w410], td[class=w410], img[class=w410] { width:180px !important; }
table[class=w470], td[class=w470], img[class=w470] { width:200px !important; }
table[class=w580], td[class=w580], img[class=w580] { width:280px !important; }
table[class=w640], td[class=w640], img[class=w640] { width:300px !important; }
table[class*=hide], td[class*=hide], img[class*=hide], p[class*=hide], span[class*=hide] { display:none !important; }
table[class=h0], td[class=h0] { height: 0 !important; }
p[class=footer-content-left] { text-align: center !important; }
#headline p { font-size: 30px !important; }
.article-content, #left-sidebar{ -webkit-text-size-adjust: 90% !important; -ms-text-size-adjust: 90% !important; }
.header-content, .footer-content-left {-webkit-text-size-adjust: 80% !important; -ms-text-size-adjust: 80% !important;}
img { height: auto; line-height: 100%;}
}
/* Client-specific Styles */
#outlook a { padding: 0; } /* Force Outlook to provide a "view in browser" button. */
body { width: 100% !important; }
.ReadMsgBody { width: 100%; }
.ExternalClass { width: 100%; display:block !important; } /* Force Hotmail to display emails at full width */
/* Reset Styles */
/* Add 100px so mobile switch bar doesn't cover street address. */
body { background-color: #dedede; margin: 0; padding: 0; }
img { outline: none; text-decoration: none; display: block;}
br, strong br, b br, em br, i br { line-height:100%; }
h1, h2, h3, h4, h5, h6 { line-height: 100% !important; -webkit-font-smoothing: antialiased; }
h1 a, h2 a, h3 a, h4 a, h5 a, h6 a { color: blue !important; }
h1 a:active, h2 a:active, h3 a:active, h4 a:active, h5 a:active, h6 a:active { color: red !important; }
/* Preferably not the same color as the normal header link color. There is limited support for psuedo classes in email clients, this was added just for good measure. */
h1 a:visited, h2 a:visited, h3 a:visited, h4 a:visited, h5 a:visited, h6 a:visited { color: purple !important; }
/* Preferably not the same color as the normal header link color. There is limited support for psuedo classes in email clients, this was added just for good measure. */
table td, table tr { border-collapse: collapse; }
.yshortcuts, .yshortcuts a, .yshortcuts a:link,.yshortcuts a:visited, .yshortcuts a:hover, .yshortcuts a span {
color: black; text-decoration: none !important; border-bottom: none !important; background: none !important;
} /* Body text color for the New Yahoo. This example sets the font of Yahoo's Shortcuts to black. */
/* This most probably won't work in all email clients. Don't include code blocks in email. */
code {
white-space: normal;
word-break: break-all;
}
#background-table { background-color: #dedede; }
/* Webkit Elements */
#top-bar { border-radius:6px 6px 0px 0px; -moz-border-radius: 6px 6px 0px 0px; -webkit-border-radius:6px 6px 0px 0px; -webkit-font-smoothing: antialiased; background-color: #c7c7c7; color: #ededed; }
#top-bar a { font-weight: bold; color: #ffffff; text-decoration: none;}
#footer { border-radius:0px 0px 6px 6px; -moz-border-radius: 0px 0px 6px 6px; -webkit-border-radius:0px 0px 6px 6px; -webkit-font-smoothing: antialiased; }
/* Fonts and Content */
body, td { font-family: 'Helvetica Neue', Arial, Helvetica, Geneva, sans-serif; }
.header-content, .footer-content-left, .footer-content-right { -webkit-text-size-adjust: none; -ms-text-size-adjust: none; }
/* Prevent Webkit and Windows Mobile platforms from changing default font sizes on header and footer. */
.header-content { font-size: 12px; color: #ededed; }
.header-content a { font-weight: bold; color: #ffffff; text-decoration: none; }
#headline p { color: #444444; font-family: 'Helvetica Neue', Arial, Helvetica, Geneva, sans-serif; font-size: 36px; text-align: center; margin-top:0px; margin-bottom:30px; }
#headline p a { color: #444444; text-decoration: none; }
.article-title { font-size: 18px; line-height:24px; color: #b0b0b0; font-weight:bold; margin-top:0px; margin-bottom:18px; font-family: 'Helvetica Neue', Arial, Helvetica, Geneva, sans-serif; }
.article-title a { color: #b0b0b0; text-decoration: none; }
.article-title.with-meta {margin-bottom: 0;}
.article-meta { font-size: 13px; line-height: 20px; color: #ccc; font-weight: bold; margin-top: 0;}
.article-content { font-size: 13px; line-height: 18px; color: #444444; margin-top: 0px; margin-bottom: 18px; font-family: 'Helvetica Neue', Arial, Helvetica, Geneva, sans-serif; }
.article-content a { color: #2f82de; font-weight:bold; text-decoration:none; }
.article-content img { max-width: 100% }
.article-content ol, .article-content ul { margin-top:0px; margin-bottom:18px; margin-left:19px; padding:0; }
.article-content li { font-size: 13px; line-height: 18px; color: #444444; }
.article-content li a { color: #2f82de; text-decoration:underline; }
.article-content p {margin-bottom: 15px;}
.footer-content-left { font-size: 12px; line-height: 15px; color: #ededed; margin-top: 0px; margin-bottom: 15px; }
.footer-content-left a { color: #ffffff; font-weight: bold; text-decoration: none; }
.footer-content-right { font-size: 11px; line-height: 16px; color: #ededed; margin-top: 0px; margin-bottom: 15px; }
.footer-content-right a { color: #ffffff; font-weight: bold; text-decoration: none; }
#footer { background-color: #c7c7c7; color: #ededed; }
#footer a { color: #ffffff; text-decoration: none; font-weight: bold; }
#permission-reminder { white-space: normal; }
#street-address { color: #b0b0b0; white-space: normal; }
</style>
<!--[if gte mso 9]>
<style _tmplitem="715" >
.article-content ol, .article-content ul {
margin: 0 0 0 24px;
padding: 0;
list-style-position: inside;
}
</style>
<![endif]-->
<script type="text/javascript">var NREUMQ=NREUMQ||[];NREUMQ.push(["mark","firstbyte",new Date().getTime()]);</script>
</head>
<body>
<table id="background-table" border="0" cellpadding="0" cellspacing="0"
width="100%">
<tbody>
<tr>
<td align="center" bgcolor="#dedede">
<table class="w640" style="margin: 0pt 10px;" border="0"
cellpadding="0" cellspacing="0" width="640">
<tbody>
<tr>
<td class="w640" height="20" width="640"><br>
</td>
</tr>
<tr>
<td class="w640" width="640">
<table id="top-bar" class="w640" bgcolor="#ffffff" border="0" cellpadding="0" cellspacing="0" width="640">
	<tbody>
	<tr>
	<td class="w15" width="15"><br>
	</td>
	<td class="w325" align="left" valign="middle"
	width="350">
	<table class="w325" border="0" cellpadding="0" cellspacing="0" width="350">
		<tbody>
		<tr>
		<td class="w325" height="8" width="350"><br>
		</td>
		</tr>
		</tbody>
	</table>
	<div class="header-content"><a
	href="http://preview.createsend1.com/t/d-e-l-l-r/">Web Version</a><span
	class="hide">&nbsp;&nbsp;| MEST Mentor Platform Confirmation<br>
	</span></div>
	<table class="w325" border="0" cellpadding="0" cellspacing="0" width="350">
		<tbody>
		<tr>
		<td class="w325" height="8" width="350"><br>
		</td>
		</tr>
		</tbody>
	</table>
	</td>
	<td class="w30" width="30"><br>
	</td>
	<td class="w255" align="right" valign="middle" width="255">
	<table class="w255" border="0" cellpadding="0" cellspacing="0" width="255">
		<tbody>
			<tr>
				<td class="w255" height="8" width="255"><br>
				</td>
			</tr>
		</tbody>
	</table>
	<table border="0" cellpadding="0" cellspacing="0">
		<tbody>
			<tr>
				<td valign="middle">
					<a href="http://preview.createsend1.com/t/d-fb-l-l-t/" rel="cs_facebox">
						<img src="https://img.createsend1.com/img/templatebuilder/like-glyph.png" 
						alt="Facebook icon" border="0" height="14" width="8">
					</a>
				</td>
				<td width="3">
					<br>
				</td>
				<td valign="middle">
					<div class="header-content">
						<a target="_blank" href="https://www.facebook.com/MESTghana" rel="cs_facebox">
							Like
						</a>
					</div>
				</td>
				<td class="w10" width="10">
					<br>
				</td>
				<td valign="middle">
					<a href="http://preview.createsend1.com/t/d-tw-l-l-d/">
						<img src="https://img.createsend1.com/img/templatebuilder/tweet-glyph.png" 
						alt="Twitter icon" border="0" height="13" width="17">
					</a>
				</td>
				<td width="3">
					<br>
				</td>
				<td valign="middle">
					<div class="header-content">
						<a target="_blank" href="https://twitter.com/MESTghana">
							Tweet
						</a>
					</div>
				</td>
				<td class="w10" width="10"><br>
				</td>
				<td valign="middle">
					<a href="http://client.forwardtomyfriend.com/d-yhiku-Preview-k" lang="en">
						<img src="https://img.createsend1.com/img/templatebuilder/forward-glyph.png"
						alt="Forward icon" border="0" height="14" width="19">
					</a>
				</td>
				<td width="3">
					<br>
				</td>
				<td valign="middle">
					<div class="header-content">
						<a href="info@meltwater.org" lang="en">
							Forward
						</a>
					</div>
				</td>
			</tr>
		</tbody>
	</table>
	<table class="w255" border="0" cellpadding="0" cellspacing="0" width="255">
		<tbody>
		<tr>
		<td class="w255" height="8" width="255"><br>
		</td>
		</tr>
		</tbody>
	</table>
	</td>
	<td class="w15" width="15"><br>
	</td>
	</tr>
	</tbody>
</table>
</td>
</tr>
<tr>
<td id="header" class="w640" align="center"
bgcolor="#ffffff" width="640">
<div style="text-align: center;" align="center"> <img
alt="header"
style="border: 0px solid ; display: inline; width: 640px; height: 206px;"
class="w640" src="http://blog.meltwater.org/wp-content/uploads/2013/12/win_header.png" label="Header Image"
id="customHeaderImage" align="top"> </div>
</td>
</tr>
<tr>
<td class="w640" bgcolor="#ffffff" height="30" width="640"><br>
</td>
</tr>
<tr id="simple-content-row">
<td class="w640" bgcolor="#ffffff" width="640">
<table class="w640" border="0" cellpadding="0"
cellspacing="0" width="640">
<tbody>
<tr>
<td class="w30" width="30"><br>
</td>
<td class="w580" width="580"> <repeater> <layout
label="Text only"> </layout></repeater>
<table class="w580" border="0" cellpadding="0" cellspacing="0" width="580">
	<tbody>
		<tr>
			<td class="w580" width="580">
				<p class="article-title" align="left">
					Welcome to the MEST Mentor Platform, *|username|*!
					<br>
				</p>
				<div class="article-content" align="left">
					<span style="color: rgb(102, 102, 102);">
						Thank you for signing up to be a part of the <a href="*|confirmation_url|*">MEST Mentor Platform</a>. 
						Your account as an entrepreneur has been approved.
					</span>
					<br	style="color: rgb(102, 102, 102);">
					<br>
				</div>
			</td>
		</tr>
		<tr>
			<td class="w580" width="580">
				<p class="article-title" align="left">
					How to Get Started
					<br>
				</p>
				<div class="article-content" align="left">
					<span style="color: rgb(102, 102, 102);">
						1) Ask yourself, "What's the biggest challenge I'm currently facing as an entrepreneur?"
					</span>
					<br style="color: rgb(102, 102, 102);">
					<span style="color: rgb(102, 102, 102);">
						2) Log into the MEST Mentor Platform and find a Mentor who can help you overcome that challenge!
					</span>
					<br style="color: rgb(102, 102, 102);">
					<br style="color: rgb(102, 102, 102);">
					<a href="*|confirmation_url|*">Find a Mentor</a>
					<br style="color: rgb(102, 102, 102);">
					<br style="color: rgb(102, 102, 102);">
					<span style="color: rgb(102, 102, 102);">
						Regards,
						<br>
						The MEST Team
					</span>
					<br style="color: rgb(102, 102, 102);">
					<br>
				</div>
			</td>
		</tr>
	</tbody>
</table>
<layout label="Two columns"></layout><layout
label="Image gallery"></layout></td>
<td class="w30" width="30"><br>
</td>
</tr>
</tbody>
</table>
</td>
</tr>
<tr>
<td class="w640" bgcolor="#ffffff" height="15" width="640"><br>
</td>
</tr>
<tr>
<td class="w640" width="640">
<table id="footer" class="w640" bgcolor="#c7c7c7" border="0"
cellpadding="0" cellspacing="0" width="640">
<tbody>
<tr>
<td class="w30" width="30"><br>
</td>
<td class="w580 h0" height="30" width="360"><br>
</td>
<td class="w0" width="60"><br>
</td>
<td class="w0" width="160"><br>
</td>
<td class="w30" width="30"><br>
</td>
</tr>
<tr>
<td class="w30" width="30"><br>
</td>
<td class="w580" valign="top" width="360"> <span
class="hide">
<p id="permission-reminder"
class="footer-content-left" align="left"><span>You're receiving this
because you signed up to be part of the MEST Mentor Platform.</span></p>
</span>
<p class="footer-content-left" align="left"><a
href="http://client.updatemyprofile.com/d-l-2AD73FFF-l-o" lang="en">Edit
your subscription</a> | <a
href="http://preview.createsend1.com/t/d-u-l-l-b/">Unsubscribe</a></p>
</td>
<td class="hide w0" width="60"><br>
</td>
<td class="hide w0" valign="top" width="160">
<p id="street-address" class="footer-content-right"
align="right"><span>MEST - Accra, Ghana and San Francisco, USA.</span></p>
</td>
<td class="w30" width="30"><br>
</td>
</tr>
<tr>
<td class="w30" width="30"><br>
</td>
<td class="w580 h0" height="15" width="360"><br>
</td>
<td class="w0" width="60"><br>
</td>
<td class="w0" width="160"><br>
</td>
<td class="w30" width="30"><br>
</td>
</tr>
</tbody>
</table>
</td>
</tr>
<tr>
<td class="w640" height="60" width="640"><br>
</td>
</tr>
</tbody>
</table>
</td>
</tr>
</tbody>
</table>
<img src="https://createsend1.com/t/d-o-l-l/o.gif"
style="border: 0pt none ! important; margin: 0pt ! important; padding: 0pt ! important; height: 1px ! important; width: 1px ! important;"
alt="" border="0" height="1" width="1">
<script type="text/javascript"> if (!NREUMQ.f) {NREUMQ.f=function() {NREUMQ.push(["load",new Date().getTime()]);var e=document.createElement("script"); e.type="text/javascript"; e.src=(("http:"===document.location.protocol)?"http:":"https:") + "//" + "js-agent.newrelic.com/nr-100.js"; document.body.appendChild(e);if(NREUMQ.a)NREUMQ.a();};NREUMQ.a=window.onload;window.onload=NREUMQ.f;};NREUMQ.push(["nrfj","beacon-1.newrelic.com","3cbe1f8970","140681","NlZWZUYFWUMEUxZZDA8ccF5AKlJEJl8MRBEOX1hURktjVQhADlEXBEAbQUYBQVkARw==",0,46,new Date().getTime(),"3CEBCC9EE80377CF","","","",""]);</script>
</body>
</html>						
'''