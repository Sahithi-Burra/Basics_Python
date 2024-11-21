name=input("enter your name:")
age=int(input("enter your age:"))
if(age>=18):
    print("eligible to vote")
else:
    x=18-age
    print("come back after",x,"years")