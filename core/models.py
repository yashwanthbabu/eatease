from django.db import models
from django.contrib.auth.models import User


################
#  RESTAURANT  #
################
class Restaurant(models.Model):
	name         = models.CharField(max_length=64, unique=True)
	address      = models.CharField(max_length=128)
	postcode     = models.CharField(max_length=10)
	phone_number = models.CharField(max_length=14)
	coords       = models.CharField(max_length=24)
	url          = models.URLField()

	def __str__(self):
		return self.name

	



#####################
#  RESTAURANT-MENU  #
#####################
class RestaurantMenus(models.Model):
	restaurant = models.OneToOneField(Restaurant)

	nuts_marked 		= models.BooleanField()
	nuts_sep    		= models.BooleanField()
	gluten_marked 		= models.BooleanField()
	gluten_sep    		= models.BooleanField()
	vegetarian_marked	= models.BooleanField()
	vegetarian_sep    	= models.BooleanField()
	vegan_marked 		= models.BooleanField()
	vegan_sep    		= models.BooleanField()
	dairy_marked 		= models.BooleanField()
	dairy_sep    		= models.BooleanField()

	general_sep = models.BooleanField() #If there is a separate menu with any/all dietary choices



################
#    REVIEW    #
################
class Review(models.Model):
	restaurant     = models.ForeignKey(Restaurant)
	user           = models.ForeignKey(User)
	title          = models.CharField(max_length=256)
	date_added     = models.DateTimeField(auto_now_add=True)
	overall_text   = models.TextField(max_length=2056)
	overall_rating = models.PositiveSmallIntegerField()

	def __str__(self):
		return self.title



#######################
#    REVIEW-DIETARY   #
#######################
class ReviewDietary(models.Model):
	review = models.OneToOneField(Review)

	nuts_rating        = models.PositiveSmallIntegerField(default=0)
	gluten_rating      = models.PositiveSmallIntegerField(default=0)
	vegetarian_rating  = models.PositiveSmallIntegerField(default=0)
	vegan_rating       = models.PositiveSmallIntegerField(default=0)
	dairy_rating       = models.PositiveSmallIntegerField(default=0)

	def __str__(self):
		return self.review.title