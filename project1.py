#super market bill generation:
#we want date and time so we take import
from datetime import datetime

name=input("enter your name:")

#list of  available items

lists='''
rice    Rs 20/kg
sugar   Rs 15/kg
salt    Rs 10/kg
oil     Rs 110/l
atta    Rs 55/kg
noodles RS 45/500g
boost   Rs 90/500g
paste   Rs 40/200g
'''
#print(lists)

#declaration
price=0
pricelist=[]
totalprice=0
finalfinalprice=0
ilist=[]
qlist=[]
plist=[]

#rates of items
items={'rice':20,'sugar':15,'salt':10,
       'oil':110,'atta':55,'noodles':45,'boost':90,
       'paste':40}

option=int(input("for list of items press 1:"))
if option==1:
    print(lists)
for i in range(len(items)):
    inp1=int(input("if you want to buy press1 or 2 for exit:"))
    if inp1==2:
        break
    if inp1==1:
        item=input("enter your items:")
        quantity=int(input("enter quantity:"))
        if item in items.keys():
            price=quantity*(items[item])

#print(price)
            pricelist.append((item,quantity,items,price))
            totalprice+=price
            ilist.append(item)
            qlist.append(quantity)
            plist.append(price)
            gst=(totalprice*5)/100
            finalamount=gst+totalprice
        else:
            print("sorry the enetered item is not available")  
    else:
        print("you entered wrong number")
    inp=input("can i bill the items yes or no:")
    if inp=='yes':
        pass
    if finalamount!=0:
        print(25*"=""kiran supermarket",25*"=")
        print(28*" ""wanaparthy")
        print("Name:",name,30*" ","Date:",datetime.now())
        print(75*"-")
        print("sno,8*",'items',8*" ",'Quantity',3*" ",'price')
              
        for i in range(len(pricelist)):
            print(i,8*' ',5*' ',ilist[i],3*' ',qlist[i],8*"",plist[i])
        print(75*"-")
        print(50*" ",'TotalAmount:','Rs',totalprice)
        print("gst amount",40*" ",'Rs',gst)
        print(75*"-")
        print(50*" ",'finalamount:','Rs',finalamount)
        print(75*"-")
        print(20*" ","Thanks for visiting")
        print(75*"-")








          