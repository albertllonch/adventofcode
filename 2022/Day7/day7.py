import os


def get_size(dirname: str,files: dict) -> int:
    sz=0
    for k, v in files.items():
        if k.startswith(f'{dirname}/'):
            sz += v

    if sz > 100000:
        return 0
    else:
        return sz


def solve(s: str) -> int:
    files = {}
    dirs = {'/'}

    pwd='/'
    for line in s.splitlines()[1:]:
        if line == '$ cd ..':
            pwd = os.path.dirname(pwd) or '/'
        elif line.startswith('$ cd'):
            pwd = os.path.join(pwd, line.split(' ',2)[-1])
            dirs.add(pwd)
        elif line.startswith(('$ ls','dir ')):
            continue
        else:
            size, filename = line.split(' ', 1)
            files[os.path.join(pwd,filename)] = int(size)

    return sum(get_size(dirname,files) for dirname in dirs)

with open('input.txt','r') as f:
    print(solve(f.read()))
