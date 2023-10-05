def solution(book_time):
    answer = 0
    time = []
    chk = [0] * len(book_time)
    for i in range(len(book_time)):
        start = int(book_time[i][0][:2])*60 + int(book_time[i][0][3:])
        end = int(book_time[i][1][:2])*60 + int(book_time[i][1][3:])
        time.append([start, end+10])

    time.sort(key=lambda x: (x[1], x[0]))
    for i in range(len(time)):
        tmp = 0
        for j in range(len(time)):
            if time[j][0] < time[i][1] <= time[j][1]:
                tmp += 1
        chk[i] = tmp


    return max(chk)
print(solution([["15:00", "17:00"], ["16:40", "18:20"], ["14:20", "15:20"], ["14:10", "19:20"], ["18:20", "21:20"]]))