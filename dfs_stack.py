import collections

def iterative_dfs(start_v):

    discovered = []
    stack = [start_v]

    while stack:
        v = stack.pop()

        if not v in discovered:

            discovered.append(v)

            for w in graph[v]:
                stack.append(w)

    return discovered

if __name__ == "__main__":
    
    graph = {
        1 : [2, 3 ,4],
        2 : [5],
        3 : [5],
        4 : [],
        5 : [6, 7],
        6 : [],
        7 : [3]
    }

    print(iterative_dfs(1))