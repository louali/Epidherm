from task3 import FilterMaterials
from task2 import GroupByFam

mat = [
    {
        'name':'material4',
        'family': {'id':1, 'name':'family1'},
        'details': {'masse_surfacique':10, 'masse_combustible':90}
    },
    {
        'name':'material3',
        'family': {'id':1, 'name':'family1'},
        'details': {'masse_surfacique':100, 'masse_combustible':25},
    },
    {
        'name':'material1',
        'family': {'id':1, 'name':'family1'},
        'details': {'masse_surfacique':10, 'masse_combustible':20}
    },
    {
        'name':'material2',
        'family': {'id':2, 'name':'family2'},
        'details': {'masse_surfacique':15, 'masse_combustible':30},
    }
]

print(FilterMaterials(mat))
print('&')
print(GroupByFam(mat))