print '          W A I T E D    A V E R A G E    C A L C U L A T O R    '

class Error(Exception):
    pass
class Incorrectstring(Error):
    pass
class Incorrectinteger(Error):
    pass

        
try:
    name = raw_input("enter name  ")
    while name.isalpha() != True:
            raise Incorrectstring
except Incorrectstring:
        while name.isalpha() != True:
                print 'Enter a valid name'
                name = raw_input("enter name  ")
        


reg_num = raw_input("enter registration number  ")


while True:
    
#num = None
    try:
        num = int(input('enter number of courses  '))
        if type(num) == int:
            break
#except  NameError:
#    while type(num) != int:
#        print 'please enter integer value'
#        num = input('Enter number of courses ')
#        #print "type of num is ",type(num)
    except :
        pass
    print "INVALID INPUT"
    

total = 0
units = 0


for i in range(num):
    
    course_code = raw_input("enter course title   ")
    score = input('enter score   ')
    unit  = input('enter unit   ')
    while unit >5 :
        print 'unit limit exceed, enter a new one'
        unit  = input('enter unit   ')
    total +=score * unit
    units += unit

average = total/units
ave = float(average)


print name, 'your waited average is ', ave
