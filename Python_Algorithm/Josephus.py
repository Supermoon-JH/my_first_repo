# 요세푸스 문제(Josephus)

n, k = map(int, input().split())

# 리스트 내포로 queue에 1부터 n까지 값을 넣는다.
queue = [k for k in range(1, n+1)]
# 이게 더 좋은 방법: queue = list(range(1, n+1))

# 큐가 비어있지 않는 한 반복문 수행
while len(queue) != 0:
    # k-1개의 데이터를 빼내고 다시 넣는다.
    for _ in range(k-1):
        c = queue.pop(0)
        queue.append(c)

    c = queue.pop(0)
    print(c)
