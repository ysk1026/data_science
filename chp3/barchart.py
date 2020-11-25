from matplotlib import pyplot as plt

movies = ["Annie Hall", "Ben-Hur", "Casablanca", "Gandhi", "West Side Story"]
num_oscars = [5, 11, 3, 8, 10]

# 막대의 x 좌표는 [0, 1 ,2 ,3 ,4], y 좌표는 [num_oscars]로 설정
plt.bar(range(len(movies)), num_oscars)

plt.title("My Favorite Movies") # 제목을 추가
plt.ylabel("# of Academy Awards") # y축에 레이블을 추가하자.

# x축 각 막대의 중앙에 영화 제목을 레이블로 추가하자.
plt.xticks(range(len(movies)), movies)

plt.show()

"""
히스토그램 그리기
히스토그램: 정해진 구간에 해당되는 항목의 개수를 보여줌으로써 값의 분포를 관찰할 수 있는 그래프 형태이다.
"""

from collections import Counter

grades = [83, 95, 91, 87, 70, 0, 85, 82, 100, 67, 73, 77, 0]

# 점수는 10점 단위로 그룹화한다. 100점은 90점대에 속한다.
histogram = Counter(min(grade // 10 * 10, 90) for grade in grades)

plt.bar([x + 5 for x in histogram.keys()],  # 각 막대를 오른쪽으로 5만큼 옮기고
        histogram.values(),                 # 각 막대의 높이를 정해주고
        10,                                 # 너비는 10 으로 하자.
        edgecolor=(0, 0, 0))                # 각 막대의 테두리는 검은색으로 설정하자.

plt.axis([-5, 105, 0, 5])                   # x축은 -5부터 105
                                            # y축은 0부터 5
plt.xticks([10 * i for i in range(11)])     # x 축의 레이블은 0, 10, ..., 100
plt.xlabel("Decile")
plt.ylabel("# of Students")
plt.title("Distribution of Exam 1 Grades")
plt.show()                        
                    
'''
plt.axis를 사용할 때 주의 할점 * y축을 0 에서 시작하지 않으면 오해를 불러 일으킬 수 있음
'''

mentions = [500, 505]
years = [2017, 2018]

plt.bar(years, mentions, 0.8)
plt.xticks(years)
plt.ylabel("# of times I heard someone say 'data science")

# 이렇게 하지 않으면 matplotlib이 x축에 0, 1 레이블을 달고
# 주변부 어딘가에 +2.013e3 이라고 표기해 둘 것이다.
plt.ticklabel_format(useOffset=False)

# 오해를 불러일으키는 y축은 500이상의 부분만 보여 줄 것이다.
plt.axis([2016.5, 2018.5, 499, 506])
plt.title("Look at the 'Huge' Increase!")
plt.show()

# 오해를 불러일으키지 않는 그래프로 변환
plt.bar(years, mentions, 0.8)
plt.xticks(years)
plt.axis([2016.5, 2018.5, 0, 550])
plt.title("Not So Huge Anymore")
plt.show()