from django.db import models
from django.contrib.auth.models import User


##################
#  USER PROFILE  #
##################
class UserProfile(models.Model):
	user = models.OneToOneField(User)

	picture = models.ImageField(upload_to='profile_images', blank=True)

	# What the user's dietary requirements?
	nuts = models.BooleanField(default=False)
	gluten = models.BooleanField(default=False)
	vegetarian = models.BooleanField(default=False)
	vegan = models.BooleanField(default=False)
	dairy = models.BooleanField(default=False)

	def __str__(self):
		return self.user.username



################
#  RESTAURANT  #
################
class Restaurant(models.Model):
	name         = models.CharField(max_length=64, unique=True)
	address      = models.CharField(max_length=128)
	postcode     = models.CharField(max_length=10)
	phone_number = models.CharField(max_length=14)
	lat			 = models.DecimalField(max_digits=13, decimal_places=10, default=0)
	lng 		 = models.DecimalField(max_digits=13, decimal_places=10, default=0)
	url          = models.URLField()

	def __str__(self):
		return self.name



##################### Show which allergens are marked on menu / if they have a separate allergy menu
#  RESTAURANT-MENU  # Haven't implemented this yet
#####################
class RestaurantMenus(models.Model):
	restaurant = models.OneToOneField(Restaurant)

	nuts_marked 		= models.BooleanField(default=False)
	nuts_sep    		= models.BooleanField(default=False)
	gluten_marked 		= models.BooleanField(default=False)
	gluten_sep    		= models.BooleanField(default=False)
	vegetarian_marked	= models.BooleanField(default=False)
	vegetarian_sep    	= models.BooleanField(default=False)
	vegan_marked 		= models.BooleanField(default=False)
	vegan_sep    		= models.BooleanField(default=False)
	dairy_marked 		= models.BooleanField(default=False)
	dairy_sep    		= models.BooleanField(default=False)

	general_sep = models.BooleanField(default=False) # If there is a separate menu with any/all dietary choices



################
#    REVIEW    #
################
class Review(models.Model):
	restaurant     = models.ForeignKey(Restaurant)
	user           = models.ForeignKey(User)
	title          = models.CharField(max_length=256)
	date_added     = models.DateTimeField(auto_now_add=True)
	overall_text   = models.TextField(max_length=2056)

	overall_rating     = models.PositiveSmallIntegerField()
	nuts_rating        = models.PositiveSmallIntegerField(null=True,blank=True)
	gluten_rating      = models.PositiveSmallIntegerField(null=True,blank=True)
	vegetarian_rating  = models.PositiveSmallIntegerField(null=True,blank=True)
	vegan_rating       = models.PositiveSmallIntegerField(null=True,blank=True)
	dairy_rating       = models.PositiveSmallIntegerField(null=True,blank=True)

	def __str__(self):
		return self.title



#######################
#    REVIEW-DIETARY   # THIS IS NOW NO LONGER USED
#######################
class ReviewDietary(models.Model):
	review = models.OneToOneField(Review)

	nuts_rating        = models.PositiveSmallIntegerField(null=True,blank=True)
	gluten_rating      = models.PositiveSmallIntegerField(null=True,blank=True)
	vegetarian_rating  = models.PositiveSmallIntegerField(null=True,blank=True)
	vegan_rating       = models.PositiveSmallIntegerField(null=True,blank=True)
	dairy_rating       = models.PositiveSmallIntegerField(null=True,blank=True)

	def __str__(self):
		return self.review.title