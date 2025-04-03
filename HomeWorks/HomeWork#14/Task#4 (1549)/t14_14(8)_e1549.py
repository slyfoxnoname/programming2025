from collections import deque

def ritual(n, m, k):
    circle = deque([("Gared", i) for i in range(1, n + 1)] + [("Keka", i) for i in range(1, m + 1)])
    next_servant = {"Gared": n + 1, "Keka": m + 1}

    while len(circle) > 1:
        circle.rotate(-k)
        first_victim = circle.popleft()
        circle.rotate(-k + 1)
        second_victim = circle.popleft()

        if first_victim[0] == second_victim[0]:
            new_servant = ("Gared", next_servant["Gared"])
            next_servant["Gared"] += 1
        else:
            new_servant = ("Keka", next_servant["Keka"])
            next_servant["Keka"] += 1

        circle.append(new_servant)

    print(circle[0][0])


if __name__ == "__main__":
    while True:
        n, m, k = map(int, input().strip().split())
        if n == 0 and m == 0 and k == 0:
            break
        ritual(n, m, k)
