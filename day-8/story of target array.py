import sys

data = []
for line in sys.stdin:
    data.append(line.rstrip("\n"))

flat_inputs = []
for line in data:
    flat_inputs.extend(list(map(int, line.split())))

a = flat_inputs[0]
b = flat_inputs[1]
v = flat_inputs[2:a + 2]
i = flat_inputs[a + 2:2 * a + 2]

final_lst = []
for j in range(a):
    final_lst.insert(i[j], v[j])
print(*final_lst)
