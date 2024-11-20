

list_tupple = [
    ('age','plage','name'),
    ('longon','birmingam','berlin')
    ]


one = " ".join([line_one for line_one in list_tupple[0]])

print(one)
numbers = [23,54,12,54,2,4,6,34,72,34,79,]

my_numbers = [number for number in numbers if number < 60]
print(my_numbers)

countries = {
    'germany':'beriln',
    'romaina':'bucuresti',
    'italiy':'rome'
    }


countries = " ".join([capital for capital in countries.values() if capital != 'rome'])
print(countries)



