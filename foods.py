{
	"cmd": ["/usr/local/bin/python3", "-u", "$file"],
}

# Copying a list
my_foods = ['burgers', 'pizzas', 'tacos']
friend_foods = my_foods[:]

# Prove that the two lists are separate lists
my_foods.append('wings')
friend_foods.append('ice cream')

print("My favorite food are:")
print(my_foods)

print("\nMy friend's favorite foods are the exact as mine:")
print(friend_foods)

