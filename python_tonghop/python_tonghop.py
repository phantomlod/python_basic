#def dienthoai( n1,n2,n3,*data1,**data2 ) :
#	tong1=tong2=tong3=0
#	tong1=n1+n2+n3
#	for t2 in data1 :
#		tong2=tong2+t2
#	for name,price in data2.items() :	
#		row ="{:20}{:10}".format(name,price)
#		tong3=tong3+ price
#	return tong1,tong2,tong3
#print(dienthoai(1,2,3,4,5,6,7,8,nokia=1000,apple=5000,samsung=3000)) 

#/// tao ham range
#def myrange(start,length,step):
#    i=start 
#    dem=0
#    while (dem<length) :
#        print(i)
#        i=i+step
#        dem=dem+1
#myrange(1,5,2)

#/// tao ham dictionary        
#def counterchar(*data) :
#    dic={}
#    for item in data :
#        for i in item :
#          i=i.upper()
#          if i in dic :
#             dic[i]=dic[i]+1
#          else :
#              dic[i]=1
#    return dic
#print(counterchar("tuan","linh","nhiem","duc","tin"))
#/////////test class
#class car() :
#    fuel = "xang"
#    maxspeed=150
#    def drive(color) :
#
#
#i=car()
#print(i.fuel)

#///ko dung constructor
#class student :
#    def info(self,name,age) :
#        print ("Name:     " ,name,"  age:   ", age)
#hs1=student()
#hs1.info("Phan Van A",18)
#// dung cónstructor + ke thua 1

#class person :
#    def __init__(slef,ho) :
#        print ("Ho : ",ho)
#class student(person) :
#    def dinhdanh(self,name,age):
#        print("Name:    ",name,"  age:   ",age)
#    def __str__(slef):
#        return ("----------------------------")
#    def __del__(self):
#        print ("destroyed")
#hs2=student("Phan")

#// ke thua 2
##class person :
##    def __init__(self,name,age) :
##        self.name= name
##        self.age=age
##    def info(self) :
##        print("toi ten la",self.name," tuoi la : ",self.age)
#nv1=person("Phan Van A",18)
#nv1.info()
##class student(person) :
##    def __init__(self,name,age,grade) :
##       person.__init__(self,name,age)
##       self.grade= grade
##       
##    def infograde(self) :
##        print("toi hoc lop: ",self.grade)
##
##hsa=student("Phan Van Tom","20","9A1")
##
##hsa.info()
##hsa.infograde()

#///doc file (read)
#fp= open("test.txt","r")
##i=1
##for line in fp :
##    print(i,line)
##    i=i+1
##print(i)
#
##// ghi file (wirte)
#wfile= open("wfile.txt","w")
#for line in fp :
#    print (line, file=wfile , end="")
#print("done")
#///buffer
#BUFFERSIZE = 25000
#rFile = open("test.txt","r")
#wFile = open("wfile.txt","w")
#buffersize=rFile.read(BUFFERSIZE)
#i=0
#while (len(buffersize)) :
#    i= i + 1
#    wFile.write(buffersize)
#    print(i,"{} byte".format(len(buffersize)))
#    buffersize = rFile.read(BUFFERSIZE)
#print("Done")

# các hàm liên quan
#rFile= open("test.txt","r")
#fpos=rFile.tell()
#print("doc toi vi tri",fpos)
##line=rFile.readline()
##print(line, end="")
#rFile.seek(300)
#print("-"*50)
#data = rFile.read()
#print(len(data))
#print(data)

#///module
#import random as ra
#print(ra.randint(1,10000))
#x=list(range(25))
#ra.shuffle(x)
#print(x)
#
#import datetime as dt
#import os 
#print(os.getcwd())
#
#
#import MyModule as my
#print(my.sum(20))
#my.linh()

# quan ly va xu ly loi
#try : 
#    a=100
#    b=0
#    x=a/b
#except ZeroDivisionError as error :
#    print("Loi: ",error)

