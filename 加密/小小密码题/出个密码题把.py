from hilbertcurve.hilbertcurve import HilbertCurve
from PIL import Image

im_cp = Image.open("m.png")
im_new = Image.new('RGB', (256, 256))

p = 8
n = 2
hilbert_curve = HilbertCurve(p, n)
distances = list(range(65536))
points = hilbert_curve.points_from_distances(distances)
order = []
for point, dist in zip(points, distances):
    order.append(tuple(point))

for k in range(65536):
    tmp = im_cp.getpixel((k % 256, k // 256))
    im_new.putpixel(order[k], tmp)

im_new.save('12.png')