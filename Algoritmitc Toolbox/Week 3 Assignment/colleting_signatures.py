# python3
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def optimal_points(segments):
    points = []
    # Sorting the segments
    order = sorted(range(len(segments)), key=lambda i: segments[i].end)
    # print(order)
    segments = [segments[i] for i in order]
    # print(segments)

    # Finding out the interval points
    i = 0
    j = 1
    while j != len(segments):
        if segments[i].end - segments[j].start >= 0:
            j += 1
        else:
            # points.append(segments[i].start)
            points.append(segments[i].end)
            i = j
            j += 1
    if len(segments) != 0:
        # points.append(segments[i].start)
        points.append(segments[i].end)
    return points


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    for p in points:
        print(p, end=' ')

