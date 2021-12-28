n = int(input())
m = int(input())
broken = []
if m != 0:
    broken = list(map(int, input().split(" ")))

buttons = [True] * 10
answer = 1000000000

for b in broken:
    buttons[b] = False

def can_move_by_num(num):
    for k in str(num):
        if not buttons[int(k)]:
            return False
    return True


# 0 <= N <= 500000
# 가능한 채널 = 무한대
# 검사해야하는 범위 = 0~1000000
for i in range(1000001):
    if can_move_by_num(i):
        answer = min(answer, len(str(i)) + abs(i-n))

answer = min(answer, abs(n - 100))

print(answer)
