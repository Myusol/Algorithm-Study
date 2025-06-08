def solution(info, edges):
    from collections import defaultdict

    graph = defaultdict(list)
    for parent, child in edges:
        graph[parent].append(child)

    max_sheep = 0

    def dfs(current_node, sheep, wolf, next_nodes):
        nonlocal max_sheep

        if info[current_node] == 0:
            sheep += 1
        else:
            wolf += 1

        if wolf >= sheep:
            return

        max_sheep = max(max_sheep, sheep)

        candidates = next_nodes + graph[current_node]

        if current_node in candidates:
            candidates.remove(current_node)

        for next_node in candidates:
            dfs(next_node, sheep, wolf, candidates.copy())

    dfs(0, 0, 0, [0])
    return max_sheep