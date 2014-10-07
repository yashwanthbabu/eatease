$(document).ready(function(){
	$('#overall-filter').rating('smallRed');
	$('#nuts-filter').rating('smallGreen');
	$('#gluten-filter').rating('smallGreen');
	$('#dairy-filter').rating('smallGreen');
	$('#vegetarian-filter').rating('smallGreen');
	$('#vegan-filter').rating('smallGreen');
});


$.fn.rating = function(starType) {
	var container = $(this);
	var labels = $(container).children('label');
	var radios = $(container).children('input');

	if(starType == 'smallGreen')
	{
		var BG = [
			'-96px -169px',
			'-77px -169px',
			'-58px -169px',
			'-39px -169px',
			'-20px -169px',
			'-1px -169px'
		];		
	};
	if(starType == 'smallRed')
	{
		var BG = [
			'-96px -123px',
			'-77px -123px',
			'-58px -123px',
			'-39px -123px',
			'-20px -123px',
			'-1px -123px'
		];		
	};

	$(container).hover(
	function(){
		//  Setting stars on hover
		$(labels).hover(function(){
			var val = $(this).attr('for');
			val = val.substr(val.length - 1);

			$(this).parent().css('background-position', BG[val]);
		});
	}, //  When mouse leaves stars
	function(){
		// Setting stars to remain if box has been checked
		var rating = $(this).children('input[type=radio]:checked').val();

		if (rating == undefined){
			$(this).css('background-position', BG[0]);
		}
		else{
			$(this).css('background-position', BG[rating]);
		};
	});
};

/*
var bigRedBg1 = '-89px -27px'
var bigRedBg2 = '-67px -27px'
var bigRedBg3 = '-45px -27px'
var bigRedBg4 = '-23px -27px'
var bigRedBg5 = '-1px -27px'

var bigGreenBg1 = '-89px -75px'
var bigGreenBg2 = '-67px -75px'
var bigGreenBg3 = '-45px -75px'
var bigGreenBg4 = '-23px -75px'
var bigGreenBg5 = '-1px -75px'

var smallRedBg1 = '-77px -123px'
var smallRedBg2 = '-58px -123px'
var smallRedBg3 = '-39px -123px'
var smallRedBg4 = '-20px -123px'
var smallRedBg5 = '-1px -123px'
*/