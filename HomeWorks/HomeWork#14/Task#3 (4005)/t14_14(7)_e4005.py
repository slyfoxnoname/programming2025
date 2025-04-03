from collections import deque


def play_war(n, deck1, deck2):
    deck1 = deque(deck1)
    deck2 = deque(deck2)

    for turn in range(200000):
        if not deck1:
            print("second", turn)
            return
        if not deck2:
            print("first", turn)
            return

        card1 = deck1.popleft()
        card2 = deck2.popleft()

        if (card1 > card2 and not (card1 == n - 1 and card2 == 0)) or (card1 == 0 and card2 == n - 1):
            deck1.append(card1)
            deck1.append(card2)
        else:
            deck2.append(card1)
            deck2.append(card2)

    print("draw")


if __name__ == "__main__":
    n = int(input().strip())
    deck1 = list(map(int, input().strip().split()))
    deck2 = list(map(int, input().strip().split()))
    play_war(n, deck1, deck2)
