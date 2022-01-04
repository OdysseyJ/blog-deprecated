count, m = map(int, input().split(" "))
nums = sorted(map(int, input().split(" ")))

stack = []
visited = [False] * count


def dfs(d, idx):
    if d == m:
        print(' '.join(map(str, stack)))
        return

    for i in range(idx, count):
        if not visited[i]:
            visited[i] = True
            stack.append(nums[i])
            dfs(d+1, i+1)
            stack.pop()
            visited[i] = False


dfs(0, 0)
