#1 Arithmetic operators 
print('ARITHMETIC OPERATORS')
num1= 10
num2 = 5
print('num1= 10')
print('num2 = 5')
print("addition of num1+num2;", num1+num2)
print('substraction of num1-num2;',num1-num2)
print('multiplication of num1*num2;',num1*num2)
print('division of num1/num2;',num1/num2)
print('modulus ofnum1%num2;',num1%num2)
print('exponentiation of num1**num2;',num1**num2)
print('floor divsion of num1//num2;',num1//num2)
#2 Assignment operators
print('ASSIGNMENT OPERATORS')
num1=2 
num1 += 1
print('num1=2 num1 += 1 value of num1;',num1)
num2=2
num2-=1
print('num2=2 num2-=1 value of num2;',num2)
num3=2
num3*=2
print('num3=2 num3*= 1 value of num3;',num3)
num4=20
num4/=5
print('num4=20 num4/=5 value of num4;',num4)
num5=8
num5%=5
print('num5=8 num5%=5 value of num5;',num5)
num6=20
num6//=2
print('num6=20 num6//=2 value of num6;',num6)
num7=2
num7**=3
print('num7=2 num7**=3 value of num7;',num7)
num8=5
num8&=2
print('num8=5 num8&=2 value of num8;',num8)
num9=2
num9|=5
print('num9=2  num9|=5 value of num9;',num9)
num10=2
num10^=3
print('num10=2 num10^=3 value of num10;',num10)
num11=2
num11>>=4
print('num11=2 num11>>=4 value of num11;',num11)
num12=2
num12<<=3
print('num12=2 num12<<=3 value of num12;',num12)
#3 comparison operators 
print('COMPARISON OPERATORS') 
num1=10
num2=20
print('num1=10')
print('num2=20')
print('num1==num2 is',num1==num2)
print('num1!=num2 is',num1!=num2)
print('num1>num2 is',num1>num2)
print('num1<num2 is',num1<num2)
print('num1>=num2 is',num1>=num2)
print('num1<=num2 is',num1<=num2)
       # 4 python logical operators
print('PYTHON LOGICAL OPERATORS')
print('the num1<15 and num2>15 is',num1<15 and num2>15) #and returns true if both statements are true
print('the num1<15 or num2>15 is',num1<15 or num2>15) #and returns true if one statements are true
print('the not(num1<15 and num2>15) is',not(num1<15 and num2>15))# it gives reverse value ,if result is true it gives false
#5 python identity operators
print('PYTHON IDENTITY OPERATORS')
z=['aaa','bbb','ccc']
q=['aaa','bbb','ccc']
t=z
print('z=',str(z))
print('q=',str(q))
print('z=q')
print('the z is q',z is q)
print('the z is not q',z is not q) 
print('the t is z',t is z)
print('the z==q',z==q)
print('the z!=q',z!=q)
print('the z==t',z==t)
#6 python membership operators
print('PYTHON MEMBERSHIP OPERATORS')
x=["car","bike"]
w=("car")
print('x',str(x))
print('w',str(w))
print('the w in x is',w in x)
print('the ship not in x is','ship' not in x)
#7  python bitwise operators
print('PYTHON BITWISE OPERATORS')
print('the 1&2 bitwise and is',1&2)#bitwise and
print('the 1|2 bitwsie or is',1|2)#bitwsie or
print('the 1^2 bitwise xor is',1^2)#bitwise xor
print('the ~2 inverts bit is',~2)#inverts bit
print('the 3>>4 bitwise right shift is',3>>4)#bitwise right shift
print('the 8<<1 bitwise left shift is',8<<1)#bitwise left shift
