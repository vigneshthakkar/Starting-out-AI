import tensorflow as tf
import mnist

print('Loading test images...')
testimages=mnist.test_images()
labels=mnist.test_labels()
testlabels=[]
for label in labels:
	a=[0]*10
	a[label]=1
	testlabels.append(a)
print('Test images loaded...')

print('Loading train images...')
trainimages=mnist.train_images()
labels=mnist.train_labels()
trainlabels=[]
for label in labels:
	a=[0]*10
	a[label]=1
	trainlabels.append(a)
print('Train images loaded...')

epochs=int(input('Enter the number of epochs : '))
batchsize=int(input('Enter the batch size : '))
numoflayers=int(input('Enter the number of recurrent layers : '))
numofunits=int(input('Enter the number of units in each layer : '))

weight=tf.Variable(tf.random_normal([numofunits*28,10]))
bias=tf.Variable(tf.random_normal([10]))
initialstate=tf.zeros([batchsize,numofunits])

x=tf.placeholder(tf.float32,[batchsize,28,28])
y=tf.placeholder(tf.float32)

def rnn(x):
	lstm=tf.contrib.rnn.LSTMCell(numofunits)
	dropout=tf.contrib.rnn.DropoutWrapper(lstm)
	rnncell=tf.contrib.rnn.MultiRNNCell([dropout]*numoflayers)
	drnn,state=tf.nn.dynamic_rnn(rnncell,x,dtype=tf.float32)
	fc=tf.reshape(drnn,[-1,28*numofunits])
	output=tf.add(tf.matmul(fc,weight),bias)
	return output

predict_y=rnn(x)
loss=tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits=predict_y,labels=y))
train=tf.train.AdamOptimizer().minimize(loss)

with tf.Session() as sess:
	sess.run(tf.global_variables_initializer())
	print('Training the Recurrent Neural Net...')
	for epoch in range(epochs):
		epochloss=0
		for batch in range(int(60000/batchsize)):
			batch_x,batch_y=trainimages[batchsize*batch:batchsize*(batch+1)],trainlabels[batchsize*batch:batchsize*(batch+1)]
			_,batchloss=sess.run([train,loss],feed_dict={x:batch_x,y:batch_y})
			epochloss+=batchloss
		print('Epoch',epoch+1,'completed. Loss =',epochloss)
	print('Neural Net trained...')
	
	print('Testing the Neural Net...')
	correct=0
	for batch in range(int(10000/batchsize)):
		batch_x,batch_y=trainimages[batchsize*batch:batchsize*(batch+1)],trainlabels[batchsize*batch:batchsize*(batch+1)]
		predict=sess.run(predict_y,feed_dict={x:batch_x})
		for prediction,y in zip(predict,batch_y):
			greatest,index=prediction[0],0
			for i in range(1,10):
				if prediction[i]>greatest: greatest,index=prediction[i],i
			if y[index]==1: correct+=1
	print('Neural Network Tested...')
	print('Accuracy =',correct/100)
	
		
		

