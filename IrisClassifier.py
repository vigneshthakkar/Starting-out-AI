from sklearn import linear_model
import mysql.connector

cls={'Iris-setosa':1,'Iris-versicolor':2,'Iris-virginica':3}
clsrev={1:'Iris-setosa',2:'Iria-versicolor',3:'Iria-virginica'}

db=mysql.connector.connect(database='vignesh', user='root', password='Vmrkvv$2212', host='127.0.0.1')
c=db.cursor()
c.execute('select * from iris')
data=c.fetchall()
x,y=[],[]
for each in data:
	a=[]
	for i in range(5):
		if i==4: y.append(cls[each[i]])
		else: a.append(each[i])
	x.append(a)
lr=linear_model.LogisticRegression(solver='newton-cg', multi_class='multinomial')
lr.fit(x,y)
print('Model score : ',lr.score(x,y)*100,'%')
char='y'
while char=='y':
	print('Enter the dimensions of the test iris flower...')
	a=[]
	z=float(input('Enter the sepal length : '))
	a.append(z)
	z=float(input('Enter the sepal width : '))
	a.append(z)
	z=float(input('Enter the petal length : '))
	a.append(z)
	z=float(input('Enter the petal width : '))
	a.append(z)
	x=[a]
	print(lr.predict(x))
	print('The flower might be : ',clsrev[lr.predict(x)[0]])
	char=input('Test one more sample? (y/n) : ')
	