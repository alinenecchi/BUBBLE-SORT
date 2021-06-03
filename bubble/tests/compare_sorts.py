import pandas as pd
import random
from sorting import selection_sort, bubble_sort, insertion_sort
from sorting import merge_sort, quick_sort

list_a = random.sample(range(1, 999), 50) #50
list_b = random.sample(range(1, 999), 100) #100
list_c = random.sample(range(1, 9999), 1000) #1mil
list_d = random.sample(range(1, 9999), 5000) #5mil
list_e = random.sample(range(1, 99999), 10000) #10mil
list_f = random.sample(range(1, 99999), 50000) #50mil
list_g = random.sample(range(1, 999999), 100000) #100mil

bubble_a = list_a.copy()
bubble_b = list_b.copy()
bubble_c = list_c.copy()
bubble_d = list_d.copy()
bubble_e = list_e.copy()
bubble_f = list_f.copy()
bubble_g = list_g.copy()

insertion_a = list_a.copy()
insertion_b = list_b.copy()
insertion_c = list_c.copy()
insertion_d = list_d.copy()
insertion_e = list_e.copy()
insertion_f = list_f.copy()
insertion_g = list_g.copy()

selection_a = list_a.copy()
selection_b = list_b.copy()
selection_c = list_c.copy()
selection_d = list_d.copy()
selection_e = list_e.copy()
selection_f = list_f.copy()
selection_g = list_g.copy()

quick_a = list_a.copy()
quick_b = list_b.copy()
quick_c = list_c.copy()
quick_d = list_d.copy()
quick_e = list_e.copy()
quick_f = list_f.copy()
quick_g = list_g.copy()

merge_a = list_a.copy()
merge_b = list_b.copy()
merge_c = list_c.copy()
merge_d = list_d.copy()
merge_e = list_e.copy()
merge_f = list_f.copy()
merge_g = list_g.copy()

coluna_a = []
coluna_b = []
coluna_c = []
coluna_d = []
coluna_e = []
coluna_f = []
coluna_g = []

coluna_a.append(bubble_sort(bubble_a))
coluna_a.append(insertion_sort(insertion_a))
coluna_a.append(selection_sort(selection_a))
coluna_a.append(quick_sort(quick_a))
coluna_a.append(merge_sort(merge_a))

coluna_b.append(bubble_sort(bubble_b))
coluna_b.append(insertion_sort(insertion_b))
coluna_b.append(selection_sort(selection_b))
coluna_b.append(quick_sort(quick_b))
coluna_b.append(merge_sort(merge_b))

coluna_c.append(bubble_sort(bubble_c))
coluna_c.append(insertion_sort(insertion_c))
coluna_c.append(selection_sort(selection_c))
coluna_c.append(quick_sort(quick_c))
coluna_c.append(merge_sort(merge_c))

coluna_d.append(bubble_sort(bubble_d))
coluna_d.append(insertion_sort(insertion_d))
coluna_d.append(selection_sort(selection_d))
coluna_d.append(quick_sort(quick_d))
coluna_d.append(merge_sort(merge_d))


coluna_e.append(bubble_sort(bubble_e))
coluna_e.append(insertion_sort(insertion_e))
coluna_e.append(selection_sort(selection_e))
coluna_e.append(quick_sort(quick_e))
coluna_e.append(merge_sort(merge_e))

coluna_f.append(bubble_sort(bubble_f))
coluna_f.append(insertion_sort(insertion_f))
coluna_f.append(selection_sort(selection_f))
coluna_f.append(quick_sort(quick_f))
coluna_f.append(merge_sort(merge_f))

coluna_g.append(bubble_sort(bubble_g))
coluna_g.append(insertion_sort(insertion_g))
coluna_g.append(selection_sort(selection_g))
coluna_g.append(quick_sort(quick_g))
coluna_g.append(merge_sort(merge_g))

data = {
    'Algoritmo' : ['Bubble', 'Insertion', 'Selection', 'Quick', 'Merge'],
    '50': coluna_a,
    '100': coluna_b,
    '1.000': coluna_c,
    '5.000': coluna_d,
    '10.000': coluna_e,
    '50.000': coluna_f,
    '100.000': coluna_g,
}
df = pd.DataFrame(data)

with pd.ExcelWriter('tests/compare.xlsx', mode='a') as file:
    df.to_excel(file, sheet_name='compare_sort')

print('Operações realizadas com sucesso!!')
