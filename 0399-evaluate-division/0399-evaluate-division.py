from collections import defaultdict

class Solution:
    def calcEquation(self, equations, values, queries):
        graph = defaultdict(dict)

        # Build graph
        for (a, b), value in zip(equations, values):
            graph[a][b] = value
            graph[b][a] = 1 / value

        def dfs(start, end, visited):
            if start == end:
                return 1.0

            visited.add(start)

            for neighbor, weight in graph[start].items():
                if neighbor not in visited:
                    result = dfs(neighbor, end, visited)
                    if result != -1:
                        return weight * result

            return -1

        answers = []

        for a, b in queries:
            if a not in graph or b not in graph:
                answers.append(-1.0)
            elif a == b:
                answers.append(1.0)
            else:
                answers.append(dfs(a, b, set()))

        return answers
        