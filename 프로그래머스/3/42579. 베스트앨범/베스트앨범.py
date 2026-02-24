def solution(genres, plays):
    answer = []
    plays_dict = {}
    total_dict = {}
    
    for i in range(len(genres)):
        if genres[i] not in plays_dict:
            plays_dict[genres[i]] = [[plays[i], i]]
            total_dict[genres[i]] = plays[i]
        else:
            plays_dict[genres[i]].append([plays[i], i])
            total_dict[genres[i]] += plays[i]
    
    genre_order = sorted(total_dict, key=total_dict.get, reverse=True)
    for genre in genre_order:
        songs = plays_dict[genre]
        songs.sort(key=lambda x:x[0], reverse=True)
        for play, idx in songs[:2]:
            answer.append(idx)
        
    return answer