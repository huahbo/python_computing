# -*- coding: utf-8 -*-
"""临时：把代码块/行内代码中被转成的 [链接](url) 还原为裸 URL。"""
import glob

bt = chr(96)
nl = chr(10)
marker = "[链接]("

def restore_code(line):
    while marker in line:
        s = line.index(marker)
        e = line.find(")", s + len(marker))
        if e == -1: break
        url = line[s + len(marker):e]
        line = line[:s] + url + line[e + 1:]
    return line

def restore_inline(line):
    needle = bt + marker
    while needle in line:
        s = line.index(needle)
        e = line.find(")" + bt, s + len(needle))
        if e == -1: break
        url = line[s + len(needle):e]
        line = line[:s] + bt + url + bt + line[e + 2:]
    return line

fixed = 0
for p in glob.glob("chapters/**/*.md", recursive=True):
    txt = open(p, encoding="utf-8").read()
    lines = txt.split(nl)
    out = []
    in_code = False
    for line in lines:
        s = line.strip()
        if s.startswith(bt * 3) or s.startswith("~~~"):
            in_code = not in_code
        elif in_code:
            line = restore_code(line)
        else:
            line = restore_inline(line)
        out.append(line)
    new = nl.join(out)
    if new != txt:
        open(p, "w", encoding="utf-8").write(new)
        fixed += 1
        print("restored", p)
print("restored files:", fixed)