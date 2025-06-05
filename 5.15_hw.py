# amount = int(input("每天卖了多少碗："))
# price = float (input("每碗多少钱："))
# days = int(input("今年营业了多少天："))
# money = amount * price * days
# print(f"今年营业额是{money}元")


# a = 0
# sum =0
# while (a<=100):
#     if a%3==0 :
#       sum+=a
#     a+=1
# print (sum)



# a = 0
# sum =0
# while (a<=100):
#     if a%3==0 and a%5==0:
#       sum+=a
#     a+=1
# print (sum)

      
# a=0
# while(a<=5):
#     print("*"*a)
#     a+=1



# a=5
# while(a>=1):
#     print("*"*a)
#     a-=1

# a=1
# sum =0
# while(a<=5):
#     sum+=1/a
#     a+=1
# print (sum)


for a in range(1,10) :
    for b in range(1,a+1) :
        print(f"{a}*{b}=",a*b,sep="",end=" ")
    print()


# number1 = int(input("请输入数字:"))
# sum = 0
# c=int(bin(number1)[2:])
# while(c>=1):
#     print(c)
#     if(c%10==1):
#         sum+=1
#     c = c//10
# print(sum)



# a = 1
# sum = 0
# while(a<101):
#     sum+=a
#     a+=1
# print(sum)

# a = 1
# sum = 0
# while(a<101):
#     if(a%2==1):
#         sum+=a
#     a+=1
# print(sum)


# number1 = int(input("请输入数字:"))
# a = 0
# number2 = 0
# while number1 >=1:
#     print(number1)
#     a = number1 %10
#     number2 = a+number2*10
#     number1=number1//10
# print(number2)