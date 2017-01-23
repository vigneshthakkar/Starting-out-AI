stack={1:[],2:[],3:[],4:[],5:[]}

opstack=[]

def find(a):
	for key in stack.keys():
		for i in range(len(stack[key])):
			if stack[key][i]==a: return (key,i)
	print(a,'not found!!')
	return(-1,-1)

def getridof(k,i,dontputonkey):
	done=0
	opstack.append('remove '+str(stack[k][i]))
	for key in stack.keys():
		if key==k or key==dontputonkey: continue
		elif len(stack[key])<5:
			number=stack[k].pop()
			stack[key].append(number)
			done=1
			break
	if done==0: print('Stack overflow. Try Deleting items to clear space.')
	printstack()

def delete(a):
	deleted=0
	for key in stack.keys():
		for i in range(len(stack[key])):
			if stack[key][i]==a:
				stack[key].pop(i)
				deleted=1
	if deleted==1:
		print(a, 'deleted!!')
		printstack()
	else: print(a, 'not found')

def printstack():
	print('The stack looks like...')
	for i in range(4,-1,-1):
		for key in stack.keys():
			try:
				length=len(str(stack[key][i]))
				print(stack[key][i],end=' '*(10-length))
			except: print('',end='          ')
		print()
		
def trytostabilize(k,index,dontputonkey):
	for key in stack.keys():
		if key==k or key==dontputonkey or len(stack[key])>3: continue
		else:
			number=stack[k].pop(index)
			stack[key].append(number)
			k=key
			index=len(stack[key])-1
	return (k,index)

def puton(a,b):
	opstack.clear()
	opstack.append('put '+str(a)+' on '+str(b))
	akey,aindex=find(a)
	if akey==-1: return
	bkey,bindex=find(b)
	if bkey==-1: return
	if akey==bkey and aindex==bindex+1:
		print('The contition is already satisfied...')
		return
	if len(stack[akey])-1>aindex:
		opstack.append('clear '+str(a))
		for i in range(len(stack[akey])-1,aindex,-1):
			getridof(akey,i,bkey)
			bkey,bindex=find(b)
	if len(stack[bkey])-1>bindex:
		opstack.append('clear '+str(b))
		for i in range(len(stack[bkey])-1,bindex,-1):
			getridof(bkey,i,akey)
			akey,aindex=find(a)
	if len(stack[bkey])>=5:
		opstack.append('reallocate '+str(b))
		bkey,bindex=trytostabilize(bkey,len(stack[bkey])-1,akey)
	stack[bkey].append(stack[akey].pop(aindex))
	print('Done!!')
	printstack()

def additem(a,key):
	if len(stack[key])>=5:
		print('Stack overflow, Choose some other row next time...')
	else: stack[key].append(a)
	print('Item added...')
	printstack()
	
	
	
