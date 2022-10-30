a = "acddbacbabibabcbabccggh"
b = "blcacffhccbacabcbbabcbab"

seta = set(a)
setb = set(b)

print("Elementy wystepujace w obu sekwencjach jednoczesnie: "+str(seta.intersection(setb))+"\nElementy wystepujace w obu sekwencjach: "+str(seta.union(setb)))
