n = int(input())
matrix = []
for i in range(n):
    matrix.append(list(map(int,input().split())))
event = []
for i,j in matrix:
    event.append((i,1))
    event.append((j,-1))
event.sort(key=lambda x:x[0])
alive = 0
year_pop = {}
for year,pop in event:
    alive+=pop
    year_pop[year] = alive
max_p = max(year_pop.values())
for year,popu in year_pop.items():
    if(popu==max_p):
        print(year)
        break
