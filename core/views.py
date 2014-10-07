from django.template import RequestContext
from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from core.models import Restaurant, Review, ReviewDietary, RestaurantMenus
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



#############
#   INDEX   #
#############
def index(request):
	context = RequestContext(request)

	recent_reviews = Review.objects.order_by('-date_added')[:3]

	for rev in recent_reviews:
			rev.date_added = rev.date_added.date()

	return render_to_response(
		'core/index.html', 
		{
			'recent_reviews': recent_reviews,
		}, 
		context,
	)

##############
#   SEARCH   #
##############
def search(request, place_url):
	context = RequestContext(request)

	place_str = URLToString(place_url)
	restaurants = Restaurant.objects.all()
	reviews = Review.objects.all()

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


	return render_to_response(
		'core/search.html',
		{
			'restaurants': restaurants,
			'reviews': reviews,
			'place_str': place_str,
		},
		context,
	)

##############################
#   SEARCH GET RESTAURANTS   #
##############################
def search_list(request):

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
