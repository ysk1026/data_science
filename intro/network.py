from collections import Counter

users = [
    { "id": 0, "name": "Hero"},
    { "id": 1, "name": "Dunn"},
    { "id": 2, "name": "Sue"},
    { "id": 3, "name": "Chi"},
    { "id": 4, "name": "Thor"},
    { "id": 5, "name": "Clive"},
    { "id": 6, "name": "Hicks"},
    { "id": 7, "name": "Devin"},
    { "id": 8, "name": "Kate"},
    { "id": 9, "name": "Klein"},
]

friendship_pairs = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4),
                    (4, 5), (5, 6), (6, 8), (7, 8), (8, 9)]

friendships = { user["id"] : [] for user in users }
print(friendships)

for i, j in friendship_pairs:
    friendships[i].append(j)
    friendships[j].append(i)
    
print(friendships)

def number_of_friends(user):
    """user의 친구는 몇 명일까?"""
    user_id = user["id"]
    friend_ids = friendships[user_id]
    return len(friend_ids)

total_connections = sum(number_of_friends(user) for user in users) # 24
num_users = len(users) # 총 사용자 리스트의 길이
avg_connections = total_connections / num_users # 24 / 10 == 2.4

# (user_id, number_of_friends) 로 구성된 리스트 생성
num_friends_by_id = [(user["id"], number_of_friends(user)) for user in users]

num_friends_by_id.sort(                     # 정렬해 보자.
    key=lambda id_and_friends: id_and_friends[1], # num_friends 기준으로
    reverse=True)                                 # 제일 큰 숫자부터 제일 작은 숫자순으로

print("연결 차수가 반영된 데이텀 네트워크")
print(num_friends_by_id)

def foaf_ids_bad(user):
    # "foaf"는 친구의 친구 ("friend of a friend")를 의미하는 약자다.
    return [foaf_id
            for friend_id in friendships[user["id"]]
            for foaf_id in friendships[friend_id]]

print(foaf_ids_bad(users[0]))

def friends_of_friends(user):
    user_id = user["id"]
    return Counter(
        foaf_id
        for friend_id in friendships[user_id] # 사용자의 친구 개개인에 대해
        for foaf_id in friendships[friend_id] # 그들의 친구들을 세어 보고
        if foaf_id != user_id                 # 사용자 자신과
        and foaf_id not in friendships[user_id] # 사용자의 친구는 제외
    )
    
print(friends_of_friends(users[3])) # id 3은 0과 함께 아는 친구가 2명, 5와 함께 아는 친구가 1명
