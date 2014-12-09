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

/*================================================
==== SHOW/HIDE FULL REVIEW ON RESTAURANT PAGE ====
================================================*/
$('.more').click(function(){
	var trunc = $(this).parent();
	$(trunc).hide();
	$(trunc).next().show();
})
$('.less').click(function(){
	var full = $(this).parent();
	$(full).hide();
	$(full).prev().show();
})