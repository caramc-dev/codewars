from collections import defaultdict


class Solution:
    def validPath(self, n, edges, source, destination):
        if source == destination:
            return True

        # Build the graph using a default dictionary
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        seen = set()
        seen.add(source)
        stack = [source]

        while stack:  # while there is a stack
            node = stack.pop()  # pop off the top most node and assign it to node
            if node == destination:  # if that node is the destination then return True
                return True
            for nei_node in graph[node]:  # If that condition is not met, visit each of the neighbour nodes,
                if nei_node not in seen:  # if you've seen, skip the if and continue in the for loop (if there is a stack),
                    seen.add(nei_node)  # and if you have not queued/visited it yet mark it as seen
                    stack.append(nei_node)  # and push any neighbours onto to the current stack

        return False  # If you don't reach a True by the time the stack empties, and the While loop concludes, its a false
    