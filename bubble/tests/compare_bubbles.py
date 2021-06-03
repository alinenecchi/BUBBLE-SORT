import pandas as pd
import random
from sorting import bubble_sort, shortbubble_sort

list_a = random.sample(range(1, 999), 50) #50
list_b = random.sample(range(1, 999), 100) #100
list_c = random.sample(range(1, 9999), 1000) #1mil
list_d = random.sample(range(1, 9999), 5000) #5mil
list_e = random.sample(range(1, 99999), 10000) #10mil

bubble_a = list_a.copy()
bubble_b = list_b.copy()
bubble_c = list_c.copy()
bubble_d = list_d.copy()
bubble_e = list_e.copy()

shortbubble_a = list_a.copy()
shortbubble_b = list_b.copy()
shortbubble_c = list_c.copy()
shortbubble_d = list_d.copy()
shortbubble_e = list_e.copy()

coluna_a = []
coluna_b = []
coluna_c = []
coluna_d = []
coluna_e = []

coluna_a.append(bubble_sort(bubble_a))
coluna_b.append(bubble_sort(bubble_b))
coluna_c.append(bubble_sort(bubble_c))
coluna_d.append(bubble_sort(bubble_d))
coluna_e.append(bubble_sort(bubble_e))

coluna_a.append(shortbubble_sort(shortbubble_a))
coluna_b.append(shortbubble_sort(shortbubble_b))
coluna_c.append(shortbubble_sort(shortbubble_c))
coluna_d.append(shortbubble_sort(shortbubble_d))
coluna_e.append(shortbubble_sort(shortbubble_e))

data = {
    'Algoritmo' : ['BubbleSort', 'ShortBubbleSort'],
    '50': coluna_a,
    '100': coluna_b,
    '1.000': coluna_c,
    '5.000': coluna_d,
    '10.000': coluna_e,
}
df = pd.DataFrame(data)

with pd.ExcelWriter('tests/compare.xlsx', mode='a') as file:
    df.to_excel(file, sheet_name='compare_bubbles')

print('Operações realizadas com sucesso!!')