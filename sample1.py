
import brainfuck

s = "Meijo University\n"
prog = ""

for c in s:
        prog = prog + "[-]"
        n = ord(c)
        for i in range(n):
                prog = prog + "+"
        prog = prog + ".\n"
print(prog)
brainfuck.evaluate(prog)

