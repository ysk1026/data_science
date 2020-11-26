'''
더 공부해보고 싶다면
matplotlib 갤러리를 살펴봄
seaborn은 matplotlib을 발전시킨 것으로 더 아름답고 복잡한 시각화 가능
Altair는 최근에 나온 선언형 시각화 파이썬 라이브러리
D3.js (웹을 위한 JS 라이브러리)
Bokeh는 D3.js 스타일의 시각화를 파이썬에서 만들 수 있게 해주는 라이브러리.

두가지 목적: 탐색(exploration) / 전달(communication)

시각화를 위해 사용하는 라이브러리 - matplotlib

matplotlib 함수

savefig() - 그래프 저장 / show() - 화면에 출력

선 그래프를 만들 때:

plt.plot(x축, y축, color = '', marker='o', linestyle='solid')

plt.title() - 제목

plt.ylabel() y축에 레이블 추가

plt.show()

plt.bar의 세번째 인자는 막대의 너비를 정한다.

plt.axis([-5, 105, 0, 5]) X축 범위(-5 ~ 105) Y축 범위(0~5)
'''