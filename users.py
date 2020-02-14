import pickle
import hashlib

class User:
	def __init__(self, username, pwhash):
		self.name = username
		self.pwhash = pwhash
		self.scores = []

	def login_user(users):
	username, hashed_pw = get_username_password()
	if username not in users:
		print("User does not exist")
	elif hashed_pw != users[username].pwhash:
		print("Wrong password!")
	return users[username]

	def get_score(user):
		score = int(input("Provide score"))
		user.scores.append(score)

	def get_username_password():
	username = input("Enter username: ")
	password = input("Enter password: ")
	hashed_pw = create_hash(username, password)
	if hashed_pw == None:
		get_username_password()
	return username, hashed_pw

	def create_user():
		username, hashed_pw = get_username_password()
		return User(username, hashed_pw)


def create_hash(username, password):
	hasher = hashlib.sha256()
	hasher.update(username.encode('utf-8'))
	if len(password) < 10 or len(password) > 2^32-1: 
		print("Silly wabbit cannot hiaev pazzwerdz *tsktsktsk*")
		return None
	hasher.update(password.encode('utf-8'))
	return hasher.digest()



if __name__ == "__main__":
	try:
		f = open("userdb", 'rb')
		users = pickle.load(f)
	except Exception as e:
		users = {}
	done = False
	user = None
	while not done:
		command = input("Input command (h for help): ")
		if command == 'c':
			user = create_user()
			users[user.name] = user
		elif command == 'l':
			user = login_user(users)
		elif command == 'v':
			print(user.name + " - " + str(user.scores))
		elif command == 's':
			get_score(user)
		elif command == '':
			done = True
		elif command == 'h':
			print("c - create user")
			print("l - login to existing user")
			print("v - view scores for current user")
			print("s - input score for current user")
			print("h - show this help")
			print("blank line to quit")
		with open("userdb", 'wb') as f:
			pickle.dump(users, f)
	f.close()


