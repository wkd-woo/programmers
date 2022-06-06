def solution(phone_book): # 정렬 풀이
    phone_book.sort(key=lambda x: (x, len(x)) )
    for i, num in enumerate(phone_book[:-1]):
        if phone_book[i+1].startswith(phone_book[i]):
            return False
        
    return True


def solution(phone_book): # 출제 의도
    answer = True
    hash_map = {}
    for phone_number in phone_book:
        hash_map[phone_number] = 1
        
    for phone_number in phone_book:
        temp = ""
        for number in phone_number:
            temp += number
            if temp in hash_map and temp != phone_number:
                answer = False
                
    return answer
