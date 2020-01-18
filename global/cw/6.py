friends = {}


def add_friends(nameOfPerson, listOfFriends):
	global friends
	if nameOfPerson in friends.keys():
		friends[nameOfPerson] += listOfFriends
	else:
		friends[nameOfPerson] = listOfFriends
	return 


def is_friends(nameOfPerson1, nameOfPerson2):
	global friends
	return nameOfPerson2 in friends[nameOfPerson1]


def print_friends(nameOfPerson):
	global friends
	print(' '.join(sorted(friends[nameOfPerson])))
