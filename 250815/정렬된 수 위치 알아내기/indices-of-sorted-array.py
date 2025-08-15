n = int(input())
sequence = list(map(int, input().split()))

# Please write your code here.

seq_with_num = [] 
for i in range(len(sequence)):
    seq_with_num.append((sequence[i],i+1))

seq_with_num.sort(key = lambda x:(x[0],x[1]))

new_seq = [t + (i+1,) for i, t in enumerate(seq_with_num)]

new_seq.sort(key=lambda x:x[1])
for elem in new_seq:
    print(elem[-1], end=' ')
