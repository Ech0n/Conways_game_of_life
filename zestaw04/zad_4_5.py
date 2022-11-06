def odwracanie(L,left,right):
    i = 0
    j = right-left
    while(j>i):
        swap = L[i+left]
        L[i+left] = L[j+left]
        L[j+left] = swap
        i+=1
        j-=1

def odwracanie_req(L,left,right):
    if(left>=right):
        return
    swap = L[left]
    L[left] = L[right]
    L[right] = swap
    odwracanie_req(L,left+1,right-1)

L =[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
odwracanie(L,4,14)
print(L)
odwracanie_req(L,9,12)
print(L)