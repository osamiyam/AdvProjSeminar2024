


import brainfuck

s = "Meijo University\n"
prog = "[-]\n"

def writeit(c, m1, m2):
        global prog
        prog += ">" + ("+" * m1)
        prog += "[<" + (c * 5) + ">-]<" + (c * m2)

writeit("+", 8, 3)
prog += ">[-]\n"
writeit("+", 6, 2)
prog += ">[-]\n"
writeit("+", 2, 0)
prog += "<<\n"
prog += "..........>>.<<\n"
prog += ".>........<.>>.<<\n" * 2
prog += "..........>>.<<\n"


print(prog)
brainfuck.evaluate(prog)

