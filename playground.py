e, s, m = map(int, input().split(" "))

i = 1
while True:
    if not((i-e)%15) and not((i-s)%28) and not((i-m)%19):
        print(i)
        break
    else:
        i += 1
