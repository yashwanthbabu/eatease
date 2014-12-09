from django.template import RequestContext
from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from main.models import Restaurant, Review, ReviewDietary, RestaurantMenus
from .forms import UserForm
from django.db.models import Count, Avg
from django.core import serializers
from types import *

import json, math, datetime

#################
#   FUNCTIONS   #
#################

# Stars function to return star class
def getStars(size, colour, value):
	if str(value) == '0.5':
		return 'star' + '-' + size + '-' + colour + '-' + 'half' 
	if str(value) in ['1.0', '1']:
		return 'star' + '-' + size + '-' + colour + '-' + '1' 
	if str(value) == '1.5':
		return 'star' + '-' + size + '-' + colour + '-' + '1half'
	if str(value) in ['2.0', '2']:
		return 'star' + '-' + size + '-' + colour + '-' + '2' 
	if str(value) == '2.5':
		return 'star' + '-' + size + '-' + colour + '-' + '2half'
	if str(value) in ['3.0', '3']:
		return 'star' + '-' + size + '-' + colour + '-' + '3' 
	if str(value) == '3.5':
		return 'star' + '-' + size + '-' + colour + '-' + '3half' 
	if str(value) in ['4.0', '4']:
		return 'star' + '-' + size + '-' + colour + '-' + '4' 
	if str(value) == '4.5':
		return 'star' + '-' + size + '-' + colour + '-' + '4half'
	if str(value) in ['5.0', '5']:
		return 'star' + '-' + size + '-' + colour + '-' + '5'
	if value is None:
		return 'noRatings'

# String to URL and URL to string
def stringToURL(str):
	str = str.replace(' ', '_')
	str = str.replace(',', '_')
	return str

def URLToString(str):
	str = str.replace('__', ', ')
	str = str.replace('_', ' ')
	return str

# Filter search results by rating. Returns True if Result >= Filter Rating, else returns False
def satisfiesFilter(rating, filter):
	if filter == 0: # Case where user not filtering by this requirement
		return True
	elif rating >= filter:
		return True
	else:
		return False

# Filter by search radius, note pi/180 ~= 0.01745, 180/pi ~= 57.2958 and 3959 is radius of earth in miles
def latLowerBound(origin_lat, distance):
	return origin_lat - (distance / 3959) * 57.2958
def latUpperBound(origin_lat, distance):
	return origin_lat + (distance / 3959) * 57.2958
def lngLowerBound(origin_lng, origin_lat,  distance):
	r = 3959 * math.cos(origin_lat * 0.01745) # radius of circle at origin_lat
	return origin_lng - (distance / r) * 57.2958
def lngLowerBound(origin_lng, origin_lat,  distance):
	r = 3959 * math.cos(origin_lat * 0.01745) # radius of circle at origin_lat
	return origin_lng + (distance / r) * 57.2958



##################### 
# USER REGISTRATION # NOTE: Not quite working. Need to fix
#####################
def register(request):

	# Was registration successful? Set to False initially
	registered = False

	# Process Form data
	if request.method == 'POST':
		# Get User Form data
		user_form = UserForm(data=request.POST)

		# If form is valid, save
		if user_form.is_valid():
			user = user_form.save()
			user.set_password(user.password)
			user.save()
		# If form not valid, print errors
		else:
			print (user_form.errors)

	# If no POST data, just render User Form ready for input
	else:
		user_form = UserForm()

	return render(
		request,
		'main/signup.html',
		{
			'user_form': user_form,
			'registered': registered,
		},
	)

#############
#   INDEX   #
#############
def index(request):

	recent_reviews_1 = Review.objects.order_by('-date_added')[:3]
	recent_reviews_2 = Review.objects.order_by('-date_added')[3:6]

	for rev in recent_reviews_1:
			rev.date_added = rev.date_added.date()
			rev.star_class = getStars('big', 'red', rev.overall_rating)

	for rev in recent_reviews_2:
			rev.date_added = rev.date_added.date()

	return render(
		request,
		'main/index.html', 
		{
			'recent_reviews_1': recent_reviews_1,
			'recent_reviews_2': recent_reviews_2,
		}, 
	)