#SQL
# create table "monhoc" ("id" integer primary key autoincrement not null, "name" varchar not null) // tao bang
# DROP TABLE "main"."monhoc"
# insert into <table> (cola,colb) values ("val1","val2")/  /them du lieu, CHU IN HOA
# update <table> set cola="teo" where id = 1  /// cap nhat du lieuj
# delete from <table> where id=1 // xoa data
# select * from <table> where id=3 
# select * from <table> order by id desc/asc (tang,giam dan)
# select * from <table> limit 2,2 ( dong 2,2 phan tu)
#import sqlite3 
#db = sqlite3.connect("school.sql")
##db=conn.cursor()
#db.execute("drop table if exists student")
#db.execute('''CREATE TABLE student (id integer primary key not null,name text)''')
#db.execute("INSERT INTO student(name) VALUES ('A')")
#db.execute("INSERT INTO student(name) VALUES ('B')")
#db.execute("INSERT INTO student(name) VALUES ('C')")
#db.execute("INSERT INTO student(name) VALUES ('D')")
#db.execute("INSERT INTO student(name) VALUES ('E')")
#db.execute("UPDATE student SET name=\"hello\" where id=4")
#db.execute("delete from student where id=5")
#db.commit()
#reslut=db.execute("select * from student")
#for row in reslut :
#    print(row)

#//mảng
#mang
#import numpy as np
#a=[1,2,3,4,5]
#arr1=np.array(a)
#print(type(arr1))
#b=[6,7,8,9,10]
#arr2=np.array(b)

#tongarr=np.array([arr1,arr2])
#print(tongarr.shape)
#A=np.arange(10)
#print(A)
##mangA=np.array([1,2,3,4,5])
##mangB=np.arange(25)
##mangC=mangB.reshape(5,5)
#abc=np.array([[12,3,4,5,5,6],[32,4,3,3,2,6]])
#print(abc.shape)
#print(np.zeros(5))
#print(np.ones(10))
#print(abc*abc)
#print(mangC.T)
#B=np.arange(6).reshape(2,3)
#print(B)
#B1=mangB[:10]
#print(B1)
#B1[:]=100
#print(mangB)
##print(mangC)
##print(mangC[2:4,1:4])
##print(mangC.sum())
##x=[]
##y=[]
##for i in range(10) :
##    x.append(np.random.randint(1,10))
##    y.append(np.random.randint(1,10))
##print(x,y)
##x=np.array(x)
##y=np.array(y)
##z=x.sort()
##print(np.unique(x))
##print(np.equal(x,y))

#bài 1 : lặp từ 1 đến 100 & chia thành 10 dòng
##for i in range(1,101) :
##    print(i,end=" ")
##    if i % 10 ==0 :
##        print("")

#bai 2 : 0-200 ; so chan ; 10 dong ; sap xep thanh cac cot thang hang
##for i in range(1,201) :
##    if i%2==0 :
##        print ("{:>3}".format(str(i)), end=" ")
##        if i % 20 == 0 :
##            print("")

#bai 3 : kiem tra so nguyen to
##def songuyento(i):
##    if i<=1 :
##        return False
##    dem =0
##    for j in range(2,i) :
##       
##        if i % j == 0 :
##            dem=dem+1
##    if dem == 0 :
##        return True
##    else :
##        return False

##print(songuyento(-100))

#bai 4 in songuyento 1-1000 , cac cot deu nhau
##dem=0
##for i in range(1,1001) :
##
##    if songuyento(i) == True :
##        dem=dem+1
##        print("{:>3}".format(str(i)), end=" ")
##        if dem%10==0:
##            print("")

#bai 5 : 1 list từ km=m
##l=[10,20,30,40,50]
##for m in l :
##    k=10*m
##    print("{} KM bang {} m".format(m,k))
##
#bai 6 : tinh n!
def giaithua(n) :
  if n<1 :
      print ("n phai lon hon 1")
  elif n==1 :
      return 1
  else :
      return n*giaithua(n-1)

print(giaithua(5))




