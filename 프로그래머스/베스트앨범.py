genres =["classic", "pop","classic" ]
plays = [500, 600,140]	

def solution(genres,plays):
    result = []
    dict_genres = {}
    genres_order = {}
    played = [[]for _ in range(100)]
    count = 0
    
    for x in range(len(genres)):
        if genres[x] not in dict_genres:
            dict_genres[genres[x]] = plays[x]
            genres_order[genres[x]] = count
            count+=1
        else:
            dict_genres[genres[x]] += plays[x]
        index = genres_order[genres[x]]
        played[index].append([plays[x],x])
        played[index].sort(key = lambda x :x[1])
        played[index].sort(key = lambda x :-x[0])
        played[index] = played[index][:2]
    
    while count != 0:
        now = max(dict_genres,key=dict_genres.get)
        index = genres_order[now]
        if len(played[index]) == 1:
            result.append(played[index][0][1])
        else:
            result.append(played[index][0][1])
            result.append(played[index][1][1])
        dict_genres.pop(now)
        count-=1
        
    return result

print(solution(genres,plays))