#SELECTION SORT 
n=int(input('Quanti numeri vuoi inserire? '))
lst=[]


#FUNZIONE CHE GENERA UNA LISTA CON I NUMERI PRESI IN INPUT
for i in range(n):
    numero=int(input('Inserisci un numero '))
    lst.append(numero)

# FUNZIONE SELECTION SORT

def selection_sort(lst2):
    for i in range(0,len(lst2)-1):
        p = 0
        min_value = lst2[-1]
        for j in range(i,len(lst2)): #j tutti gli elementi 
            if lst2[j]>min_value:
                p=j
        lst2[i],lst2[p] = lst2[p],lst[i]
selection_sort(lst)
print(lst)




        