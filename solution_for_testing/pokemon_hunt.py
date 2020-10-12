import bisect

locations = {}

file = open('../inputs/input4.txt',"r")

current_location = [0,0]
locations[0] = [0]

count = 1

def is_input_valid(commands: str) -> bool:
    for character in commands:
        if character != "N" and character != "O" and character != "E" and character != "S":
            return False
    return True

def getLocation(location, command):
	if command == "N":
		return [location[0],location[1]+1]
	if command == "S":
		return [location[0],location[1]-1]
	if command == "E":
		return [location[0]+1,location[1]]
	if command == "O":
		return [location[0]-1,location[1]]

input_ = file.readline()

if not is_input_valid(input_):
	print("Bad input")
	quit()

while input_:
	for char in input_:
		current_location = getLocation(current_location,char)
		if not current_location[0] in locations:
			locations[current_location[0]] = [current_location[1]]
			count += 1
		else:
			item_found = False
			for location_ in locations[current_location[0]]:
				if current_location[1] == location_:
					item_found = True
					break
				elif location_>current_location[1]:
					break
			if not item_found:
				bisect.insort(locations[current_location[0]], current_location[1])
				count += 1
	input_ = file.readline()
	if not is_input_valid(input_):
		print("Bad input")
		quit()


file.close()
print("total: {}".format(count))