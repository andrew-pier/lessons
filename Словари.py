moskva = 495
piter = 812
penza = 8412

d = {
    'moskva': 495,
    'piter': 812,
    'penza': 8412
}
r = dict(moskva=495, piter=812, penza=8412)
r['magadan'] = 8413
for i in r:
    print(i, ' = ', r[i])
