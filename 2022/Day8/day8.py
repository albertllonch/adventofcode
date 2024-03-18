
def solve(f): 
    m = []
    for line in f.readlines(): 
        row = [int(x) for x in line.strip()]
        m.append(row)
    m_transposed = list(zip(*m))

    visible = 0
    for i in range(len(m[0])):
        for j in range(len(m)):
            tree = m[i][j]
            views = [   [z for z in m[i][0:j]],[z for z in m[i][j+1:]],\
                        [z for z in m_transposed[j][0:i]],[z for z in m_transposed[j][i+1:]]\
                    ]
            if any(list(map(lambda view: all([z < tree for z in view]),views))):
                visible +=1
    return visible
    
with open('input.txt','r') as f:
    print(solve(f))
