class MyList(list):
    def sort(self, num,reverse=False):
        for i in range(0,len(num)):
            min = i
            for x in range(i+1,len(num)):
                if reverse==True:
                    if num[min]> num[x]:
                        min = x
                else:
                    if num[min]<num[x]:
                        min = x
            num[i],num[min]=num[min],num[i] 
        return num
    

list=[5,8,1,3,9,7]
list1 =  MyList()
print(list1.sort(list,True))
print(list1.sort(list,0))