##############
#   SEARCH   #
##############
def search(request, place_url=''):

	place_str = URLToString(place_url)

	sr_list = [
		{'1': {'text': '1 mile', 'selected': ''} },
		{'3': {'text': '3 miles', 'selected': ''} },
		{'5': {'text': '5 miles', 'selected': ''} },
		{'6': {'text': '+ 5 miles', 'selected': ''} },
	]	
	overall_list = []
	nuts_list = []
	gluten_list = []
	veg_list = []
	vegan_list = []
	dairy_list = []

	# If GET variables are defined in URL
	if request.method == 'GET':
		# Get Search Radius form URL and modify select with value
		sr = request.GET.get('sr')

		if sr: # If there is a GET variable, select corresponding option
			for item in sr_list:
				if item.keys()[0] == sr:
					item[sr]['selected'] = 'selected'


		# Take GET variable from URL and check corresponding radio button
		def checkRadio(_list, getVar):
			for i in range (1,6):
				_list.append({ 'rating': i, 'checked': '' })

			getRating = request.GET.get(getVar)
			if  getRating :
				index = int(getRating) - 1
				_list[index]['checked'] = 'checked'

		checkRadio(overall_list, 'o')
		checkRadio(nuts_list, 'n')
		checkRadio(gluten_list, 'g')
		checkRadio(veg_list, 'v')
		checkRadio(vegan_list, 've')
		checkRadio(dairy_list, 'd')

	# =============== #
	# Perform queries #
	# =============== #
	getVars = { 'sr': '', 'o': '', 'n': '', 'g': '', 'v': '', 've': '', 'd': '' }

	# Assigning GET vars to dictionary
	if request.method == 'GET':
		for var in getVars:
			getVar = request.GET.get(var)
			try:
				getVar = int(getVar)
			except ValueError:
				getVar = 0
			except TypeError:
				getVar = 0
			if 0 <= getVar < 6:
				getVars[var] = getVar
			else:
				getVars[var] = 0

	# Create dict for additional SQL Query
	# Only perform query for selected ratings
	# Setting default values to 0 allows us to use 'satisfiesFilter' function later
	searchQuery = {
		'num_reviews': 'SELECT COUNT(*) FROM main_review WHERE main_review.restaurant_id = main_restaurant.id',
		'recent_review_1': 'SELECT title FROM main_review WHERE main_review.restaurant_id = main_restaurant.id ORDER BY date_added DESC LIMIT 1',
		'date_added_1': 'SELECT date_added FROM main_review WHERE main_review.restaurant_id = main_restaurant.id ORDER BY date_added DESC LIMIT 1',
		'recent_review_2': 'SELECT title FROM main_review WHERE main_review.restaurant_id = main_restaurant.id ORDER BY date_added DESC LIMIT 1 OFFSET 1',
		'date_added_2': 'SELECT date_added FROM main_review WHERE main_review.restaurant_id = main_restaurant.id ORDER BY date_added DESC LIMIT 1 OFFSET 1',		
		'avg_overall': 'SELECT ROUND(2 * AVG(overall_rating), 0) / 2 FROM main_review WHERE main_review.restaurant_id = main_restaurant.id',
		'avg_nuts': 0,
		'avg_gluten': 0,
		'avg_veg': 0,
		'avg_vegan': 0,
		'avg_dairy': 0,
	}

	# If no variables have been checked then just return all ratings
	# Otherwise return just checked ratings
	noneChecked = getVars['g'] == 0 and getVars['n'] == 0 and getVars['v'] == 0 and getVars['ve'] == 0 and getVars['d'] == 0

	if noneChecked:
		searchQuery['avg_nuts'] = 'SELECT ROUND(2 * AVG(nuts_rating), 0) / 2 FROM main_review WHERE main_review.restaurant_id = main_restaurant.id'
		searchQuery['avg_gluten'] = 'SELECT ROUND(2 * AVG(gluten_rating), 0) / 2 FROM main_review WHERE main_review.restaurant_id = main_restaurant.id'
		searchQuery['avg_veg'] = 'SELECT ROUND(2 * AVG(vegetarian_rating), 0) / 2 FROM main_review WHERE main_review.restaurant_id = main_restaurant.id'
		searchQuery['avg_vegan'] = 'SELECT ROUND(2 * AVG(vegan_rating), 0) / 2 FROM main_review WHERE main_review.restaurant_id = main_restaurant.id'
		searchQuery['avg_dairy'] = 'SELECT ROUND(2 * AVG(dairy_rating), 0) / 2 FROM main_review WHERE main_review.restaurant_id = main_restaurant.id'
	else:
		if 0 < getVars['n'] < 6:
			searchQuery['avg_nuts'] = 'SELECT ROUND(2 * AVG(nuts_rating), 0) / 2 FROM main_review WHERE main_review.restaurant_id = main_restaurant.id'
		if 0 < getVars['g'] < 6:
			searchQuery['avg_gluten'] = 'SELECT ROUND(2 * AVG(gluten_rating), 0) / 2 FROM main_review WHERE main_review.restaurant_id = main_restaurant.id'
		if 0 < getVars['v'] < 6:
			searchQuery['avg_veg'] = 'SELECT ROUND(2 * AVG(vegetarian_rating), 0) / 2 FROM main_review WHERE main_review.restaurant_id = main_restaurant.id'
		if 0 < getVars['ve'] < 6:
			searchQuery['avg_vegan'] = 'SELECT ROUND(2 * AVG(vegan_rating), 0) / 2 FROM main_review WHERE main_review.restaurant_id = main_restaurant.id'
		if 0 < getVars['d'] < 6:
			searchQuery['avg_dairy'] = 'SELECT ROUND(2 * AVG(dairy_rating), 0) / 2 FROM main_review WHERE main_review.restaurant_id = main_restaurant.id'

	# NOTE : Need to filter Restaurant.objects by search radius!
	restaurants = Restaurant.objects.all().extra(select=searchQuery).extra(order_by=['-avg_overall'])
	restaurants = list(restaurants)
	# Only display restaurants which satisfy the search requirements
	restaurants = [rest for rest in restaurants if ( satisfiesFilter(rest.avg_overall, getVars['o'])
													and satisfiesFilter(rest.avg_nuts, getVars['n'])
													and satisfiesFilter(rest.avg_gluten, getVars['g'])
													and satisfiesFilter(rest.avg_veg, getVars['v'])
													and satisfiesFilter(rest.avg_vegan, getVars['ve'])
													and satisfiesFilter(rest.avg_dairy, getVars['d'])
												)
											]

	# Adding star css classes
	# If requirement is not being queried then the class returned will be None and nothing will display in template
	for rest in restaurants:
		rest.overall_star_class = getStars('big', 'red', rest.avg_overall)
		rest.all_stars = [
			{'name': 'Nuts',   		'star_class': getStars('small', 'green', rest.avg_nuts) }, 
			{'name': 'Gluten',   	'star_class': getStars('small', 'green', rest.avg_gluten) }, 
			{'name': 'Vegetarian',  'star_class': getStars('small', 'green', rest.avg_veg) }, 
			{'name': 'Vegan',   	'star_class': getStars('small', 'green', rest.avg_vegan) }, 
			{'name': 'Dairy',  		'star_class': getStars('small', 'green', rest.avg_dairy) }, 
		]

	return render(
		request,
		'main/search.html',
		{
			'place_str': place_str,
			'sr_list': sr_list,
			'overall_list': overall_list,
			'nuts_list': nuts_list,
			'gluten_list': gluten_list,
			'veg_list': veg_list,
			'vegan_list': vegan_list,
			'dairy_list': dairy_list,
			'restaurants': restaurants,
		},
	)


