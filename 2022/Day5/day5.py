class Bay:
    def __init__(self,nCrates):
        self.nCrates = nCrates
        self.crates = [CrateStack() for _ in range(nCrates)]

    def add_items(self,items):
        for crate,item in zip(self.crates,items):
            if item != ' ':
                crate.add_item(item)

    def move(self,take,origin,dest,move_multiple):
        items = self.crates[origin-1].get_items(take)
        if move_multiple:
            self.crates[dest-1].content.extend(items)
        else:
            self.crates[dest-1].content.extend(reversed(items))

    def print_bay(self):
        for crate in self.crates:
            print(crate.content)
        print('-----')

    def get_top_crates(self):
        result = ""
        for x in self.crates:
            if len(x.content) > 0:
                result += x.content[-1]
        return result

class CrateStack:
    def __init__(self):
        self.content = []

    def add_item(self,item):
        self.content.append(item)

    def get_items(self,take):
        items = self.content[-take:]
        self.content = self.content[:-take]
        return items

    def __str__(self):
        return str(self.content)


def solve(file_name,isPartTwo=False):
    
    with open(file_name, 'r') as f:
        lines = f.readlines()
    
    # read and load initial state of bay
    bay = Bay(len(lines[0])//4)
    crate_lines = lines[:lines.index('\n')-1]
    for line in reversed(crate_lines):
        items = list(line)[1:-1:4]
        bay.add_items(items) 
    
    # perform moves of input

    moves = lines[lines.index('\n') + 1:]
    for move in moves:
        info = move.strip().split(' ')
        bay.move(int(info[1]),int(info[3]),int(info[5]),isPartTwo)
    
    print(bay.get_top_crates())


if __name__ == '__main__':
    solve('input.txt',True)
