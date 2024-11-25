print("*"*5,"ATM Machine","*"*5)
amount=int(input("enter the amount:"))
l=[500,200,100,50,20,10,5,2,1]
c=0
single_notes={}
for i in l:
    Notes=amount//i
    c=c+Notes
    if Notes==1:
        single_notes[i]=Notes
    print(f"{i} notes--> {Notes}")
    amount=amount%i
print("Minimum number of notes:",c)
print("Number of single notes",single_notes)