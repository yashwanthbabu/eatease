var markers = [];
var MY_MAPTYPE_ID = 'custom_style';
var map;
var restid = [];
var geocoder;
var mapCenter;
var place;

function initialize() {

	geocoder = new google.maps.Geocoder();
	if ($('#search-location')) {
		place = $('#search-location').attr('value');
	};
	geocoder.geocode({
		'address': place
	}, function(results, status){
		if (status == google.maps.GeocoderStatus.OK) {
			map.setCenter(results[0].geometry.location);
		} else {
			map.setCenter(new google.maps.LatLng(51.4516,-2.5876));
		}
	});

	/*=============
	| Map Options |
	=============*/
	var mapOptions = {
		center: new google.maps.LatLng(51.4516,-2.5876),
		zoom: 12,
		panControl: false,
		zoomControlOptions: {
    		style: google.maps.ZoomControlStyle.SMALL
  		},
  		mapTypeControlOptions: {
      		mapTypeIds: [google.maps.MapTypeId.ROADMAP, MY_MAPTYPE_ID]
    	},
    	//mapTypeId: MY_MAPTYPE_ID
	};

	/*==================
	| Defining the map |
	==================*/
	map = new google.maps.Map(document.getElementById("search-map-canvas"), mapOptions);

	/*=====================================
	| AJAX request to get restaurant data |
	=====================================*/
	/*
	var sr = $('#searchRadius option:selected').val();
	// Getting object with all checked radio values
	var radios = {
		overallrating : '', nutsrating: '', glutenrating: '', vegrating: '', veganrating: '', dairyrating: ''
	};
	$('input[type="radio"]:checked').each(function(){ // Adding values of checked radios into radios object
		radios[this.name] = this.value
	});
	console.log(radios);
	console.log(restArray);
	// ++++++ AJAX ++++++
	$.get(
		'/filter_test',
		{
			'sr': sr,
			'o':  radios['overallrating'],
			'n':  radios['nutsrating'],
			'g':  radios['glutenrating'],
			'v':  radios['vegrating'],
			've': radios['veganrating'],
			'd':  radios['dairyrating'] 
		},
		function(response){
			// +++ Add all places to map +++
			console.log(response);
			for (var i = 0; i < response.length; i++)
			{
				resp = response[i]['fields'];
				console.log(response[i]);
				//Getting x and y coords
				coords = resp['coords'];
				coords = coords.split(',');

				//Setting content for info box
				var infoPic     = '<div style="height: 100px;"></div>'
				var infoHeading = '<div class="infoContainer"><h3>' + resp['name'] + '</h3>';
				var infoStars   = '<span class="' + resp['overall_star_class'] + '"></span>'
				var infoReview1 = '<h4>' + '"' + resp['recent_reviews1'] + '"' + '</h4>';
				var infoReview2 = '<h4>' + '"' + resp['recent_reviews2'] + '"' + '</h4></div>';

				var infoContent = infoPic + infoHeading + infoStars + infoReview1 + infoReview2;

				var marker = new google.maps.Marker(
					{
						position: new google.maps.LatLng(coords[0], coords[1]),
						title:    resp['name'], // For when you hover over icon
						map:      map,
						icon: 	  {url: '../../static/img/pin-green-new.png' },
						html:     infoContent,
						id:       resp['id']
					}
				);
				//Push marker to markers array
				markers.push(marker);
				//Options for infoWindow
				var infoWindowOptions = {
					maxWidth: 0,
					alignBottom: true,
					pixelOffset: new google.maps.Size(-140, -37),
					//closeBoxURL: '../../static/img/cancel-circle.png',
					closeBoxMargin: '8px',
					boxStyle: {
						background: '#ddd',
						backgroundSize: 'cover',
						fontSize: '13px',
						fontWeight: 300,
						fontFamily: '"Source Sans", sans-serif',
						color: '#666',
						borderRadius: '3px',
						border: '1px solid #999',
						opacity: 1,
						width: '280px',
						zIndex: 5000
					}
				};
				//Create info window
				var infoWindow = new InfoBox(infoWindowOptions);
				//Bring up infoWindow on CLICK
				google.maps.event.addListener(marker, 'click', function(){
					infoWindow.setContent(this.html);
					infoWindow.open(map, this);
					//$(restid[i]).css('background', 'red');
				});
				google.maps.event.addListener(map, 'click', function(){
					infoWindow.close();
				});
			};
		},
		'json'
	);   */
	
	/*========================================
	| Get Restaurant Data and display on map |
	========================================*/
			for (var i = 0; i < restArray.length; i++)
			{
				resp = restArray[i];
				console.log('RESP: ' + resp);
				//Getting x and y coords
				lat = resp['lat'];
				lng = resp['lng']

				//Setting content for info box
				var infoPic     = '<div style="height: 100px;"></div>'
				var infoHeading = '<div class="infoContainer"><h3>' + resp['name'] + '</h3>';
				var infoStars   = '<span class="' + getStars('small', 'red', resp['overall']) + '"></span>'
				var infoReview1 = '<h4>' + '"' + resp['recent_reviews1'] + '"' + '</h4>';
				var infoReview2 = '<h4>' + '"' + resp['recent_reviews2'] + '"' + '</h4></div>';

				var infoContent = infoPic + infoHeading + infoStars + infoReview1 + infoReview2;

				var marker = new google.maps.Marker(
					{
						position: new google.maps.LatLng(lat, lng),
						title:    resp['name'], // For when you hover over icon
						map:      map,
						icon: 	  {url: '../../static/img/pin-green-new.png' },
						html:     infoContent,
						id:       resp['id']
					}
				);
				//Push marker to markers array
				markers.push(marker);
				//Options for infoWindow
				var infoWindowOptions = {
					maxWidth: 0,
					alignBottom: true,
					pixelOffset: new google.maps.Size(-140, -37),
					//closeBoxURL: '../../static/img/cancel-circle.png',
					closeBoxMargin: '8px',
					boxStyle: {
						background: '#ddd',
						backgroundSize: 'cover',
						fontSize: '13px',
						fontWeight: 300,
						fontFamily: '"Source Sans", sans-serif',
						color: '#666',
						borderRadius: '3px',
						border: '1px solid #999',
						opacity: 1,
						width: '280px',
						zIndex: 5000
					}
				};
				//Create info window
				var infoWindow = new InfoBox(infoWindowOptions);
				//Bring up infoWindow on CLICK
				google.maps.event.addListener(marker, 'click', function(){
					infoWindow.setContent(this.html);
					infoWindow.open(map, this);
					//$(restid[i]).css('background', 'red');
				});
				google.maps.event.addListener(map, 'click', function(){
					infoWindow.close();
				});
			};
}; //Initialize

