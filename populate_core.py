import os
import random

def populate():

	# TONINA's DELI
	tonina = add_restaurant(
		name='Tonina\'s Deli', 
		address='123 Lorem Ipsum Street', 
		postcode='BS2 9HA', 
		phone_number='123456789', 
		url='#'
	)

	r1 = add_review(
		restaurant=tonina, 
		user='mark', 
		title='Lorem ipsum dolor sit amet!', 
		overall_text='Lorem ipsum dolor sit amet, augue deseruisse appellantur te eam, eu omnium offendit pro. Cu iudico vidisse definitiones pri, ne enim duis iisque mei, id mundi pericula partiendo per. Duo at alterum disputando conclusionemque, cu facete torquatos vis, est decore scripserit ut. Corrumpit incorrupte id his, ius ut lorem inani tritani. Vero vocibus usu in, in neglegentur delicatissimi mei.', 
		overall_rating=random.randint(1,5)
	)

	r1_dietary = add_review_dietary(
		review=r1, 
		nuts_rating=random.randint(1,5), 
		gluten_rating=random.randint(1,5), 
		vegetarian_rating=random.randint(1,5), 
		vegan_rating=random.randint(1,5), 
		dairy_rating=random.randint(1,5)
	)

	r2 = add_review(
		restaurant=tonina, 
		user='mark', 
		title='Lorem ipsum dolor sit amet!', 
		overall_text='Lorem ipsum dolor sit amet, augue deseruisse appellantur te eam, eu omnium offendit pro. Cu iudico vidisse definitiones pri, ne enim duis iisque mei, id mundi pericula partiendo per. Duo at alterum disputando conclusionemque, cu facete torquatos vis, est decore scripserit ut. Corrumpit incorrupte id his, ius ut lorem inani tritani. Vero vocibus usu in, in neglegentur delicatissimi mei.', 
		overall_rating=random.randint(1,5)
	)

	r2_dietary = add_review_dietary(
		review=r2, 
		nuts_rating=random.randint(1,5), 
		gluten_rating=random.randint(1,5), 
		vegetarian_rating=random.randint(1,5), 
		vegan_rating=random.randint(1,5), 
		dairy_rating=random.randint(1,5)
	)

	r3 = add_review(
		restaurant=tonina, 
		user='mark', 
		title='Lorem ipsum dolor sit amet!', 
		overall_text='Lorem ipsum dolor sit amet, augue deseruisse appellantur te eam, eu omnium offendit pro. Cu iudico vidisse definitiones pri, ne enim duis iisque mei, id mundi pericula partiendo per. Duo at alterum disputando conclusionemque, cu facete torquatos vis, est decore scripserit ut. Corrumpit incorrupte id his, ius ut lorem inani tritani. Vero vocibus usu in, in neglegentur delicatissimi mei.', 
		overall_rating=random.randint(1,5)
	)

	r3_dietary = add_review_dietary(
		review=r3, 
		nuts_rating=random.randint(1,5), 
		gluten_rating=random.randint(1,5), 
		vegetarian_rating=random.randint(1,5), 
		vegan_rating=random.randint(1,5), 
		dairy_rating=random.randint(1,5)
	)

	ton_menu = add_menus(
		restaurant=tonina, 
		nuts_marked=True, 
		nuts_sep=False, 
		gluten_marked=True, 
		gluten_sep=False, 
		vegetarian_marked=False, 
		vegetarian_sep=True, 
		vegan_marked=False, 
		vegan_sep=True, 
		dairy_marked=True, 
		dairy_sep=True, 
		general_sep=False
	)

	# MARCO's

	marco = add_restaurant(
		name='Marco\'s', 
		address='456 Lorem Ipsum Street', 
		postcode='BS8 1TL', 
		phone_number='456789123', 
		url='#'
	)

	mr1 = add_review(
		restaurant=marco, 
		user='mark', 
		title='Lorem ipsum dolor sit amet!', 
		overall_text='Lorem ipsum dolor sit amet, augue deseruisse appellantur te eam, eu omnium offendit pro. Cu iudico vidisse definitiones pri, ne enim duis iisque mei, id mundi pericula partiendo per. Duo at alterum disputando conclusionemque, cu facete torquatos vis, est decore scripserit ut. Corrumpit incorrupte id his, ius ut lorem inani tritani. Vero vocibus usu in, in neglegentur delicatissimi mei.', 
		overall_rating=random.randint(1,5)
	)

	mr1_dietary = add_review_dietary(
		review=mr1, 
		nuts_rating=random.randint(1,5), 
		gluten_rating=random.randint(1,5), 
		vegetarian_rating=random.randint(1,5), 
		vegan_rating=random.randint(1,5), 
		dairy_rating=random.randint(1,5)
	)

	mr2 = add_review(
		restaurant=marco, 
		user='mark', 
		title='Lorem ipsum dolor sit amet!', 
		overall_text='Lorem ipsum dolor sit amet, augue deseruisse appellantur te eam, eu omnium offendit pro. Cu iudico vidisse definitiones pri, ne enim duis iisque mei, id mundi pericula partiendo per. Duo at alterum disputando conclusionemque, cu facete torquatos vis, est decore scripserit ut. Corrumpit incorrupte id his, ius ut lorem inani tritani. Vero vocibus usu in, in neglegentur delicatissimi mei.', 
		overall_rating=random.randint(1,5)
	)

	mr2_dietary = add_review_dietary(
		review=mr2, 
		nuts_rating=random.randint(1,5), 
		gluten_rating=random.randint(1,5), 
		vegetarian_rating=random.randint(1,5), 
		vegan_rating=random.randint(1,5), 
		dairy_rating=random.randint(1,5)
	)

	mr3 = add_review(
		restaurant=marco, 
		user='mark', 
		title='Lorem ipsum dolor sit amet!', 
		overall_text='Lorem ipsum dolor sit amet, augue deseruisse appellantur te eam, eu omnium offendit pro. Cu iudico vidisse definitiones pri, ne enim duis iisque mei, id mundi pericula partiendo per. Duo at alterum disputando conclusionemque, cu facete torquatos vis, est decore scripserit ut. Corrumpit incorrupte id his, ius ut lorem inani tritani. Vero vocibus usu in, in neglegentur delicatissimi mei.', 
		overall_rating=random.randint(1,5)
	)

	mr3_dietary = add_review_dietary(
		review=mr3, 
		nuts_rating=random.randint(1,5), 
		gluten_rating=random.randint(1,5), 
		vegetarian_rating=random.randint(1,5), 
		vegan_rating=random.randint(1,5), 
		dairy_rating=random.randint(1,5)
	)

	marco_menu = add_menus(
		restaurant=marco, 
		nuts_marked=True, 
		nuts_sep=False, 
		gluten_marked=True, 
		gluten_sep=False, 
		vegetarian_marked=False, 
		vegetarian_sep=True, 
		vegan_marked=False, 
		vegan_sep=True, 
		dairy_marked=True, 
		dairy_sep=True, 
		general_sep=False
	)




