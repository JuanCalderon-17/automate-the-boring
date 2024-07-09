import sys, time
indent = 0 #how many spaces to indent 
indentIncreasing = True #indent increasing

try:
    while True:
        print(' ' * indent, end='')
        print('*******')
        time.sleep(0.1) #pause for 1/10 of a second

        
        if indentIncreasing:
            indent =+ 1
            if indent == 20:
                #change directions
                indentIncreasing = False 

        else:
            #decrease number of spaces 
            indent =- 1
            if indent == 0:
                indentIncreasing = True 


except KeyboardInterrupt:
    sys.exit('error brother')
