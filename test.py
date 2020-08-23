test = [
        { "id":1, "pid":0},
        { "id":2, "pid":1},
        { "id":3, "pid":1},
        { "id":4, "pid":2},
        { "id":5, "pid":2},
        { "id":6, "pid":2},
        { "id":7, "pid":3},
        { "id":8, "pid":3},
        { "id":9, "pid":3},
        { "id":10,"pid":4},
        { "id":11,"pid":4},
        { "id":12,"pid":4},
        { "id":13,"pid":4},
        ]

def reuse(pid,l,r):
    l = [ e for e in l if e not in r]
    if len(l) == 0:
        return r
    for e in l:
        if e['pid'] == pid:
            r.append(e)
            r = reuse(e['id'],l,r)
    return r

r = []
res = reuse(0,test,r)

[ print(r) for r in res ]
