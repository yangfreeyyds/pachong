from hilbertcurve.hilbertcurve import HilbertCurve
from PIL import Image

im_cp = Image.open("Rzz.jpg")
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
    tmp = im_cp.getpixel(order[k])
    im_new.putpixel((k % 256, k // 256), tmp)

im_new.save('m.png')