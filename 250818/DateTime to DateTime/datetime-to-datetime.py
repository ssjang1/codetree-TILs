a, b, c = map(int, input().split())

# Please write your code here.

m_sum = a * 24 * 60 + b *60 + c
m_standard = 11 * 24 * 60 + 11 * 60 + 11

if m_sum >= m_standard:
    print(m_sum-m_standard)
else:
    print(-1)