n = [4,6,1,2,3,5,7]

for i in range (len(n)):
    for j in range (i+1,len(n)):
        if n[j] < n[i]:
            n[j], n[i] = n[i], n[j]
            
print(n)
    