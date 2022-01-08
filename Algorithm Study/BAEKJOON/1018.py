"""
지민이는 자신의 저택에서 MN개의 단위 정사각형으로 나누어져 있는 M×N 크기의 보드를 찾았다.
어떤 정사각형은 검은색으로 칠해져 있고, 나머지는 흰색으로 칠해져 있다. 지민이는 이 보드를 잘라서 8×8 크기의 체스판으로 만들려고 한다.
체스판은 검은색과 흰색이 번갈아서 칠해져 있어야 한다.
구체적으로, 각 칸이 검은색과 흰색 중 하나로 색칠되어 있고, 변을 공유하는 두 개의 사각형은 다른 색으로 칠해져 있어야 한다.
따라서 이 정의를 따르면 체스판을 색칠하는 경우는 두 가지뿐이다. 하나는 맨 왼쪽 위 칸이 흰색인 경우, 하나는 검은색인 경우이다.
보드가 체스판처럼 칠해져 있다는 보장이 없어서, 지민이는 8×8 크기의 체스판으로 잘라낸 후에 몇 개의 정사각형을 다시 칠해야겠다고 생각했다.
당연히 8*8 크기는 아무데서나 골라도 된다. 지민이가 다시 칠해야 하는 정사각형의 최소 개수를 구하는 프로그램을 작성하시오.
"""
def cut(L, case):
    answer = []
    first, second= 0,0
    for i in range(8):
        c = case[i % 2]
        for j in range(8):
            if c[j] != L[i][j]:
                first += 1
    for i in range(8):
        c = case[(i + 1) % 2]
        for j in range(8):
            if c[j] != L[i][j]:
                second += 1
    return min(first, second)

def solution(L):
    color=["B", "W"]
    case = [[color[i%2] for i in range(8)], [color[(i+1)%2] for i in range(8)]]
    answer=[]
    r_loop, c_loop = row-7, col-7
    for r in range(r_loop):
        for c in range(c_loop):
            cuted=[row[c:c + 8] for row in L[r:r + 8]]
            answer.append(cut(cuted, case))

    return min(answer)


row, col  = map(int, input().split())
mtrx=[input() for _ in range(row)]
print(solution(mtrx))
