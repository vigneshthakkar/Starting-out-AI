from sklearn import linear_model
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis, QuadraticDiscriminantAnalysis
import mysql.connector
from sklearn.naive_bayes import GaussianNB

cls={'Iris-setosa':1,'Iris-versicolor':2,'Iris-virginica':3}
clsrev={1:'Iris-setosa',2:'Iria-versicolor',3:'Iria-virginica'}

def logisticregression(x,y):
	lr=linear_model.LogisticRegression(solver='newton-cg', multi_class='multinomial')
	lr.fit(x,y)
	return lr

def lineardiscriminantanalysis(x,y):
	lda=LinearDiscriminantAnalysis(solver='lsqr', shrinkage='auto')
	lda.fit(x,y)
	return lda

def quadraticdiscriminantanalysis(x,y):
	qda=QuadraticDiscriminantAnalysis()
	qda.fit(x,y)
	return qda

def gaussiannaivebayes(x,y):
	gnb=GaussianNB()
	gnb.fit(x,y)
	return gnb

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
print('Choose a method : ')
print('1. Logistic Regression')
print('2. Linear Discriminant Analysis')
print('3. Quadratic Discriminant Analysis')
print('4. Gaussian Naive Bayes')
num=int(input('Enter your choice : '))
if num==1: classifier=logisticregression(x,y)
elif num==2: classifier=lineardiscriminantanalysis(x,y)
elif num==3: classifier=quadraticdiscriminantanalysis(x,y)
elif num==4: classifier=gaussiannaivebayes(x,y)
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
	print('The flower might be : ',clsrev[classifier.predict(x)[0]])
	char=input('Test one more sample? (y/n) : ')
