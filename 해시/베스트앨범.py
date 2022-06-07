def solution(genres, plays):
    answer = []
    genres_plays = {}
    greatest = {}
    for i, (genre, play) in enumerate(zip(genres, plays)):
        if genre not in genres_plays:
            genres_plays[genre] = 0
        genres_plays[genre] += play
        if genre not in greatest:
            greatest[genre] = []
        greatest[genre].append((i, play))
    
    for key, value in greatest.items():
        greatest[key].sort(key=lambda x:(x[1]), reverse=True) 
    
    genres_plays = sorted(genres_plays.items(), key=lambda item: item[1], reverse=True)
    for key, value in genres_plays:
        temp = []
        for idx, play in greatest[key][:2]:
            temp.append(idx)
        answer += temp
        
    return answer