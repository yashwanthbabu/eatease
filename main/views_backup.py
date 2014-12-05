from django.template import RequestContext
from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from main.models import Restaurant, Review, ReviewDietary, RestaurantMenus
from django.db.models import Count, Avg
from django.core import serializers
import json
from types import *

import math, datetime

#################
#   FUNCTIONS   #
#################

# Stars function to return star class
def getStars(size, colour, value):
	if str(value) == '0.5':
		return 'star' + '-' + size + '-' + colour + '-' + 'half' 
	if str(value) == '1.0':
		return 'star' + '-' + size + '-' + colour + '-' + '1' 
	if str(value) == '1.5':
		return 'star' + '-' + size + '-' + colour + '-' + '1half'
	if str(value) == '2.0':
		return 'star' + '-' + size + '-' + colour + '-' + '2' 
	if str(value) == '2.5':
		return 'star' + '-' + size + '-' + colour + '-' + '2half'
	if str(value) == '3.0':
		return 'star' + '-' + size + '-' + colour + '-' + '3' 
	if str(value) == '3.5':
		return 'star' + '-' + size + '-' + colour + '-' + '3half' 
	if str(value) == '4.0':
		return 'star' + '-' + size + '-' + colour + '-' + '4' 
	if str(value) == '4.5':
		return 'star' + '-' + size + '-' + colour + '-' + '4half'
	if str(value) == '5.0':
		return 'star' + '-' + size + '-' + colour + '-' + '5'

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



#############
#   INDEX   #
#############
def index(request):
	context = RequestContext(request)

	recent_reviews_1 = Review.objects.order_by('-date_added')[:3]
	recent_reviews_2 = Review.objects.order_by('-date_added')[3:6]

	for rev in recent_reviews_1:
			rev.date_added = rev.date_added.date()
			rev.star_class = getStars('big', 'red', rev.overall_rating)

	for rev in recent_reviews_2:
			rev.date_added = rev.date_added.date()

	return render_to_response(
		'main/index.html', 
		{
			'recent_reviews_1': recent_reviews_1,
			'recent_reviews_2': recent_reviews_2,
		}, 
		context,
	)

##############
#   SEARCH   #
##############
def search(request, place_url=''):
	context = RequestContext(request)

	place_str = URLToString(place_url)
	restaurants = Restaurant.objects.all()
	reviews = Review.objects.all()

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

		if sr: # If there is a GET variable
			for item in sr_list:
				if item.keys()[0] == sr:
					item[sr]['selected'] = 'selected'


		# Take GET variable from URL and check corresponding radio button
		def checkRadio(_list, getVar):
			for i in range (1,6):
				_list.append({ 'rating': i, 'checked': '' })

			getRating = request.GET.get(getVar)
			if getRating:
				index = int(getRating) - 1
				_list[index]['checked'] = 'checked'

		checkRadio(overall_list, 'o')
		checkRadio(nuts_list, 'n')
		checkRadio(gluten_list, 'g')
		checkRadio(veg_list, 'v')
		checkRadio(vegan_list, 've')
		checkRadio(dairy_list, 'd')

	for rest in restaurants:
		rest.reviews            = reviews.filter(restaurant=rest)
		rest.recent_reviews     = reviews.filter(restaurant=rest).order_by('date_added')[:2]
		rest.num_reviews        = len(rest.reviews)
		rest.avg_overall        = rest.reviews.aggregate(Avg('overall_rating'))
		rest.avg_overall        = rest.avg_overall['overall_rating__avg']
		rest.avg_overall        = 0.5 * math.ceil(2.0 * rest.avg_overall)
		rest.overall_star_class = getStars('big', 'red', rest.avg_overall)

		for rev in rest.recent_reviews:
			rev.date_added = rev.date_added.date()
			rev.author = rev.user


	return render_to_response(
		'main/search.html',
		{
			'restaurants': restaurants,
			'reviews': reviews,
			'place_str': place_str,
			'sr_list': sr_list,
			'overall_list': overall_list,
			'nuts_list': nuts_list,
			'gluten_list': gluten_list,
			'veg_list': veg_list,
			'vegan_list': vegan_list,
			'dairy_list': dairy_list,
		},
		context,
	)


