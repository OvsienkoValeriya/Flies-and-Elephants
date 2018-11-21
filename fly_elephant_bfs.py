import json
import sys

filename = sys.argv[1]
start = sys.argv[2]
finish = sys.argv[3]

graph = None
with open(filename, "r", encoding="utf-8") as f:
    graph = json.load(f)

queue = [(start, None)]
visited = []
breadcrumbs = {}

while len(queue) != 0:
    vertex, breadcrumb = queue.pop(0)
    if vertex not in visited:
        visited.append(vertex)
        breadcrumbs[vertex] = breadcrumb
        for child in graph[vertex]:
            queue.append((child, vertex))

path = []
ancestor = finish
while ancestor is not None:
    path.append(ancestor)
    ancestor = breadcrumbs[ancestor]

path.reverse()
print(path)