def answer(question):
	if question.rfind('why')!=-1:
		if question.rfind('not')!=-1 or question.rfind("doesn't")!=-1 or question.rfind("didn't")!=-1:
			return 'I hate negativity, please ask affermative questions.'
		elif question.rfind('remove')!=-1:
			question=question.split()
			index=question.index('remove')
			query=' '.join(question[index:index+2])
			if query.rfind('?')!=-1: query=query.rstrip('?')
			try:
				index=opstack.index(query)
				for i in range(index-1,-1,-1):
					if opstack[i].startswith('clear'): return ('I was trying to '+opstack[i])
			except: return 'I never did that!!'
		elif question.rfind('clear')!=-1:
			question=question.split()
			index=question.index('clear')
			query=' '.join(question[index:index+2])
			if query.rfind('?')!=-1: query=query.rstrip('?')
			try:
				index=opstack.index(query)
				return 'I was trying to '+opstack[0]
			except: return 'No, I never did that!!'
		elif question.rfind('put')!=-1:
			question=question.split()
			index=question.index('put')
			query=' '.join(question[index:index+4])
			if query.rfind('?')!=-1: query=query.rstrip('?')
			try:
				index=opstack.index(query)
				return 'Because you told me to do so, remember??'
			except: return 'What?? I never did that!!'
		elif question.rfind('reallocate')!=-1:
			question=question.split()
			index=question.index('reallocate')
			query=' '.join(question[index:index+2])
			query=query.rstrip('?')
			print(query)
			if query in opstack: return "Otherwise a Stack overflow would have occured and you wouldn't have liked it."
			else: return "I'm convinced I didnt do anything like that."
		else: return "I only remove, clear and reallocate stuff. Nothing else. :)"
	elif question.rfind('how')!=-1:
		if question.rfind('not')!=-1 or question.rfind("doesn't")!=-1 or question.rfind("didn't")!=-1:
			return 'I know no negativity, mind asking affermative questions??'
		elif question.rfind('remove')!=-1:
			question=question.split()
			index=question.index('remove')
			query=' '.join(question[index:index+2])
			if query.rfind('?')!=-1: query=query.rstrip('?')
			try:
				index=opstack.index(query)
				answer='I removed '
				for item in opstack[index-1::-1]:
					if item.startswith('clear'): break
					elif item.startswith('remove'): answer+='...'+(item[7:])
				if answer=='I removed ': return 'It was already on the top. So, it was easy to remove. Smart ehh??'
				else: return answer+'...and finally it was on the top. :D'
			except: return "I don't think i ever did that. :("
		elif question.rfind('clear')!=-1:
			question=question.split()
			index=question.index('clear')
			query=' '.join(question[index:index+2])
			if query.rfind('?')!=-1: query=query.rstrip('?')
			try:
				index=opstack.index(query)
				answer='By removing '
				for item in opstack[index+1:]:
					if item.startswith('clear'): break
					elif item.startswith('remove'): answer+='...'+(item[7:])
				if answer=='By removing ': return "It was already on the top. I didn't have to remove anything. :)"
				else: return answer
			except: return "Sorry, but I don't think I did that!"
		elif question.rfind('put')!=-1:
			question=question.split()
			index=question.index('put')
			query=' '.join(question[index:index+4])
			if query.rfind('?')!=-1: query=query.rstrip('?')
			try:
				index=opstack.index(query)
				answer='By clearing '
				a,b=query[4:].split(' on ')
				for item in opstack:
					if item[6:]==a: answer+='...'+a
					elif item[6:]==b: answer+='...'+b
				if answer=='By clearing ': return "I didn't have to do anything"
				else: return answer
			except: return 'Hey, I Never did that!!'
		elif question.rfind('reallocate')!=-1:
			question=question.split()
			index=question.index('reallocate')
			query=' '.join(question[index:index+2])
			query=query.rstrip('?')
			if query in opstack: return "That was pretty easy. It was on the top. Phew!"
			else: return "I'm sure i didn't do anythig like that. You might wanna check again. :)"
		else: "I intelligent enough remove, clear and reallocate stuff. And, I answer questions only about my bihaviour. I'm not answerable for anything other than that."
	elif question.rfind('what')!=-1:
		if question.rfind('not')!=-1 or question.rfind("doesn't")!=-1 or question.rfind("didn't")!=-1:
			return 'Why are you so negative? Ask affermative questions, please...'
		elif question.rfind('above')!=-1:
			question=question.split()
			number=0
			for word in question:
				word=word.rstrip('?')
				if word.isnumeric(): number=word; break
			key,index=find(int(number))
			if key!=-1 and index!=-1:
				try: return "As I examine the situation, "+str(stack[key][index+1])+" is above "+str(stack[key][index])+" in row "+str(key)+"."
				except: return "Looking at the stack, I infer, "+str(stack[key][index])+" is at the top in row "+str(key)+". Nothing is above that."
		elif question.rfind('below')!=-1:
			question=question.split()
			number=0
			for word in question:
				word=word.rstrip('?')
				if word.isnumeric(): number=word; break
			key,index=find(int(number))
			if key!=-1 and index !=-1:
				if index>0: return "As I see the stack, "+str(stack[key][index-1])+" is below "+str(stack[key][index])+" in row "+str(key)+"."
				else: return "Looking at the stack, I seems to me that, "+str(stack[key][index])+" is lowest in row "+str(key)+". Nothing is below that."
		else:
			question=question.split()
			number=0
			for word in question:
				word=word.rstrip('?')
				if word.isnumeric(): number=word; break
			query=''
			index=-1
			for i in range(len(opstack)):
				if opstack[i].rfind(number)!=-1: query=opstack[i]; index=i
			if query=='' and index==-1: return "I pretty sure I did't do anything like that."
			elif query.rfind('remove')!=-1:
				reason=''
				for i in range(index-1,-1,-1):
					if opstack[i].rfind('clear')!=-1: reason=opstack[i]; break
				query=query.replace(' ','d ')
				return "I "+query+" because I was trying to "+reason
			elif query.rfind('clear')!=-1:
				reason=''
				for i in range(index-1,-1,-1):
					if opstack[i].rfind('put')!=-1: reason=opstack[i]; break
				query=query.replace(' ','ed ')
				return "I "+query+" because I was trying to "+reason
			else: return "Sorry, but I sure I didn't come across "+number
	else: return "I'm not smart enough to understand that one. you might wanna ask Vignesh. He is smarter!"
		
	
c='y'
print('Welcome!')
while c=='y':
	print('Choose one of the following options...')
	print('1) Add item')
	print('2) Delete item')
	print('3) Put something on something')
	print('4) Print the stack')
	print('5) Ask Questions')
	a=input('Enter your choice or enter "quit" to exit : ')
	try:
		a=int(a)
		if a==1:
			a=int(input('Enter the item to be added : '))
			key=int(input('Enter the row to which the item is to be added : '))
			additem(a,key)
		elif a==2:
			a=int(input('Enter the item to be deleted : '))
			delete(a)
		elif a==3:
			a=int(input('Enter the an item : '))
			b=int(input('You want to put this item on which item ? '))
			puton(a,b)
		elif a==4: printstack()
		elif a==5:
			char='y'
			while char=='y':
				print()
				question=input('Q - ')
				print('A - '+answer(question))
				print(); print()
				char=input('Ask more questions?? (y/n) : ')
				print()
	except:
		if a=='quit': c='n'
		else: print('Invalid option! Please select a valid option...')
print('Thank you')