#!/usr/bin/env python
# coding: utf-8

# In[ ]:


p1={"pnr":"--","berthno":1,"cts":'avl',"berthtype":'lb',"name":"--",'age':"--"}
p2={"pnr":"--","berthno":2,"cts":'avl',"berthtype":'lb',"name":"--","age":"--"}
p3={"pnr":"--","berthno":3,"cts":'avl',"berthtype":'lb',"name":"--","age":"--"}
p4={"pnr":"--","berthno":4,"cts":'avl',"berthtype":'lb',"name":"--","age":"--"}
p5={"pnr":"--","berthno":5,"cts":'avl',"berthtype":'mb',"name":"--","age":"--"}
p6={"pnr":"--","berthno":6,"cts":'avl',"berthtype":'mb',"name":"--","age":"--"}
p7={"pnr":"--","berthno":7,"cts":'avl',"berthtype":'mb',"name":"--","age":"--"}
p8={"pnr":"--","berthno":8,"cts":'avl',"berthtype":'mb',"name":"--","age":"--"}
p9={"pnr":"--","berthno":9,"cts":'avl',"berthtype":'ub',"name":"--","age":"--"}
p10={"pnr":"","berthno":10,"cts":'avl',"berthtype":'ub',"name":"--","age":""}
p11={"pnr":"","berthno":11,"cts":'avl',"berthtype":'ub',"name":"--","age":"--"}
p12={"pnr":"","berthno":12,"cts":'avl',"berthtype":'ub',"name":"--","age":"--"}
p13={"pnr":"","berthno":13,"cts":'avl',"berthtype":'sub',"name":"--","age":"--"}
p14={"pnr":"","berthno":14,"cts":'avl',"berthtype":'sub',"name":"--","age":"--"}
p15={"pnr":"","berthno":15,"cts":'avl',"berthtype":'slb',"name":"--","age":"--"}
p16={"pnr":"","berthno":16,"cts":'avl',"berthtype":'slb',"name":"--","age":"--"}

l=[p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12,p13,p14,p15,p16]
def book(berth,name,age):
    count=0
    if age<=5:
        return "No ticket"
    if age>5 and age<=60:
        for i in l:
            count+=1
            if i["cts"]=="avl" and i["berthtype"]==berth:
                i["cts"]="fil"
                i["age"]=age
                i["name"]=name
                
                i["pnr"]=count+1234
                return ["ticket booked with pnr",count+1234]         
    if age>60:
        for i in l:
            count+=1
            if i["cts"]=="avl" and i["berthtype"]==berth:
                i["cts"]="fil"
                i["age"]=age
                i["name"]=name
                
                i["pnr"]=count+1234
                return("ticket booked with pnr",count+1234)
                break
            else:
                if i["cts"]=="avl":
                    i["cts"]="fil"
                    i["age"]=age
                    i["name"]=name
                    
                    i["pnr"]=count+1234
                    return("ticket booked with pnr",count+1234)
                    break
def choice(n):
    
    if n==1:
        print("ticket booking")
        berth=input("enter birth preference")
        name=input("enter your name")
        age=int(input("enter your age"))
        print(book(berth,name,age))
        return (choice(n=int(input("enter your choice 1-booking 2-diplay pnr 3-current status"))))
    elif n==2:
        s=int(input("enter"))
        for i in l:
            if i["pnr"]==s:
                print(i)
        return (choice(n=int(input("enter your choice 1-booking 2-diplay pnr 3-current status"))))
    elif n==3:
        for i in l:
            print(i)
        return (choice(n=int(input("enter your choice 1-booking 2-diplay pnr 3-current status"))))
    else:
        return "exit"
    
    
print(choice(n=int(input("enter your choice 1-booking\n2-diplay pnr details\n3-Total chart"))))
   


