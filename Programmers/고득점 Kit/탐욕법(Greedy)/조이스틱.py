def solution(name):
    # alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    # moves = []
    # answer = 0

    # for word in name:
    #     move = alphabet.index(word)
    #     if move > 13:
    #         move = len(alphabet) - move
    #     moves.append(move)

    # cnt = 0
    # max_cnt = 0
    # for i in moves:
    #     if i == 0:
    #         cnt += 1
    #         max_cnt = max(cnt,max_cnt)
    #     else:
    #         cnt = 0

    # answer = sum(moves) + len(name) - 1 - max_cnt
    # return answer

    answer = 0
    n = len(name)

    def alphabet_to_num(char):
        num_char = [i for i in range(14)] + [j for j in range(12, 0, -1)]
        return num_char[ord(char) - ord('A')]

    for ch in name:
        answer += alphabet_to_num(ch)

    move = n - 1

    for idx in range(n):
        next_idx = idx + 1
        while (next_idx < n) and (name[next_idx] == 'A'):   # 연속 A인 구간 건너뛰기
            next_idx += 1
        distance = min(idx, n - next_idx)   # 첨,끝에서의 거리 중 최소
        
        move = min(move, idx + n - next_idx + distance)
        # idx : 현재 위치
        # n - next_idx : 오른쪽 끝까지의 거리

    answer += move
    return answer

print(solution('AAAOEAAAN'))