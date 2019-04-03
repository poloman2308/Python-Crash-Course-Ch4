{
	"cmd": ["/usr/local/bin/python3", "-u", "$file"],
}

my_pizzas = ['meat lovers', 'buffalo chicken', 'supreme']
friend_pizzas = my_pizzas[:]

my_pizzas.append('sausage')
friend_pizzas.append('cheese')

print("My favorite pizzas are:")
for pizza in my_pizzas:
	print(pizza.title())

print("\nMy friend's favorite kind of pizzas are:")
for pizza in friend_pizzas:
	print(pizza.title())

	