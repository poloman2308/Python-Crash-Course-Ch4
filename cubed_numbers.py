{
	"cmd": ["/usr/local/bin/python3", "-u", "$file"],
}

cubed = []
for number in range(1, 11):
	cube = number**3
	cubed.append(cube)

for cube in cubed:
	print(cube)

	