import socket
#Client Interface code
def print_menu():
	message = """Python DB Menu

	1. Find customer
	2. Add customer
	3. Delete customer
	4. Update customer age
	5. Update customer address
	6. Update customer phone
	7.Print report
	8.Exit
	"""
	print (message)

def check_number(AgeorPhone):
	number = input(AgeorPhone)
	try:
		value = int(number)
		return value
	except ValueError:
		print("this is not a number.")
		return check_number(AgeorPhone)

def get_input_and_check_it():
	number = input("Select: \n")
	try:
		value = int(number)
		if value in range(1,9):
			return value
		else:
			print ("Number outside specified range")
			return get_input_and_check_it()
	except ValueError:
		print("this is not a number.")
		return get_input_and_check_it()
#Connect to server code
def connect_to_server_and_send_value(valueToBeSent):
	s = socket.socket()
	port = 9999
	s.connect(('127.0.0.1',port))
	s.send(str(valueToBeSent).encode('utf8'))
	if(valueToBeSent != 7):
		s.send(str(input("Customer Name:\n")).encode('utf8'))
	if valueToBeSent == 2:
		s.send(str(check_number("Customer Age:\n")).encode('utf8'))
		s.send(str(input("Customer Address:\n")).encode('utf8'))
		s.send(str(check_number("Customer PhoneNumber:\n")).encode('utf8'))
	if valueToBeSent == 4:
		s.send(str(check_number("Customer Age:\n")).encode('utf8'))
	if valueToBeSent == 5:
		s.send(str(input("Customer Address:\n")).encode('utf8'))
	if valueToBeSent == 6:
		s.send(str(check_number("Customer PhoneNumber:\n")).encode('utf8'))
	print (s.recv(1024).decode('utf8'))
	s.close


print_menu()
inputNumber = get_input_and_check_it()
while inputNumber != 8:
	connect_to_server_and_send_value(inputNumber)
	print_menu()
	inputNumber = get_input_and_check_it()
print ("Thank You, GoodBye!")
