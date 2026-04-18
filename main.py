import itertools

def generatsiya_kombinatsiyalari(n, r):
    return list(itertools.combinations(range(1, n+1), r))

n = int(input("N sonini kiriting: "))
r = int(input("R sonini kiriting: "))

kombinatsiyalar = generatsiya_kombinatsiyalari(n, r)
for kombinatsiya in kombinatsiyalar:
    print(kombinatsiya)
```

```python
import math

def generatsiya_kombinatsiyalari(n, r):
    kombinatsiya = math.comb(n, r)
    return kombinatsiya

n = int(input("N sonini kiriting: "))
r = int(input("R sonini kiriting: "))

kombinatsiya = generatsiya_kombinatsiyalari(n, r)
print(kombinatsiya)
