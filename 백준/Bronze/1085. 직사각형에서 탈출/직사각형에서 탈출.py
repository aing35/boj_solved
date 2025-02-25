import sys

x, y, w, h = map(int, sys.stdin.readline().split())

# x축 따지기
if w - x < x:
    x_sel = w - x
else:
    x_sel = x

# y축 따지기
if h - y < y:
    y_sel = h - y
else:
    y_sel = y

# 결정된 x, y 비교
if x_sel > y_sel:
    sys.stdout.write(f"{y_sel}")
else:
    sys.stdout.write(f"{x_sel}")
