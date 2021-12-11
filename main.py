num=9696
def rot(num1):
    if num1>9000: 
        num1=num1-9000
        if num1>900: 
            num1=num1-900
            if num1>90: 
                num1=num1-90
                if num1==9: 
                    print (9999)
                else:
                    print (9996)                   
            else:
                num1=num1-60
                if num1==9: 
                    print (9996)
                else:
                    print (9966)
        else:
            num1=num1-600
            if num1>90: 
                num1=num1-90
                if num1==9: 
                    print (9996)
                else:
                    print (9966)
            else:
                num1=num1-60
                if num1==9: 
                    print (9966)
                else:
                    print  (9666)
    else: 
        num1=num1-6000
        if num1>900: 
            num1=num1-900
            if num1>90: 
                num1=num1-90
                if num1==9: 
                    print (9996)
                else:
                    print (9696)
            else:
                num1=num1-60
                if num1==9: 
                    print (9669)
                else:
                    print (9666)
        else:
            num1=num1-600
            if num1>90: 
                num1=num1-90
                if num1==9: 
                    print (9696)
                else:
                    print  (6696)
            else:
                num1=num1-60
                if num1==9: 
                    print (9666)
                else:
                    print  (6666) 
rot(num)
