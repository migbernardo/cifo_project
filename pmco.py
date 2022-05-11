from random import sample

p1 = [8, 4, 2, 9, 6, 5, 7, 3, 1]
p2 = [8, 3, 2, 5, 6, 9, 7, 4, 1]
co_points = sample(range(len(p1)), k=2)
co_points.sort()
