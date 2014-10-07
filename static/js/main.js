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
$('.panel.search-panel').jBox('Tooltip',
{
	content: 'Just so you know, the search filters are not up and running right now.',
	position: {x: 'center', y: 'top'},
	outside: 'y'
});
$('.summary h2').jBox('Tooltip',
{
	content: 'TODO: Create restaurant template and link to it from here.',
	position: {x: 'left', y: 'top'},
	outside: 'y'
});