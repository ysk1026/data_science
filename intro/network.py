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

