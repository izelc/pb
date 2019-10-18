#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[3]:


import numpy as np
#d) Create a zero matrix using a function provided by numpy.
d= np.zeros((3,4))
print(d)


# In[4]:


#e) Print the second row of an 4 × 3 array.
e = np.matrix([[1,2,3,4],[4,3,4,2],[4,3,97,7]])
print(e[1])


# In[5]:


#f) Print the third column of an 4 × 4 array.
f=np.random.randint(100,size=(4,4))
print(f)
print(f[:,3])


# In[6]:


#g) Transpose an array.


# In[7]:


x3 =np.array([[1,2,3,4],[7,5,3,1],[6,5,3,2],[9,7,5,7]]) 
#np.ones((4,4)) 
#np.random.randint(10, size=(4, 4))
print(x3)
print('-----------------------------')
print(x3[3,2])


# In[8]:


#b) Create a 1 × 4 row vector.
b=np.array([1,2,3,4])
print(b)


# In[9]:


#c) Create a 5 × 1 column vector.
c=np.array([[1],[2],[3],[4],[5]])
print(c)


# In[10]:


#h) Create two arrays of equal size (m × m). Multiply them once using conventional matrix multiplication and once using elementwise multiplication.
m=np.random.randint(10,size=(4,4))
z=np.random.randint(10,size=(4,4))
print(m)
print(z)

#elementwise
n=m*z

#matrix multiplication
o=np.matmul(m,z)

print(n)
print(o)


#axis changes vertically and horizontally concatanation
print(np.concatenate((m,z),axis=1))


'''

l) Replicate a 3 × 1 vector to an array of size 3 × 1000.

m) Replace all matrix entries less than 0 by 0.

n) Create a vector containing numbers from 1 to 100 with a gap of 7 between the numbers.
o) Create a vector with 100 entries. Set every second element to 0.
p) Create a vector with 100 entries. Delete every second element.
q) Create 2 arrays a, b of size 1000 × 3 containing random numbers.
'''


# In[11]:


print(np.ones((10,2)).reshape(4,5))


# In[12]:


'''
array1 = np.array([2, 2, 2, 0, 2, 0, 2])
print np.where(array1==0, 1, array1) 
'''

#m) Replace all matrix entries less than 0 by 0.

arr=np.array([[-1,2,0],[-2,-8,8],[1,2,-5]])
print(np.where(arr<0, 0, arr)) 


# In[13]:


#n) Create a vector containing numbers from 1 to 100 with a gap of 7 between the numbers.
arr=np.arange(1,100,7)
print(arr)


# In[21]:


#p) Create a vector with 100 entries. Delete every second element.
o=np.arange(1,100)
print(o)
x = np.delete(o, np.arange(1, o.size, 2))
print(x)


# In[25]:


#o) Create a vector with 100 entries. Set every second element to 0.
p=np.arange(1,100)
print(p)
#startinex: stop index: step size , called slicing 
p[0:50:2]=0
print(p)


# In[24]:


#q) Create 2 arrays a, b of size 1000 × 3 containing random numbers
q1=np.random.randint(10, size=(2,3))
q2=np.random.randint(10, size=(2,3))
print(q1)
print(q2)
#numrows = len(arr)    # row num 
#numcols = len(arr[0]) # column num
'''r) You can interprete the rows of such a arrays as vectors of size 1 × 3. Compute the dot product of
those vectors using loops. This means you have to iterate over the rows of the 1000 × 3 array and
compute the dot product between the vectors represented by the current array row.'''
sumrow=np.zeros(len(q1))
for i in range(len(q1)):
    for j in range(len(q1[i])):
        sumrow[i]+=q1[i,j]*q2[i,j]
        
print(sumrow)

#np.dot() This function returns the dot product of two arrays. For 2-D vectors, it is the equivalent to matrix multiplication
summ=np.zeros(len(q1))
for i in range(len(summ)):
 summ[i]=np.dot(q1[i],q2[i])

print(summ)


# In[ ]:




