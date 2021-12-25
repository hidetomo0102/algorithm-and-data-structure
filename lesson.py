# ABC130 C - Rectangle Cutting

W, H, x, y = map(float, input().split())

count = 0
if (x == W / 2) and (y == H / 2):
    count = 1

print((W * H) / 2, count)
