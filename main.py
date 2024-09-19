my_dict = {'Dima':1989, 'Aleksey':1983}
print(my_dict)
print(my_dict.get('Dima'))
print (my_dict.get('Sergey'))
my_dict.update({'Max': 1986, 'Andrey': 1985})
a = my_dict.pop('Aleksey')
print(a)
print(my_dict)

my_set = {1, 3, 5, 7, 1, 3, 5, 'Car', False, (123, 321, 231)}
print(my_set)
my_set.add(10)
my_set.add(11)
my_set.remove('Car')
print(my_set)