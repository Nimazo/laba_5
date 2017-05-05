

a = [1,2,3,4,5,1,1,2,3]
a1 = [6,7,8]
print('list: ',' '.join([str(i) for i in a]))
print('Введите удаляемый элемент: '),
n = int(input())
a.remove(n)
print('list1 с удаленным элементом:',' '.join([str(i) for i in a]))

print('Введите номер элемента с которого будем удалять из list1:')
n = int(input())
print('Введите количество удаляемых элементов из list 1: ')
k = int(input())
n = a.index(n)
for i in range(k):
    a.remove(a[n])
print('lisr1 после удаления:',' '.join([str(i) for i in a]))

print('list2: ',' '.join([str(i) for i in a1]))

a.extend(a1)
a.sort()
print('Объеденили list2 в list1: ', ' '.join([str(i) for i in a]))
    
    
