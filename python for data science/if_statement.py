# if statement in the python 
# It is used to control the flow of the statement 

#n=input("Enter the number ")
#n=int(n)
#if n%2==0:
    #print("Number is even ")
#else:
    #print("Number is odd") 


    indian=["samosa","kachori","dal","naan"]
    pakistan=["nihari","paya","karahi"]
    bangladesh=["panta bhat","chorchori","funcha"]
    dish=input("Enter the dish name")
    if dish in indian:
        print(f={dish} is indian)
    elif dish in pakistan:
        print(f={dish} is pakistan)
    elif dish in bangladesh:
        print(f={dish} is bangladesh )
    else:
        print(" I don't know about the dish")             