def add_review(restaurant, user, title, overall_text, overall_rating):
	rev = Review.objects.get_or_create(
		restaurant=restaurant, 
		user=user, 
		title=title, 
		overall_text=overall_text, 
		overall_rating=overall_rating
	)[0]

	return rev

def add_review_dietary(review, nuts_rating, gluten_rating, vegetarian_rating, vegan_rating, dairy_rating):
	red = ReviewDietary.objects.get_or_create(
		review=review, 
		nuts_rating=nuts_rating, 
		gluten_rating=gluten_rating, 
		vegetarian_rating=vegetarian_rating, 
		vegan_rating=vegan_rating, 
		dairy_rating=dairy_rating
	)[0]
	return red

def add_restaurant(name, address, postcode, phone_number, url):
	res = Restaurant.objects.get_or_create(
		name=name, 
		address=address, 
		postcode=postcode, 
		phone_number=phone_number, 
		url=url
	)[0]

	return res

def add_menus(restaurant, nuts_marked, nuts_sep, gluten_marked, gluten_sep, vegetarian_marked, vegetarian_sep, vegan_marked, vegan_sep, dairy_marked, dairy_sep, general_sep):

	men = RestaurantMenus.objects.get_or_create(
		restaurant=restaurant, 
		nuts_marked=nuts_marked, 
		nuts_sep=nuts_sep, 
		gluten_marked=gluten_marked, 
		gluten_sep=gluten_sep, 
		vegetarian_marked=vegetarian_marked, 
		vegetarian_sep=vegetarian_sep, 
		vegan_marked=vegan_marked, 
		vegan_sep=vegan_sep, 
		dairy_marked=dairy_marked, 
		dairy_sep=dairy_sep, 
		general_sep=general_sep
	)[0]

	return men

#Start Executing
if __name__ == '__main__':
	print('Starting eatease poulation script')
	os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'eatease.settings')
	from core.models import Restaurant, RestaurantMenus, Review, ReviewDietary
	populate()