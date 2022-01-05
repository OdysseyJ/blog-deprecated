n = int(input())

for _ in range(n):
    words = input().split(" ")
    sentence = " ".join(["".join(reversed(word)) for word in words])
    print(sentence)
