#1-Bir listeyi düzleştiren (flatten) fonksiyon yazın. Elemanları birden çok katmanlı listelerden ([[3],2] gibi) oluşabileceği gibi, non-scalar verilerden de oluşabilir.
#2-Verilen listenin içindeki elemanları tersine döndüren bir fonksiyon yazın. Eğer listenin içindeki elemanlar da liste içeriyorsa onların elemanlarını da tersine döndürün.
l=[[1,'a',['cat'],2],[[[3]],'dog'],4,5]
flattened_l=[]
def flatten_l(lst):
    for i in lst:
        if isinstance(i,list):
            flatten_l(i)
        else:
             flattened_l.append(i)
flatten_l(l)
print(flattened_l)                

x = flattened_l

def new_lst(l1):
    l1=[str(i)for i in l1]
    l1.reverse()
    return l1
result = new_lst(x)
print(result)    