x = int(input("Enter:- "))
is_negative = x<0
x = abs(x)
list1 = list(map(int,str(x)))
list1.reverse()
a = int("".join(map(str,list1)))
if is_negative:      
    print(-a)
else:
    print(a)