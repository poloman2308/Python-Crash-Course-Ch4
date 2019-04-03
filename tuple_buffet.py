{
	"cmd": ["/usr/local/bin/python3", "-u", "$file"],
}

menu_items = ('burgers', 'pizzas', 'hot dogs', 'tacos', 'fajitas')

print("The restaurant only offers these foods on its menu:")
for food in menu_items:
	print("- " + food.title())

# Menu gets updated
menu_items = ('burgers', 'pizzas', 'tacos', 'pasta', 'fried rice')

print("\nThe restaurant has updated its menu:")
for food in menu_items:
	print("- " + food.title())

