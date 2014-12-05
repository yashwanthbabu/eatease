/*=========================
==== RETURN STAR CLASS ====
=========================*/
function getStars(size, colour, value) {
	if (value == '0.5'){
		return 'star' + '-' + size + '-' + colour + '-' + 'half' 
	};
	if (value == '1.0'){
		return 'star' + '-' + size + '-' + colour + '-' + '1' 
	};
	if (value == '1.5'){
		return 'star' + '-' + size + '-' + colour + '-' + '1half'
	};
	if (value== '2.0'){
		return 'star' + '-' + size + '-' + colour + '-' + '2' 
	};
	if (value == '2.5'){
		return 'star' + '-' + size + '-' + colour + '-' + '2half'
	};
	if (value == '3.0'){
		return 'star' + '-' + size + '-' + colour + '-' + '3' 
	};
	if (value == '3.5'){
		return 'star' + '-' + size + '-' + colour + '-' + '3half' 
	};
	if (value == '4.0'){
		return 'star' + '-' + size + '-' + colour + '-' + '4' 
	};
	if (value == '4.5'){
		return 'star' + '-' + size + '-' + colour + '-' + '4half'
	};
	if (value == '5.0'){
		return 'star' + '-' + size + '-' + colour + '-' + '5'
	};
}

/*===============================================
==== PRELIMINARY FUNCTIONS FOR AJAX REQUESTS ====
===============================================*/

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
};

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
};

/*======================================================================
==== GETTING LOCATION FROM PLACES API AND NAVIGATING TO SEARCH PAGE ====
======================================================================*/
function  strToUrl(string) {
	string = string.replace(/, /g, '__');
	string = string.replace(/ /g, '_');
	return string;
};
// On Index Page
function placeSearch() {
	var place = $('#location').val();
	console.log(place);
	place = strToUrl(place);
	url = '/search/' + place;
	location.assign(url);
};
/*
$(document).ready(function(){
	var form = $('#front-page-search');
	$('#location').change(function(){
		$(form).attr('action', '/search/' + $(this).val());
	})
})
*/
// TEST
/*
$(document).ready (function(){
	$(document).click(function(){
		var whatis = $('#location').val();
		console.log(whatis);
	})
})
*/










// On Search Page
function placeUpdate() {
	var place = document.getElementById('search-location').value;
	place = strToUrl(place);
	location.assign(place);
}
/*===============================================================
==== FUNCION TO GET VALUES OF INPUTS AND PUT GET VARS IN URL ====
===============================================================*/
$(document).ready(function(){
	$('select').change(function(){
		updateUrl();
	});
	$('input[type="radio"]').change(function(){
		updateUrl();
	});
});

function updateUrl() {
	var urlStr = ''; // Create string for GET variables
	var sr = $('#searchRadius').val();
	urlStr += '?sr=';
	urlStr += sr;
	var radios = {
		overallrating : '', nutsrating: '', glutenrating: '', vegrating: '', veganrating: '', dairyrating: ''
	};
	$('input[type="radio"]:checked').each(function(){ // Adding values of checked radios into radios object
		radios[this.name] = this.value
	});
	for (filter in radios) { //  Adding ratings into URL String
		if (radios[filter]) { // If one of the radios has been checked
			if (filter === 'veganrating') { // Special case for vegan rating, shorthand ve
				urlStr += '&ve=';
				urlStr += radios[filter];
			} else {
				var snippet = '&' + filter.charAt(0) + '=' + radios[filter];
				urlStr += snippet;
			};
		};
	};
	location.assign(urlStr);
};

var TestVar = 'Test Variable'
/*===================================
==== SEARCH PAGE - CLEAR FILTERS ====
===================================*/
$(document).ready(function(){
	$('#clear-filters').click(function(){
		console.log(location);
		location.search = '';
	});	
});


/*====================================================
==== TOGGLE LIST/MAP BUTTON ACTIVE CLASS ON CLICK ====
====================================================*/
$(document).ready(function(){
	$('#list-view').click(function(){
		$(this).addClass('active');
		$('#map-view').removeClass('active');
		$('#search-map-canvas').hide();
	});
	$('#map-view').click(function(){
		$(this).addClass('active');
		$('#list-view').removeClass('active');
		$('#search-map-canvas').show();
	});
});


/*=================================
==== FORM SUBMIT ON INDEX PAGE ====
=================================*/
// Helper functions to encode urls
/*
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

/*
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
*/ //   PROBABLY GET RID OF THIS ++++++++++++++++++++++++++++++ ^

/*========================================
==== SHOW/HIDE FILTERS ON SEARCH PAGE ====
========================================*/

// DON'T NEED THIS FOR THE TIME BEING ++++++++++++++++++++
/*
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
*/	


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
// DON'T NEED THIS FOR THE TIME BEING ++++++++++++++++++++
/*
$(document).ready(function(){
	var width = $('#search-map-canvas').width();
	$('#search-map-canvas').height(width);
});

window.onresize = function(){
	var width = $('#search-map-canvas').width();
	$('#search-map-canvas').height(width);
};
*/


/*============================
==== CHANGING SIZE OF MAP ====
============================*/
// DON'T NEED THIS FOR THE TIME BEING ++++++++++++++++++++
/*
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
*/

/*===========================================
==== AJAX FORM SUBMISSION ON SEARCH PAGE ====
===========================================*/
// DON'T NEED THIS FOR THE TIME BEING ++++++++++++++++++++
/*
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
*/

/*===========================================
==== NOTIFICATION OF NON-FUNCTIONAL BITS ====
===========================================*/

// DON'T NEED THIS FOR THE TIME BEING ++++++++++++++++++++
/*
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
/*
$('.summary h2').jBox('Tooltip',
{
	content: 'TODO: Create restaurant template and link to it from here.',
	position: {x: 'left', y: 'top'},
	outside: 'y'
});
*/


////////////////
//Data Binding//
////////////////
function DataBinder(object_id) {
	var puSub = $({});

	var data_attr = 'bind-' + object_id;
	var message = object_id + ':change';

	$(document).on('change', '[data-' + data_attr + ']', function(e){
		var $input = $(this);

		pubSub.trigger(message, [ $input.data(data_attr), $input.val() ]);
	});

	pubSub.on(message, function(e, prop_name, new_val){
		$('[data-' + data_attr + '=' + prop_name + ']').each(function(){
			var $bound = $(this);

			if ($bound.is('input, textarea, select')) {
				$bound.val(new_val);
			}
			else {
				$bound.html(new_val);
			}
		});
	});
	return pubSub;
};