# link : https://leetcode.com/problems/count-the-number-of-complete-components/


from collections import defaultdict
class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)

        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)

        visited = set()
        cnt = 0
        def dfs(node,comp):
            comp.add(node)
            visited.add(node)
            for n in graph[node]:
                if n not in visited:
                    dfs(n,comp)
        for i in range(n):
            if i not in visited:
                comp = set()
                dfs(i,comp)
                if all(len(graph[node]) == len(comp)-1 for node in comp):
                    cnt += 1

        return cnt
        
