import pickle
class Customer:
    cuslist=[]
    def __init__(self):
        self.id=0
        self.age=0
        self.name=""

    def addcust(self):
        Customer.cuslist.append(self)

    def searchcust(self):
        for cus in Customer.cuslist:
            if(cus.id==self.id):
                self.age=cus.age
                self.name=cus.name


    def delcust(self):
        # for i in range(len(Customer.cuslist)):
        #     if(Customer.cuslist[i].id==self.id):
        #         cus=Customer.cuslist.pop(i)
        #         return
        for e in Customer.cuslist:
            if(e.id==self.id):
                Customer.cuslist.remove(e)
                return
    @staticmethod
    def savetoPickle():
        f=open("D://cetpa//mypickle.txt","wb")
        pickle.dump(Customer.cuslist,f)
        f.close()
    @staticmethod
    def loadfromPickle():
        f = open("D://cetpa//mypickle.txt", "rb")
        Customer.cuslist=pickle.load(f)
        f.close()


#Presentation Layer
def displayall():
    for cus in Customer.cuslist:
        print("Customer ID:",cus.id, "Customer Age:",cus.age, "Customer Name:",cus.name)


while(1):
    print("1 to add customer, 2 to delete customer")
    print("3 to search customer, 4 to display all")
    print("5 to exit, 6 save to pickle, 7 load from pickle:")
    c=int(input("Enter Your Choice"))
    if(c==1): #Add Customer
        cus=Customer()
        cus.id=int(input("Enter Customer ID"))
        cus.age=int(input("Enter Customer Age"))
        cus.name=input("Enter Customer Name")
        cus.addcust()
    elif(c==2): #Delete Customer
        cus=Customer()
        cus.id=int(input("Enter Customer ID"))
        cus.delcust()
        print("Customer Deleted Successfully")
    elif(c==3): #Search Customer
        cus=Customer()
        cus.id=int(input("Enter Customer ID"))
        cus.searchcust()
        print("Cust ID:",cus.id,"Cust Name:",cus.name, "Cust Age:",cus.age)
    elif(c==4):
        displayall()
    elif(c==5):
        exit()
    elif (c == 6):
        Customer.savetoPickle()
    elif (c == 7):
        Customer.loadfromPickle()

