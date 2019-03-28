def lev(s1, s2):
    d = [[0]*(len(s2))]*(len(s1))
    for i in range(len(s1)):
        d[i][0] = i

    for i in range(len(s2)):
        d[0][i] = i

    for j in range(1, len(s2)):
        for i in range (1, len(s1)):
            if s1[i] == s2[j]:
                d[i][j] = d[i-1][j-1]
            else:
                d[i][j] = min(d[i-1][j]+1,d[i][j-1]+1,d[i-1][j-1]+1)
    print(d)
    return d[len(s1)-1][len(s2)-1]

print(lev("ros","horse"))