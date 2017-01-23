att={
'cap_type':['bell','conical','convex','flat','knobbed','sunken'], 
'cap_surface':['fibrous','grooves','scaly','smooth'], 
'cap_color':['brown','buff','cinnamon','gray','green','pink','purple','red','white','yellow'], 
'bruises':['yes','no'], 
'odor':['almond','anise','creosote','fishy','foul','musty','none','pungent','spicy'], 
'gill_attachment':['attached','descending','free','notched'], 
'gill_spacing':['close','crowded','distant'], 
'gill_size':['broad','narrow'], 
'gill_color':['black','brown','buff','chocolate','gray','green','orange','pink','purple','red','white','yellow'], 
'stalk_shape':['enlarging','tapering'], 
'stalk_root':['bulbous','club','cup','equal','rhizomorphs','rooted','missing'], 
'stalk_surface_above_ring':['fibrous','scaly','silky','smooth'], 
'stalk_surface_below_ring':['fibrous','scaly','silky','smooth'], 
'stalk_color_above_ring':['brown','buff','cinnamon','gray','orange','pink','red','white','yellow'], 
'stalk_color_below_ring':['brown','buff','cinnamon','gray','orange','pink','red','white','yellow'], 
'veil_type':['partial','universal'], 
'veil_color':['brown','orange','white','yellow'], 
'ring_number':[0,1,2], 
'ring_type':['cobwebby','evanescent','flaring','large','none','pendant','sheathing','zone'], 
'spore_print_color':['black','brown','buff','chocolate','green','orange','purple','white','yellow'], 
'population':['abundant','clustered','numerous','scattered','several','solitary'], 
'habitat':['grasses','leaves','meadows','paths','urban','waste','woods'],
}
ch='y'
while ch=='y':
	donelist={}
	keys=[
	'cap_type',
	'cap_surface',
	'cap_color',
	'bruises',
	'odor',
	'gill_attachment',
	'gill_spacing',
	'gill_size',
	'gill_color',
	'stalk_shape',
	'stalk_root',
	'stalk_surface_above_ring',
	'stalk_surface_below_ring',
	'stalk_color_above_ring',
	'stalk_color_below_ring',
	'veil_type',
	'veil_color',
	'ring_number',
	'ring_type',
	'spore_print_color',
	'population',
	'habitat',
	]
	import mysql.connector
	found=0
	db=mysql.connector.connect(user='root',password='Vmrkvv$2212',host='127.0.0.1',database='vignesh')
	c=db.cursor()
	while(len(keys)>0):
		answer=''
		while 1:
			try: curratt=keys.pop()
			except: break
			curratt=[curratt]
			question=curratt.copy()[0]
			curratt=curratt[0]
			question.replace('_',' ')
			print('what is the '+curratt+'?')
			for val in att[curratt]:
				print('     '+str(val))
			print("     I don't know")
			answer=input('Enter your answer : ')
			print('Alright, Noted...')
			if answer=="I don't know": continue
			donelist[curratt]=answer
			break
		if answer=='': break;
		query="select distinct(type) from mushrooms where "
		for k in donelist.keys():
			if k.isnumeric(): query+=k+'='+donelist[k]+' and '
			else: query+=k+'="'+donelist[k]+'" and '
		query=query[:len(query)-4]
		c.execute(query)
		output=c.fetchall()
		if len(output)==1:
			print('The mushroom is '+output[0][0])
			found=1
			break
		elif len(output)==0: break
		else: continue
	if found==0:
		print("Sorry, I couldn't figureout the type of mushroom. :(")
		print('Perhaphs you should know more about it and then come back. :)')
	ch=input('Do you wanna try again? (y/n) : ')
	
	
	
	
	
	
	
	
	
	
	
	
	
	