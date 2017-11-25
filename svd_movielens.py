import csv
import numpy as np
import pandas as pd

def SVD(M):
    
    Mt=np.transpose(M)
    prd=np.dot(M,Mt)
    
    #Eigen Value Decomposition
    eigenvalue,eigenvec=np.linalg.eig(prd)
    
    #Indirect sort on eigenvalue to find out the proper indices, the same can 
    #be used with corresponding eigenvectors
    sortindex=eigenvalue.argsort()[::-1]
    
    #Sort Eigen values
    eigenvalue=eigenvalue[sortindex]    
       
    #To calculate sigma
    sigma=np.sqrt(abs(eigenvalue))
    sigma=np.around(sigma,decimals=2)    
    totalsigma=np.sum(sigma,dtype=float)
    
    #To Calculate Variance of Data preserved
    dim=600
    sumsigma=0.0
    cs=0
    while(cs<600):
        sumsigma+=sigma[cs]
        cs+=1
    print('We have', dim, 'components preserving',(sumsigma/totalsigma)*100,'% variance of data')
    sigma=sigma[0:dim]
    
    
    #To Calculate U - we had earlier calculated eigenvec for MMt
    #Sort and reduce U to nXdim
    U=eigenvec[:,sortindex]
    U=U[:,0:dim]
    U=np.real(U)
    U=np.around(U,decimals=2)
    
   
    
    #To Calculate V
    prd=np.dot(Mt,M)
    eigenvalue,eigenvec=np.linalg.eig(prd)
    sortindex=eigenvalue.argsort()[::-1]
    V=eigenvec[:,sortindex]
    V=V[:,0:dim]
    V=np.real(V)
    V=np.around(V,decimals=2) 
    
    return U,sigma,V
    


def query(q,V):
    #find q*v, w
    prd=np.dot(q,V)
    Vt=np.transpose(V)
    other=np.dot(prd,Vt)
    return other


#To Prepare list of movies - for recommending
print('Movie Recommender using SVD')

fileh=open('u.item','r')
reader = csv.reader(fileh, delimiter='|')
movienames=list()
# The list of all the movies with movieid-1 as list index
for row in reader:
	movienames.append(row[1])

num_users=943
num_movies=1682



#To Prepare matrix M 

fp2=open('u.data','r')
reader = csv.reader(fp2, delimiter='\t')
m=list()
for j in range(num_users):
	m.append([0]*num_movies)
for row in reader:
	m[int(row[0])-1][int(row[1])-1]=float(row[2])
	
M=np.array(m)

U,sigma,V=SVD(M)




#To preduct movies for a user.

print("Enter userid (1-943)")
uid=int(input())    
q=m[uid-1]
predict=query(q,V)

	

#Sorting the user_rating row based on index
idx=predict.argsort()[::-1]
predicted=predict[idx]


#To display 10 movies, can change it by taking input from user
nm=10
i=0
j=0

mr=list()

print("\n\nRecommended movies for UserID",uid,'\n')
while(i<nm):
    if(m[uid-1][idx[j]]==0):
        mr1=list()
        mr1.append(idx[j])
        mr1.append(movienames[idx[j]-1])
        mr.append(mr1)
        #print(idx[j],'\t',,'\t',predict[idx[j]], j)
        i+=1
    j+=1

df=pd.DataFrame(mr,  columns=['MovieID', 'MovieName'])
print(df)

     
       


