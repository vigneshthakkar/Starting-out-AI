ch='y'
while ch=='y':
	att=['hair','feathers','eggs','milk','airborne','aquatic','predator','toothed','backbone','breathes','venomous','fins','legs','tail','domestic','catsize']
	import mysql.connector
	found=0
	output=[]
	db=mysql.connector.connect(user='root', password='Vmrkvv$2212', host='127.0.0.1', database='vignesh')
	c=db.cursor()
	donelist={}
	while(len(att)>0):
		answer=''
		while 1:
			try: curratt=att.pop();
			except: break
			print()
			print()
			print(curratt+'?')
			if curratt=='legs':
				answer=input("Enter number in 0,2,4,5,6,8 (Enter 'I don't know' if you don't kow the answer) : ")
			else:
				print('     yes')
				print('     no')
				print("     I don't know")
				answer=input('Enter your answer : ')
			print('Alright, Noted...')
			if answer=="I don't know": continue
			donelist[curratt]=answer
			break
		if answer=='': break;
		query="select distinct(name) from animals where "
		for k in donelist.keys():
			try: query+=k+'='+int(donelist[k])+' and '
			except: query+=k+'="'+donelist[k]+'" and '
		query=query[:len(query)-4]
		c.execute(query)
		output=c.fetchall()
		if len(output)==1:
			print()
			print()
			print('The animal is '+output[0][0])
			found=1
			break
		elif len(output)==0: break
		else: continue
	if found==0:
		print("Sorry, I couldn't figureout the animal. :(")
		if len(output)>0:
			print('The possible animals are : ')
			for i in range(len(output)):
				print(output[i][0])
		print('Perhaphs you should know more about it and then come back. :)')
	ch=input('Do you wanna try again? (y/n) : ')