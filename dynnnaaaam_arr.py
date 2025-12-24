import ctypes
import math
import matplotlib.pyplot as plt

class DynamicArray:
    def __init__(self, strategy_type, initial_capacity=8, my_number=5):
        self.n = 0 
        self.capacity = initial_capacity
        self.strategy_type = strategy_type
        self.my_number = my_number
        self.resize_count = 0
        self.A = (self.capacity * ctypes.py_object)() 

    def append(self, obj):
        if self.n == self.capacity:
            self._resize(self._get_new_capacity())
        self.A[self.n] = obj
        self.n += 1

    def _get_new_capacity(self):
        if self.strategy_type == 1: 
            return self.capacity * 2
        elif self.strategy_type == 2: 
            factor = 1 + self.my_number / 10
            return math.ceil(self.capacity * factor)
        elif self.strategy_type == 3: 
            factor = 1 + (self.my_number / 10) / math.log2(self.n + 2)
            return math.ceil(self.capacity * factor)

    def _resize(self, new_cap):
        B = (new_cap * ctypes.py_object)()
        for k in range(self.n):
            B[k] = self.A[k]
        self.A = B
        self.capacity = new_cap
        self.resize_count += 1


MY_NUMBER = 8 
limit = 1000000
strategies = [1, 2, 3]
final_results = {}

for s in strategies:
    arr = DynamicArray(strategy_type=s, initial_capacity=8, my_number=MY_NUMBER)
    unused_history = []
    
    for i in range(limit):
        arr.append(i)

        unused_history.append((arr.capacity - arr.n) / arr.capacity * 100)
    
    final_results[s] = {
        'resizes': arr.resize_count,
        'history': unused_history
    }


plt.figure(figsize=(10, 6))
for s in strategies:
    plt.plot(final_results[s]['history'], label=f'Стратегія {s} (Resizes: {final_results[s]["resizes"]})')

plt.title(f'Аналіз стратегій зростання (Мій номер: {MY_NUMBER})')
plt.xlabel('Кількість елементів в масиві')
plt.ylabel('Частка невикористаної пам’яті (%)')
plt.legend()
plt.grid(True)
plt.show()

