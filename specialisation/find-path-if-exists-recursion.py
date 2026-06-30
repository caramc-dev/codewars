from collections import defaultdict


class Solution:
    def validPath(self, n, edges, source, destination):
        # 1. DFS with recursion

        # Base case - if the source matches the destintation break out and return True
        if source == destination:
            return True

        # Build the graph using a default dictionary
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        seen = set()
        seen.add(source)

        # Create recursive function
        def dfs(i):
            if i == destination:  # return True if the source is the destination
                return True

            for nei_node in graph[i]:  # Loop through all the neighbours of the current node i
                if nei_node not in seen:  # If the node is not in seen (has not been visisted yet)
                    seen.add(nei_node)  # add it to seen (has been visited) before recursing to avoid looping on cycles
                    if dfs(nei_node):  # recurse here, into the neighbour suspending control waiting for control to return
                        return True  # if that branch found the destination, propagate True straight back up
                        # if dfs(nei_node) was False, control returns to this loop and tries the next neighbour
            return False  # every neighbour explored, none led to destination - this branch is a dead end

        return dfs(source)

