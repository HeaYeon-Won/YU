"""
정렬된 두 묶음의 숫자 카드가 있다고 하자. 각 묶음의 카드의 수를 A, B라 하면 보통 두 묶음을 합쳐서 하나로 만드는 데에는 A+B 번의 비교를 해야 한다. 
이를테면, 20장의 숫자 카드 묶음과 30장의 숫자 카드 묶음을 합치려면 50번의 비교가 필요하다.

매우 많은 숫자 카드 묶음이 책상 위에 놓여 있다. 이들을 두 묶음씩 골라 서로 합쳐나간다면, 고르는 순서에 따라서 비교 횟수가 매우 달라진다. 
예를 들어 10장, 20장, 40장의 묶음이 있다면 10장과 20장을 합친 뒤, 합친 30장 묶음과 40장을 합친다면 (10 + 20) + (30 + 40) = 100번의 비교가 필요하다. 
그러나 10장과 40장을 합친 뒤, 합친 50장 묶음과 20장을 합친다면 (10 + 40) + (50 + 20) = 120 번의 비교가 필요하므로 덜 효율적인 방법이다.
N개의 숫자 카드 묶음의 각각의 크기가 주어질 때, 최소한 몇 번의 비교가 필요한지를 구하는 프로그램을 작성하시오.
"""
from sys import stdin
import heapq
def solution(heap):
    result=0
    while len(heap)!=1:
        first, second = heapq.heappop(heap), heapq.heappop(heap)
        next = first+second
        result+=next
        heapq.heappush(heap, next)
    print(result)

n=int(input())
heap=[]
for _ in range(n):
    heapq.heappush(heap, (int(stdin.readline())))
solution(heap)

"""
첫번째 시도
그저 정렬해놓은 데이터를 계속 더해가며 값을 갱신하였다.
이렇게 되면 항상 1,2번째 우선순위를 가진 값이 뽑혀야하지만 이를 만족하지 못하였다.
예를들어 30,30,30,40,50 이 있을때
첫번째 시행에서 60이 나온다.
이후 60+30이 아닌 30+40이 더 적은 값이므로 높은 우선순위를 가져야하지만 그러지 못하였다.

두번째 시도
한번 시행 후 리스트[1:]만큼을 잘라온 후 정렬하여 다시 진행하였다.
이때 시간복잡도는 O(size(리스트)-1) + O(N Log N) =  O(size(리스트)-1) 이 시행 횟수만큼 반복되어
약 N^2의 시간복잡도를 가지게 되어 시간초과가 발생하였다.

세번째 시도
총 N개의 노드가 있을때 완전 이진트리의 높이는 logN이다.
이때 힙의 삽입과 삭제에 걸리는 시간은 O(logN)이다.
이를 N번 반복하였으므로 총 시간복잡도 O(NlogN)으로 제출에 성공하였다.

"""