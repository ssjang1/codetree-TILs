# s,q = input().split(' ')
# q = int(q)

# for i in range(q):
#     a,b,c = input().split(' ')
#     if a =='1':
#         b = int(b)
#         c = int(c)
#         check = list(s)
#         char1 = check[b-1]
#         char2 = check[c-1]
#         check[b-1] = char2 
#         check[c-1] = char1

#         result = ''.join(check)
#         print(result)
#     elif a=='2':
#         result = s.replace(b,c)
#         print(result)

# 입력 받기
s, q = input().split()
q = int(q)

# 질의 처리
for _ in range(q):
    query = input().split()
    if query[0] == '1':  # 1번 명령: 문자 교환
        a, b = int(query[1]), int(query[2])
        # 문자열을 리스트로 변환하여 문자 교환 수행
        s_list = list(s)
        s_list[a-1], s_list[b-1] = s_list[b-1], s_list[a-1]
        s = ''.join(s_list)  # 다시 문자열로 변환
    elif query[0] == '2':  # 2번 명령: 문자 치환
        old_char, new_char = query[1], query[2]
        s = s.replace(old_char, new_char)  # 모든 old_char를 new_char로 변경
    print(s)  # 결과 출력
