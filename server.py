import socket

dbList = []

#Loading the data into a list of lists
with open('data.txt') as file:
	for line in file:
		wordsList = line.split('|')
		dbWordList =[]
		for word in wordsList:
			v = word.strip('\n')
			dbWordList.append(v.strip())
		if dbWordList[0] != '':
			dbList.append(dbWordList) 

def make_report():
	dbList.sort()
	report = "**Python DB contents**\n"
	for line in dbList:
		for word in line:
			report = report + word + "|"
		report = report[0:-1] + '\n'
	return report

def get_list(name):
	for customerData in dbList:
		if str(customerData[0]) == name:
			return customerData	
	return f"{name} Not Found in DataBase"

def get_details(name):
	variable = get_list(name)
	if isinstance(variable,str):
		return variable
	else:
		report = "Server Response: "
		for word in variable:
			report = report + word + "|"
		report = report[0:-1] + '\n'
		return report

def add_customer(name,age,address,phone):
	variable = get_list(name)
	if isinstance(variable,str):
		dbList.append([name,age,address,phone])
		return "Customer successfully added to DataBase"
	else:
		return "Customer already exists in DataBase"

def delete_customer(name):
	for customerData in dbList:
		if str(customerData[0]) == name:
			dbList.remove(customerData)
			return f"Deleted {name} successfully"	
	return f"{name} Not Found in DataBase"

def update_info(name,typeOfinformation,information):
	variable = get_list(name)
	if isinstance(variable,str):
		return variable
	else:
		variable[typeOfinformation] = information
		return "Update Successfull"

#Server related Code:
s = socket.socket()
port = 9999
s.bind(('',port))
s.listen(5)
print("socket is listening")

while True:
	c, addr = s.accept()
	optionPicked = c.recv(1024).decode('utf8')

	if int (optionPicked) != 7:
		name = c.recv(1024).decode('utf8')

	if int(optionPicked) == 1:
		c.send(get_details(name).encode('utf8')) 
	elif int(optionPicked) == 2:
		age = c.recv(1024).decode('utf8')
		address = c.recv(1024).decode('utf8')
		phone = c.recv(1024).decode('utf8')
		c.send(add_customer(name,age,address,phone).encode('utf8'))
	elif int(optionPicked) == 3:
		c.send(delete_customer(name).encode('utf8'))
	elif int(optionPicked) == 4:
		age = c.recv(1024).decode('utf8')
		c.send(update_info(name,1,age).encode('utf8'))
	elif int(optionPicked) == 5:
		address = c.recv(1024).decode('utf8')
		c.send(update_info(name,2,address).encode('utf8'))
	elif int(optionPicked) == 6:
		phone = c.recv(1024).decode('utf8')
		c.send(update_info(name,3,phone).encode('utf8'))
	elif int(optionPicked) == 7:
		c.send(make_report().encode('utf8'))
	
	c.close

