#Exercise of if else statement

#Exercise 1
india=["mumbai","banglore","chennai","delhi"]
pakistan=["lahore","karachi","islamabad"]
bangladesh=["dhaka","khulna","rangpur"]

cities=input("Enter the city name")
if cities in india:
    print(f"{cities} is in india")
elif cities in pakistan:
    print(f"{cities} is in pakistan")
elif cities in bangladesh:
    print(f"{cities} is in bangladesh")


    #Exercise 2
    c1=input("Enter the first city")
    c2=input("Enter the second city")

    if c1 and c2 in india:
        print("Both the city belong to India")
    else:
        print("Both the city are not belong to the same country")      


        #Exercise3
        s=input("Enter the fasting sugar level")
        if s<80:
            print("Sugar is Low")
        elif s>100:
            print("sugar is high")          
