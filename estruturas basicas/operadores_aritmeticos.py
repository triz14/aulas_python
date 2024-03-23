#Fazendo comparação com operadores aritméticos
a = 2 == 3
b = 2 != 3
c = not 5 == 6
d = "d" not in "danilo"
e = 2 > 3 or 5 != 6
f = 2 == 3 and 2 < 3

print(a)
print(b)
print(c)

n1 = 2
n2 = 3

a = n1 > n2
print(f"A comparação {n1} > {n2} dá {a}")

a2 = n1 == n2
print(f"A comparação {n1} == {n2} dá {a2}")

a3 = n1 >= n2
print(f"A comparação {n1} >= {n2} dá {a3}")

a4 = n1 <= n2
print(f"A comparação {n1} <= {n2} dá {a4}")

a5 = n1 != n2
print(f"A comparação {n1} != {n2} dá {a5}")

a = 2
b = 3
c = 4
d = 5

print(f"A comparação {a}>{b} and {c}>{d}, ou seja, {a>b} and {c>d} dá {a>b and c>d}")
print(f"A comparação {a}<{b} and {c}>{d}, ou seja, {a<b} and {c>d} dá {a<b and c>d}")
print(f"A comparação {a}>{b} and {c}<{d}, ou seja, {a>b} and {c<d} dá {a>b and c<d}")
print(f"A comparação {a}<{b} and {c}<{d}, ou seja, {a<b} and {c<d} dá {a<b and c<d}")