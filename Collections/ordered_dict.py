from collections import OrderedDict

d = OrderedDict()
for _ in range(int(input())):
    prod_name, space, price = input().rpartition(' ')
    d[prod_name] = d.get(prod_name, 0) + int(price)
for i, p in d.items():
    print(i, p)
