import heapq


def d1p1(path: str) -> int:
    with open(path) as f:
        lines = [line.strip() for line in f]

    weights, running_total = [], 0
    for line in lines:
        try:
            running_total += int(line)
        except:
            weights.append(running_total)
            running_total = 0

    return max(weights)


def d1p2(path: str) -> int:
    with open(path) as f:
        lines = [line.strip() for line in f]
    
    heap, running_total = [], 0
    for line in lines:
        try:
            running_total += int(line)
        except:
            heapq.heappush(heap, -running_total)
            running_total = 0

    return sum([-heapq.heappop(heap) for _ in range(3)])