##############################
#   SEARCH GET RESTAURANTS   #
##############################
def search_list(request):


	context = RequestContext(request)

	"""
	sr = ''
	o  = ''
	n  = ''
	g  = ''
	v  = ''
	ve = ''
	d  = ''
 	
	if request.method == 'GET':
		sr = request.GET['sr']
		o = request.GET['o']
		n = request.GET['n']
		g = request.GET['g']
		v = request.GET['v']
		ve = request.GET['ve']
		d = request.GET['d']
	"""

	# TODO: Take filters and query db to get only the entries which match the search terms
	# Currently displays ALL restaurants

	
	restaurants = Restaurant.objects.values()

	reviews = Review.objects.values()

	for rest in restaurants:
		recent_reviews = reviews.filter(restaurant_id=rest['id']).order_by('date_added')[:2]

		rest.update({'recent_reviews1': recent_reviews[0]['title']})
		rest.update({'recent_reviews2': recent_reviews[1]['title']})

		rest_reviews = reviews.filter(restaurant=rest['id'])

		rest.update({'num_reviews': len(rest_reviews) })

		avg_overall        = rest_reviews.aggregate(Avg('overall_rating'))
		avg_overall        = avg_overall['overall_rating__avg']
		avg_overall        = 0.5 * math.ceil(2.0 * avg_overall)
		overall_star_class = getStars('small', 'red', avg_overall)

		rest.update({'overall_star_class': overall_star_class })


	restaurants_dict = [rest for rest in restaurants]

	restaurants_list = json.dumps(restaurants_dict)

	return HttpResponse(restaurants_list)
	
	


#######################
#   RESTAURANT PAGE   #
#######################
def restaurant(request, rest_url):
	context = RequestContext(request)

	rest_name = URLToString(rest_url)
	rest_details = Restaurant.objects.filter(name=rest_name)


	return render_to_response(
		'main/restaurant.html',
		{
			'rest_name': rest_name,
			'rest_details': rest_details,
		},
		context,
	)




####################
#   FIILTER TEST   #
####################
def filter_test(request):
	context = RequestContext(request)

	getVars = { 'sr': '', 'o': '', 'n': '', 'g': '', 'v': '', 've': '', 'd': '' }

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

	# NOTE : Need to filter Restaurant.objects by search radius
	restaurants = Restaurant.objects.all().extra(select={
										'avg_overall':
											'SELECT ROUND(2 * AVG(overall_rating), 0) / 2 FROM main_review \
											WHERE main_review.restaurant_id = main_restaurant.id',
										'avg_nuts': 
											'SELECT ROUND(2 * AVG(nuts_rating), 0) / 2 FROM main_review \
											WHERE main_review.restaurant_id = main_restaurant.id',
										'avg_gluten':
											'SELECT ROUND(2 * AVG(gluten_rating), 0) / 2 FROM main_review \
											WHERE main_review.restaurant_id = main_restaurant.id',
										'avg_veg':
											'SELECT ROUND(2 * AVG(vegetarian_rating), 0) / 2 FROM main_review \
											WHERE main_review.restaurant_id = main_restaurant.id',
										'avg_vegan':
											'SELECT ROUND(2 * AVG(vegan_rating), 0) / 2 FROM main_review \
											WHERE main_review.restaurant_id = main_restaurant.id',
										'avg_dairy':
											'SELECT ROUND(2 * AVG(dairy_rating), 0) / 2 FROM main_review \
											WHERE main_review.restaurant_id = main_restaurant.id',
										}).order_by('-avg_overall', '-avg_gluten')

	restaurants = list(restaurants)

	restaurants = [rest for rest in restaurants if (satisfiesFilter(rest.avg_overall, getVars['o']) 
													and satisfiesFilter(rest.avg_nuts, getVars['n'])
													and satisfiesFilter(rest.avg_gluten, getVars['g'])
													and satisfiesFilter(rest.avg_veg, getVars['v'])
													and satisfiesFilter(rest.avg_vegan, getVars['ve'])
													and satisfiesFilter(rest.avg_dairy, getVars['d'])
												)
											]

	
	revs = Review.objects.all()

	return render_to_response(
		'main/filter_test.html',
		{
			'getVars': getVars,
			'rest': restaurants,
			'reviews': revs,
		},
		context,
	)
	