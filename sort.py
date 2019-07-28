#插入排序
lista=[1,40,12,25,78,8,9,18]
def insert_sort(list):
    for i in range(1,len(list)):
        key=list[i]
        j=i-1
        while( j>0  and list[j]>key):
            list[j+1]=list[j]
            j-=1
        list[j+1]=key
    return list
#归并排序
def merge_sort(list):
    if len(list)<=1:
        return list
    mid=len(list)//2
    left=merge_sort(list[:mid])
    right=merge_sort(list[mid:])
    return merge(left,right)
def merge( left,right):
    i,j=0,0
    result=[]
    while(i<len(left) and j<len(right)):
        if left[i]<right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
    result+=left[i:]
    result += right[j:]
    return result
#选择排序
def select_sort(list):
    for i in range(len(list)):
        a=list[i]
        for j in range(i,len(list)):
            if list[j]<list[i]:
                temp=list[i]
                list[i]=list[j]
                list[j]=temp
    return list
#冒泡排序
def bubble_sort(list):
    for i in range(1,len(list)):
        for j in range(len(list)-i):
            if list[j]>list[j+1] :
                temp = list[j+1]
                list[j+1] = list[j]
                list[j] = temp
    return list
#希尔排序
def shell_sort(list):
    grap=len(list)//2
    while grap>=1:
        for i in range(grap,len(list)):
            j=i-grap
            while j>=0 and list[j]>list[i]:
                list[j+grap]=list[j]
                j-=grap



