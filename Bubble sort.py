
cisla=[1,3,6,4,5,2,8,9,7]
x=0

def bubble_sort(val):
    change=True
    while change:
        change=False
        for i in range(len(val)-1):
            if val[i]>val[i+1]:
                x,val[i]=val[i],x
                change=True
    return val
print(bubble_sort(cisla))
