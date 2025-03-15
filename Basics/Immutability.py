#Fundamental Data Type is python are immutable
x = 10
#Here x is the Reference variable for object 10
print(id(x)) # Here we can chek the id of the obj
x = x  + 1
#Here we are performing changes in the onj. 
#What will happen here is the new obj will be created and now my reference variable x is pointing
#to the new obj 11 and obh(10) is now eligible for garbage collection.
print(id(x))
