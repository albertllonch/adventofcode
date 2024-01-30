def part_one():
    with open('input.txt','r') as f:
        b = ''
        movements = 4
        for x in f.readline():
            if len(b) <= 3:
                b += x
                continue
            if b.count(b[0]) == 1 and b.count(b[1]) == 1 and \
                    b.count(b[2]) == 1 and b.count(b[3]) == 1:
                        print(movements)
                        break
            b += x
            b = b[1:]
            movements += 1

def part_two():
    with open('input.txt', 'r') as f:
        stream = f.read().strip()
        for i in range(14,len(stream)+ 1):
            if len(set(stream[i - 14:i])) == 14:
                print(i)
        return None

if __name__ == "__main__":
    part_one()
    part_two()


