import numpy as np

input_file="" #open test file
input=open(input_file,"r")

vertices=int(input.readline()) #reading the input file
buildGraph=np.zeros((vertices,vertices))

while True:        
        textLine=input.readline()
        
        if textLine=="":
            break
        textLine=textLine.split()       
        
        p=int(textLine[0])
        q=int(textLine[1])
        buildGraph[q][p]=1

input.close()

print("\nWeb Graph:\n",buildGraph) #Print the Web Graph

print("\nVertices: ",vertices) #Print vertices number

M=np.zeros((vertices,vertices)) # Calculate Matrix

outerLink=np.sum(buildGraph, axis=0)

for i in range(vertices):
    for j in range(vertices):
        if(buildGraph[i][j]==1):
                M[i][j]=1/outerLink[j]
        
print("\nMatrix (M):\n",M)

r=np.ones(vertices)
r=r/vertices
print("\nBegining of the Iterations:")
print("\nIteration",0, " ", np.around(r, decimals=5))

i=1
while i<100:
    prev_r=r.copy()
    r=np.dot(M,r)
    print("Iteration",i, " ", np.around(r, decimals=5))
    
    change=abs(prev_r-r)/prev_r  

    if(all(i <= 0.05 for i in change)):
        break  
    i=i+1
    
output=open("output "+input_file,"w") #Writing output

for i in range(len(r)):
    strr="< "+str(i)+", "+str(round(r[i], 5))+" >\n"
    output.write(strr)
                      
output.close()
