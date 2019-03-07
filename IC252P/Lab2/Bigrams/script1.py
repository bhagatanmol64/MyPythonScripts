'''File Selector Code'''
fil=input("Enter the file code(A or B):")
files={"A":'_time_mach',"B":'_jane_eyre'}
'''Opening and reading file'''
with open('file'+fil+files[fil]+'.txt','r',encoding="utf8") as f:
    data=f.read().lower()
'''Taking inputs'''
X,Y=input('Enter the first letter:').lower(),input('Enter the second letter:').lower()
rd=''.join(list(filter(None,[c*int(c.isalpha()) for c in data])))
'''Giving Outputs'''
print("Probability of A:","%.6f" %(rd.count(X)/len(rd)))
print("Probability of B:","%.6f" %(rd.count(Y)/len(rd)))
print("Probability of A|B:","%.6f" %(rd.count(Y+X)/rd.count(Y)))
print("Probability of B|A:","%.6f" %(rd.count(X+Y)/rd.count(X)))