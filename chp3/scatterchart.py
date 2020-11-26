from matplotlib import pyplot as plt

friends = [70, 65, 72, 63, 71, 64, 60, 64, 67]
minutes = [175, 170, 205, 120, 220, 130, 105, 145, 190]
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']

plt.scatter(friends, minutes)

# 각 포인트에 레이블을 달자.
for label, friend_count, minute_count in zip(labels, friends, minutes):
    plt.annotate(label,
    xy = (friend_count, minute_count), # 레이블을 데이터 포인트 근처에 두되
    xytext=(5, -5),                    # 약간 떨어져 있게 하자.
    textcoords='offset points')
    
plt.title("Daily Minutes vs. Number of Friends")
plt.xlabel("# of friends")
plt.ylabel("daily minutes spent on the site")
plt.show()


# 변수들끼리 비교할 때 matplotlib이 자동으로 축의 범위를 설정하게 하면 그림과 같이 공정한 비교를 하지 못할 수 있다
test_1_grades = [ 99, 90, 85, 97, 80]
test_2_grades = [ 100, 85, 60, 90, 70]

plt.scatter(test_1_grades, test_2_grades)
plt.title("Axes Aren't Comparable")
plt.xlabel("test 1 grade")
plt.ylabel("test 2 grade")

# 여기서 plt.axis("equal")을 추가하면 공정한 비교가 됨
plt.axis("equal")
plt.show()

