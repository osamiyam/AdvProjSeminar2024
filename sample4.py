

import brainfuck

s = "Meijo University\n"
prog = "[-]\n"
nn = 0

def writeit(c, m1, m2):
        global prog
        prog += ">" + ("+" * m1)
        prog += "[<" + (c * 5) + ">-]<" + (c * m2)

for c in s:
        n = ord(c)
        if n >= nn:
                if n - nn < 128:
                        writeit("+", (n - nn) // 5, (n - nn) % 5)
                else :
                        writeit("-", (nn - n + 256) // 5, (nn - n + 256) % 5)
        else:
                if nn - n < 128:
                        writeit("-", (nn - n) // 5, (nn - n) % 5)
                else :
                        writeit("+", (n - nn + 256) // 5, (n - nn + 256) % 5)
        nn = n
        prog += ".\n"
print(prog)
brainfuck.evaluate(prog)

