#for loop exercise

#Exercise 1
result=["heads","tails","tails","heads","tails","heads","heads","tails","tails","tails"]
count=0
for res in result:
    if res=="heads":
        count=count+1
print("head count is ",count)    


#Exercise 2
for i in range(1,10):
    if(i%2==0):
        continue
    print(i*i)


 #Exercise 3
for i in range(5):
    print(f"You can run{i+1} miles")
    tired=input("Are you tired?")
    if tired=="yes":
        break
    if(i==4):
        print("hurray you are a rock star")
    else:
        print("You did'nt finish the race")  




  #Exercise 4
for i in range(1,6):
    s=''
    for j in range(i):
        s+='*'
    print(s)                
