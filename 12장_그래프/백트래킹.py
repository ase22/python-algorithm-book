# 백트래킹(Backtracking)은 해결책에 대한 후보를 구축해 나아가다가 가능성이 없다고 판단되는 즉시
# 후보를 포기(백트랙)해 정답을 찾아가는 범용적인 알고리즘으로, 제약 충족 문제에 특히 유용하다.
# 제약 충족 문제: 수많은 제약조건을 충종하는 상태를 찾아내는 수학 문제를 말한다.

# 예) 스도쿠에서
  # 제약조건: 1~9의 숫자를 한 번만 넣는 조건
  # 상태: 정답
# 다양한 예) 십자말 풀이, 8퀸 문제, 4색 문제, 배낭 문제, 문자열 파싱, 조합 최적화

# 백트래킹은 DFS와 같은 방식으로 탐색하는 모든 방법을 뜻하며, DFS는 백트래킹의 골격을 이루는 알고리즘이다.

# 백트래킹은 가보고 되돌아오고를 반복한다. 운이 좋으면 시행착오를 거치고 목적지에 도착할 수 있지만,
# 최악의 경우에는 모든 경우를 다 거친 다음에 도착할 수 있다.

# 그래서 브루트 포스와 유사하지만 한 번 방문 후 가능성이 없는 경우 즉시 후보를 포기한다는 점(가지치기, pruning)에서
# 매 번 같은 경로를 방문하는 브루트 포스보다 더 우월한 알고리즘이다.

