/*=====================
==== HELP FOR CSRF ====
=====================*/

// This function gets cookie with a given name
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getCookie('csrftoken');
 
/*
The functions below will create a header with csrftoken
*/
 
function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
function sameOrigin(url) {
    // test that a given url is a same-origin URL
    // url could be relative or scheme relative or absolute
    var host = document.location.host; // host + port
    var protocol = document.location.protocol;
    var sr_origin = '//' + host;
    var origin = protocol + sr_origin;
    // Allow absolute or scheme relative URLs to same origin
    return (url == origin || url.slice(0, origin.length + 1) == origin + '/') ||
        (url == sr_origin || url.slice(0, sr_origin.length + 1) == sr_origin + '/') ||
        // or any other URL that isn't scheme relative or absolute i.e relative.
        !(/^(\/\/|http:|https:).*/.test(url));
}
 
$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && sameOrigin(settings.url)) {
            // Send the token to same-origin, relative URLs only.
            // Send the token only if the method warrants CSRF protection
            // Using the CSRFToken value acquired earlier
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});

/*=================================
==== FORM SUBMIT ON INDEX PAGE ====
=================================*/
// Helper functions to encode urls
var stringToURL = function(str) {
	str = str.replace(/, /g, "__");
	str = str.replace(/ /g, "_");
	return str;
};
var URLToString = function(str) {
	str = str.replace(/__/g, ", ");
	str = str.replace(/_/g, " ");
	return str;
};

$('#index-search-submit').click(function(event){
	event.preventDefault();
	var place
	if ($('#index-text').val() == '') {
		place = '_';
	} else {
		place = stringToURL( $('#index-text').val() );
	}
	console.log(place);
	$('#index-search').attr('action', '/core/search/' + place)
	$('#index-search').submit();
});


/*========================================
==== SHOW/HIDE FILTERS ON SEARCH PAGE ====
========================================*/

$(document).ready(function(){
	
	$('#hide-filters').click(function(){
		$('#filters-container').slideUp(500, function(){
			$('#hide-filters').hide();
			$('#show-filters').css('display', 'block');
		});
	});
	$('#show-filters').click(function(){
		$('#filters-container').slideDown(500, function(){
			$('#hide-filters').css('display', 'block');
			$('#show-filters').hide();
		});
	});
});	
/*
$('#hide-filters').jBox('Tooltip', {
	content: 'Hide Search Filters',
	position: {x: 'center', y: 'bottom'},
	outside: 'y'
});
$('#show-filters').jBox('Tooltip', 
{
	content: 'Show Search Filters',
	position: {x: 'center', y: 'bottom'},
	outside: 'y'
});
*/


/*================================
==== MAKING MAP CANVAS SQUARE ====
================================*/
$(document).ready(function(){
	var width = $('#search-map-canvas').width();
	$('#search-map-canvas').height(width);
});

window.onresize = function(){
	var width = $('#search-map-canvas').width();
	$('#search-map-canvas').height(width);
};

/*===============================
==== MAKING MAP CANVAS FIXED ====
===============================*/
/*$(document).ready(function($){
	$.lockfixed('#search-results-col', {offset: {top: 92}});
})
*/

/*============================
==== CHANGING SIZE OF MAP ====
============================*/
$(document).ready(function(){
	$('#large-map').click(function(){
		$('#search-map-canvas').insertAfter($('#map-toggle')).width('99.5%');
		$('#small-map-panel').hide();
		
		var width = $('#search-map-canvas').width();
		$('#search-map-canvas').height(width);

		$('#large-map').addClass('active');
		$('#small-map').removeClass('active');
		$('#no-map').removeClass('active');
	});
	$('#small-map').click(function(){
		$('#small-map-panel').show().append($('#search-map-canvas'));

		$('#search-map-canvas').width('99.5%');
		var width = $('#search-map-canvas').width();
		$('#search-map-canvas').height(width);

		$('#large-map').removeClass('active');
		$('#small-map').addClass('active');
		$('#no-map').removeClass('active');
	});
	$('#no-map').click(function(){
		$('#search-map-canvas').slideUp(600);
		$('#large-map').removeClass('active');
		$('#small-map').removeClass('active');
		$('#no-map').addClass('active');
	});
});

/*===========================================
==== AJAX FORM SUBMISSION ON SEARCH PAGE ====
===========================================*/
$('#main-search-submit').click(function(event){
	event.preventDefault();
	$.ajax({
		type: 'POST',
		url: '/search_list/'
		data: {
			'location': $('#location').val(),
			'something': 'blah blah blah'
		},
		success: function(data) {
			console.log('DATADATADATA: ' + data);
			console.log('LOCATION: ' + $('#location').val())
		}
	});
	return false;
});


/*===========================================
==== NOTIFICATION OF NON-FUNCTIONAL BITS ====
===========================================*/
$('#login').jBox('Tooltip', 
{
	content: 'Just so you know, this button has no function at present.',
	position: {x: 'center', y: 'bottom'},
	outside: 'y'
});
$('#signup').jBox('Tooltip', 
{
	content: 'Just so you know, this button has no function at present.',
	position: {x: 'center', y: 'bottom'},
	outside: 'y'
});
/*$('.panel.search-panel').jBox('Tooltip',
{
	content: 'Just so you know, the search filters are not up and running right now.',
	position: {x: 'center', y: 'top'},
	outside: 'y'
});*/
$('.summary h2').jBox('Tooltip',
{
	content: 'TODO: Create restaurant template and link to it from here.',
	position: {x: 'left', y: 'top'},
	outside: 'y'
});