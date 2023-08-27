def solution(phone_book):
    phone_book.sort()
    print(phone_book)
    for i in range(len(phone_book) - 1):
        prefix_len = len(phone_book[i])
        if phone_book[i + 1][:prefix_len] == phone_book[i]:
            answer = False
            break
        answer = True 
    return answer

print(solution(["12","123","1235","567","88"]))

# 다른 풀이

# def solution(phone_book):
#     answer = True
#     hash_map = {}
#     for phone_number in phone_book:
#         hash_map[phone_number] = 1
#     for phone_number in phone_book:
#         temp = ""
#         for number in phone_number:
#             temp += number
#             if temp in hash_map and temp != phone_number:
#                 answer = False
#     return answer