$(document).ready(function(){
	if(document.getElementById('search-map-canvas')) {
		initialize();
	};
});


/*===========================================
===== Places autocomplete on index page =====
===========================================*/

$(document).ready(function(){
	if (document.getElementById('location')){
		//Grab input
		var input = document.getElementById('location')
		//Bounds of map
		var southWest = new google.maps.LatLng(49.667628,-7.609406)
		var northEast = new google.maps.LatLng(59.333189,0.740204)
		var ukBounds  = new google.maps.LatLngBounds(southWest, northEast)

		var searchBox = new google.maps.places.SearchBox(input,
		{
			bounds: ukBounds,
			types: ['(cities)'],
			componentRestrictions: { country: 'gb' }
		})
	};
});

/*===========================================
===== Places autocomplete on search page =====
===========================================*/
$(document).ready(function(){
	if (document.getElementById('search-location')){
		//Grab input
		var input = document.getElementById('search-location')
		//Bounds of map
		var southWest = new google.maps.LatLng(49.667628,-7.609406)
		var northEast = new google.maps.LatLng(59.333189,0.740204)
		var ukBounds  = new google.maps.LatLngBounds(southWest, northEast)

		var searchBox = new google.maps.places.SearchBox(input,
		{
			bounds: ukBounds,
			types: ['(cities)'],
			componentRestrictions: { country: 'gb' }
		})
	};
});



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


/*
$(document).ready(function(){

	var csrftoken = getCookie('csrftoken');

	$.ajaxSetup({
	    beforeSend: function(jqXHR, settings) {
	        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
	            jqXHR.setRequestHeader("X-CSRFToken", csrftoken);
	        }
	    }
	});

	var location = 'Some coords';
	$.post(
		'',
		{'location': location, 'csrfmiddlewaretoken': csrftoken},
		function() {console.log('It worked...' + location)}, // Success function
		'text'
	)
})
*/