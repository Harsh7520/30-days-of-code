n = int(input())
a = list(map(int, input().split()))
mini = min(a)
minii = a.index(mini)
s_a = a[minii:]
m_s_a = max(s_a)
if(m_s_a>=mini):
    print(m_s_a-mini)
else:
    print(0)
