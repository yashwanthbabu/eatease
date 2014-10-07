var markers = [];
var MY_MAPTYPE_ID = 'custom_style';
var map;
var restid = [];
var geocoder;
var mapCenter;

function initialize() {

	geocoder = new google.maps.Geocoder();

	var pathname = $(location).attr('pathname');
	var place = pathname.substr(pathname.lastIndexOf('/') + 1);
	place = URLToString(place);
	console.log(place)
	geocoder.geocode({
		'address': place
	}, function(results, status){
		console.log('Has it geocoded? ' + google.maps.GeocoderStatus.OK)
		if (status == google.maps.GeocoderStatus.OK)
		{
			console.log('Yay it worked!')
			map.setCenter(results[0].geometry.location)
			console.log('#####' + mapCenter)
		} 
		else {
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
	$.get(
		'/core/search_list/',
		function(response) {

			/*==========================
 			| Adding all places to map |
			==========================*/
			for (var i = 0; i < response.length; i++)
			{
				//Getting x and y coords
				coords = response[i]['coords'];
				coords = coords.split(',');

				//Setting content for info box
				var infoPic     = '<div style="height: 100px;"></div>'
				var infoHeading = '<div class="infoContainer"><h3>' + response[i]['name'] + '</h3>';
				var infoStars   = '<span class="' + response[i]['overall_star_class'] + '"></span>'
				var infoReview1 = '<h4>' + '"' + response[i]['recent_reviews1'] + '"' + '</h4>';
				var infoReview2 = '<h4>' + '"' + response[i]['recent_reviews2'] + '"' + '</h4></div>';

				var infoContent = infoPic + infoHeading + infoStars +infoReview1 +infoReview2

				var marker = new google.maps.Marker(
					{
						position: new google.maps.LatLng(coords[0], coords[1]),
						title:    response[i]['name'], // For when you hover over icon
						map:      map,
						icon: 	  {url: '../../static/img/pin-green-new.png' },
						html:     infoContent,
						id:       response[i]['id']
					}
				);
				//Push marker to markers array
				markers.push(marker);
				//Options for infoWindow
				var infoWindowOptions = {
					maxWidth: 0,
					alignBottom: true,
					pixelOffset: new google.maps.Size(-140, -37),
					closeBoxURL: '../../static/img/cancel-circl.png',
					closeBoxMargin: '8px',
					boxStyle: {
						background: 'url(http://lorempixel.com/400/400/food)',
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
					//console.log(this.id);
				});

				google.maps.event.addListener(map, 'click', function(){
					infoWindow.close();
				});
			};
		},
		'json'
	);

}; //Initialize


google.maps.event.addDomListener(window, 'load', initialize);



/*===========================================
===== Places autocomplete on index page =====
===========================================*/
$(document).ready(function(){
	//Grab input
	var input = document.getElementById('index-text')
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
});



/*
@dark-blue: lighten(#172C3C, 2%);
@mid-blue:  lighten(#274862, 2%);
@red:       saturate(lighten(#995052, 10%), 10%);
@orange:    lighten(#D96831, 2%);
@yellow:    lighten(#E6B33D, 2%);
*/

