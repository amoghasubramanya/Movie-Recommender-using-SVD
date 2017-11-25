import csv
import numpy as np

def SVD(M,dim):
    Mt=np.transpose(M)
    
    
    #To Calculate U
    prd=np.dot(M,Mt)
    
    #Eigen Value Decomposition
    eigenvalue,eigenvec=np.linalg.eig(prd)
    
    #Indirect sort on eigenvalue to find out the proper indices, the same can 
    #be used with corresponding eigenvectors
    sortindex=eigenvalue.argsort()[::-1]
    
    
    #Sort Eigen values
    eigenvalue=eigenvalue[sortindex]    
    
    #Sort and reduce U to nXdim
    U=eigenvec[:,sortindex]
    U=U[:,0:dim]
    U=np.real(U)
    U=np.around(U,decimals=2)
  
     #To calculate sigma
    sigma=np.sqrt(abs(eigenvalue))
    sigma=sigma[0:dim]
    sigma=np.around(sigma,decimals=2)
    
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
    prd=np.dot(q,V)
    Vt=np.transpose(V)
    print(abs(prd))
    other=np.dot(prd,Vt)
    print(abs(other))
    return


#Reading the data
dataset=list()
fp=open('dataset.txt','r')
reader = csv.reader(fp, delimiter=',')
for row in reader:
    dataset.append(row)
    
    
#print(dataset)
movies=list()
users=list()
for i in dataset[0]:
    movies.append(i)
for i in dataset:
    users.append(i[0])
movies.remove("X")
users.remove("X")
#print(movies)
#print(users)
dataset.pop(0)          #Removing movies
for i in dataset:       #Removing users
    i.pop(0)       
m=list(dataset)
M=np.mat(m,dtype=int)
print(M)
U,sigma,V=SVD(M,2)


print("U ", U)
print("---------------------------------------")
print("sigma ", sigma)
print("---------------------------------------")
print("Vt ", V.transpose())
print("---------------------------------------")

