"""
Test file to check the working of recommender
With 600 principal components preserving 92% variance of data.
"""
import csv
import numpy as np

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
    dim=600
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
uid=int(input("Enter userid"))    
q=m[uid-1]

#Get the list of movies watched by userid
watch=m[uid-1]

watched=list()
for i in range(len(watch)):
    if(watch[i]==5):
        watched.append(i)
        
print('List of movies User rated-5\n',watched)

#Sorting the user_rating row based on index


predict=query(q,V)
idx=predict.argsort()[::-1]

predicted=predict[idx]


#print(predict[0])

i=0
j=0
wp=list()
while(j<100):
    if(predict[idx[j]]>4.5):
        wp.append(idx[j])
    j+=1
        
print('List of movies with prediction>4.5')    
print(np.sort(wp).tolist())
    
     

    
     
       


