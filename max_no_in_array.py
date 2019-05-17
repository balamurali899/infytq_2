def find_max(num1, num2):
    max_num=-1
    list=[]
    for i in range(num1,num2+1):
        list.append(i)
    
    if(num1<num2):
        list1=[]
        for i in list:
            temp=i
            sum=0
            if(i//100==0):
                while(i>0):
                   rem=i%10
                   sum=sum+rem
                   i=i//10
                if(sum%3==0 and temp%5==0):                       
                    list1.append(temp)                
    max_num=max(list1)                
    return max_num
max_num=find_max(10,60)
print(max_num)