#######################
#   RESTAURANT PAGE   #
#######################
def restaurant(request, rest_url=''):

	rest_id = rest_url
	

	# Getting number of reviews and average ratings.
	searchQuery = {
		'num_reviews': 'SELECT COUNT(*) FROM main_review WHERE main_review.restaurant_id = ' + rest_id,
		'avg_overall': 'SELECT ROUND(2 * AVG(overall_rating), 0) / 2 FROM main_review WHERE main_review.restaurant_id = ' + rest_id,
		'avg_nuts': 'SELECT ROUND(2 * AVG(nuts_rating), 0) / 2 FROM main_review WHERE main_review.restaurant_id = ' + rest_id,
		'avg_gluten': 'SELECT ROUND(2 * AVG(gluten_rating), 0) / 2 FROM main_review WHERE main_review.restaurant_id = ' + rest_id,
		'avg_veg': 'SELECT ROUND(2 * AVG(vegetarian_rating), 0) / 2 FROM main_review WHERE main_review.restaurant_id = ' + rest_id,
		'avg_vegan': 'SELECT ROUND(2 * AVG(vegan_rating), 0) / 2 FROM main_review WHERE main_review.restaurant_id = ' + rest_id,
		'avg_dairy': 'SELECT ROUND(2 * AVG(dairy_rating), 0) / 2 FROM main_review WHERE main_review.restaurant_id = ' + rest_id,
	}
	# Perform the query
	rest_details = Restaurant.objects.filter(pk=rest_id).extra(select=searchQuery)
	rest_details = rest_details[0]

	# Add star css classes
	rest_details.overall_star_class = getStars('big', 'red', rest_details.avg_overall)
	rest_details.all_stars = [
		{ 'name': 'Nuts', 		'star_class': getStars('big', 'green', rest_details.avg_nuts) },
		{ 'name': 'Gluten', 	'star_class': getStars('big', 'green', rest_details.avg_gluten) },
		{ 'name': 'Vegetarian', 'star_class': getStars('big', 'green', rest_details.avg_veg) },
		{ 'name': 'Vegan', 		'star_class': getStars('big', 'green', rest_details.avg_vegan) },
		{ 'name': 'Dairy', 		'star_class': getStars('big', 'green', rest_details.avg_dairy) },
	]

	# Getting all reviews 
	rest_reviews = Review.objects.filter(restaurant_id=rest_id)

	for rev in rest_reviews:
		rev.overall_star_class = getStars('small', 'red', rev.overall_rating)
		rev.all_stars = [
			{ 'name': 'Overall',	'star_class': getStars('small', 'red', rev.overall_rating) },
			{ 'name': 'Nuts',		'star_class': getStars('small', 'green', rev.nuts_rating) },
			{ 'name': 'Gluten',		'star_class': getStars('small', 'green', rev.gluten_rating) },
			{ 'name': 'Vegetarian',	'star_class': getStars('small', 'green', rev.vegetarian_rating) },
			{ 'name': 'Vegan',		'star_class': getStars('small', 'green', rev.vegan_rating) },
			{ 'name': 'Dairy',		'star_class': getStars('small', 'green', rev.dairy_rating) },
		]
		rev.all_stars = [x for x in rev.all_stars if x['star_class'] not in ['noRatings', None] ]

	return render_to_response(
		request,
		'main/restaurant.html',
		{
			'rest': rest_details,
			'reviews': rest_reviews,
		},
	)
