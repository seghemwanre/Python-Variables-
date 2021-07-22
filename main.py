'''
Variable Assignment 
'''

# add 'Solomon' to the Variable 'name'
#name = "Solomon"
#print (name)

#===========================

#assign same value to multiply variables on the same line 
#a = b = c = 'cat'
#print (a)
#print (b)
#print (c)

#===========================

#reuse variable name, the last assignment is printed 

# colour = 'Red' 
# colour = 'Blue'
# print (colour)

#===========================

#Legalnames
# firstname = 'Solomon'
# first_name = 'Solomon'
# _firs_tname = 'Solomon'
# firstName = 'Solomon'
# firstname2 = 'Solomon'
#FIRSTNAME = 'Solomon'

#Illegalnames
#2firstname = 'Solomon'
#first-name = 'Solomon'
#first name = 'Solomon'

#===========================

'''
Reserved keywords
'''
#help ('keywords')
#if = 'love'
#print (if )

#===========================

#variable types 
#var = 27
#print (type (var))


'''
Object Identity 
'''
#score = 400 
#identity = id(score)
#print (identity)

#===========================
#score variable is saved into the pb by reference 

#score = 400
#pb = score 
#print (id(score))
#print (id(pb))

#both score and pb point to the same object 
# score -------------> int 100 <------------pb
#score = 100 
#pb = score 
#print (type(score))
#print (type(pb))
#print (score)
#print (pb)

#===========================
# pb --------------------------> int 20 
# score------------------------> into 100 
#pb =20 
#score = 100 
#print (type(score)) 
#print (type(pb))
#print (score)
#print (pb)

#===========================
#garbage collection 
# pb --------------------------> int 20 
# score -----------------------> str 'completed' 
#          -----------------> int 100
pb = 20 
score = 100 
score = 'completed'
print (type(score))
print (type(pb))
print (score)
print (pb)

