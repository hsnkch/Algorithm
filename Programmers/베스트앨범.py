# 재생횟수가 같은 경우에서 오류 발생
# def solution(genres, plays):
#     answer = []
#     dic = {}    # 장르당 재생 횟수 저장
#     idx_dic = {}    # 고유 번호, 재생 횟수 저장

#     for i in range(len(plays)):
#         idx_dic[plays[i]] = i

#     for i in range(len(genres)):
#         dic[genres[i]] = []
#         for j in range(len(genres)):
#             if genres[i] == genres[j]:
#                 dic[genres[i]].append(plays[j])

#     for key in dic:
#         dic[key] = sorted(dic[key], reverse=True)
    

#     total_plays = {}
#     for i in dic:
#         total_plays[i] = sum(dic[i])

#     total_plays = sorted(total_plays.items(), key=lambda x: x[1], reverse=True)
#     dic = list(dic.items())
#     dic = sorted(dic, key = lambda x: sum(x[1]), reverse=True)

#     for i in range(len(dic)):
#         if len(dic[i][1]) > 2:
#             for j in range(2):
#                 answer.append(idx_dic[dic[i][1][j]])
#         else:
#             for j in range(len(dic[i][1])):
#                 answer.append(idx_dic[dic[i][1][j]])
#     return answer
    


def solution(genres, plays):
    answer = []
    genre_play = {}  # 장르별 총 재생 횟수를 저장하는 딕셔너리
    song_play = {}   # 곡의 재생 횟수와 고유 번호를 저장하는 딕셔너리
    
    # 각 장르와 곡에 대한 정보를 딕셔너리에 저장
    for i in range(len(genres)):
        genre = genres[i]
        play = plays[i]
        song_play[i] = (play, genre)
        genre_play[genre] = genre_play.get(genre, 0) + play
    
    # 장르별 총 재생 횟수를 내림차순으로 정렬
    sorted_genre_play = sorted(genre_play.items(), key=lambda x: x[1], reverse=True)
    print(sorted_genre_play)
    print(song_play)
    
    # 장르별로 가장 많이 재생된 곡을 두 개씩 선택
    for genre, _ in sorted_genre_play:
        # genre_songs = [song for song, (play, g) in song_play.items() if g == genre]
        genre_songs = []
        for song, (play, g) in song_play.items():
            if g == genre:
                genre_songs.append(song)
        genre_songs = sorted(genre_songs, key=lambda x: (song_play[x][0], -x), reverse=True)
        answer.extend(genre_songs[:2])
    
    return answer


print(solution(["classic", "pop", "classic", "classic", "pop"],[500, 600, 150, 800, 2500]))