def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

def job_scheduling(jobs):
    jobs_sorted = sorted(jobs, key=lambda x: x[1])
    selected = []
    prev_finish = 0

    for start, finish in jobs_sorted:
        if start >= prev_finish:
            selected.append((start, finish))
            prev_finish = finish

    return selected

import heapq
def dijkstra_mst(graph, source):
    distance = dict.fromkeys(graph, float('inf'))
    distance[source] = 0
    heap = [(0, source)]

    while heap:
        d, u = heapq.heappop(heap)
        if d > distance[u]:
            continue
        for v, weight in graph[u]:
            new_dist = d + weight
            if new_dist < distance[v]:
                distance[v] = new_dist
                heapq.heappush(heap, (new_dist, v))

    return distance

# Test cases
print("Selection sort (Greedy):")
print(selection_sort([64, 25, 12, 22, 11]))

jobs = [(1,2),(2,7),(4,6),(7,10)]
print("\nJob scheduling (Greedy):")
print(job_scheduling(jobs))

graph = {
    'A':[('B',5),('C',1)],
    'B':[('D', 1)],
    'C': [('B', 2), ('D', 6)],
    'D': []
}
print("\nDijkstra's shortest path (Greedy):")
print(dijkstra_mst(graph, 'A'))
