def get_sums(p):
    s =[]
    m = len(p)
    for mask in range(1 << m):
        sm = 0
        for i in range(m):
            if mask & (1 << i):
                sm += p[i]
        s.append(sm)
    return s

def get_balanced(p):
    s = get_sums(p)
    st = set(s)
    b = set()
    for w in s:
        if w % 2 == 0 and (w // 2) in st:
            b.add(w)
    return sorted(b)
def main():
    n,m = map(int, input().split())
    b = list(map(int, input().split()))
    p = list(map(int, input().split()))

    bw = get_balanced(p)

    res = set()
    for x in b:
        for w in bw:
            res.add(x + w)

    for w in sorted(res):
       print(w)

main()