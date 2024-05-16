

import brainfuck

s = "Meijo University\n"
prog = "[-]\n"
nn = 0

for c in s:
        n = ord(c)
        if n >= nn:
                for i in range(n - nn): prog = prog + "+"
        else:
                for i in range(nn - n): prog = prog + "-"
        nn = n
        prog = prog + ".\n"
print(prog)
brainfuck.evaluate(prog)

