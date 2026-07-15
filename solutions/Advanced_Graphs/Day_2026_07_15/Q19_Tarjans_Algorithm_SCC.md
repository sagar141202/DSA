# Tarjan's Algorithm (SCC)

## Problem Statement
Given a directed graph, find all strongly connected components (SCCs) in the graph. A strongly connected component is a subgraph where there is a path from every vertex to every other vertex. The graph is represented as an adjacency list, where each index represents a vertex and its corresponding value is a list of its neighboring vertices. The algorithm should output all SCCs in the graph.

## Approach
Tarjan's algorithm uses depth-first search (DFS) to traverse the graph and identify SCCs. It maintains a stack of vertices and uses a low-link value to keep track of the smallest index reachable from each vertex. The algorithm iteratively pops vertices from the stack and adds them to the current SCC if their low-link value is greater than or equal to the index of the current SCC.

## Complexity
- Time: O(V + E)
- Space: O(V)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Tarjan {
public:
    int indexCounter = 0;
    vector<int> indices;
    vector<int> lowlinks;
    vector<bool> onStack;
    stack<int> stack;
    vector<vector<int>> sccs;

    void strongconnect(int vertex) {
        indices[vertex] = indexCounter;
        lowlinks[vertex] = indexCounter;
        indexCounter++;
        stack.push(vertex);
        onStack[vertex] = true;

        for (int neighbor : graph[vertex]) {
            if (indices[neighbor] == -1) {
                strongconnect(neighbor);
                lowlinks[vertex] = min(lowlinks[vertex], lowlinks[neighbor]);
            } else if (onStack[neighbor]) {
                lowlinks[vertex] = min(lowlinks[vertex], indices[neighbor]);
            }
        }

        if (lowlinks[vertex] == indices[vertex]) {
            vector<int> connectedComponent;
            while (true) {
                int w = stack.top();
                stack.pop();
                onStack[w] = false;
                connectedComponent.push_back(w);
                if (w == vertex) break;
            }
            sccs.push_back(connectedComponent);
        }
    }

    vector<vector<int>> tarjanSCC(vector<vector<int>>& graph) {
        this->graph = graph;
        int numVertices = graph.size();
        indices.resize(numVertices, -1);
        lowlinks.resize(numVertices, -1);
        onStack.resize(numVertices, false);

        for (int i = 0; i < numVertices; i++) {
            if (indices[i] == -1) {
                strongconnect(i);
            }
        }

        return sccs;
    }

private:
    vector<vector<int>> graph;
};

int main() {
    int numVertices = 8;
    vector<vector<int>> graph(numVertices);
    graph[0].push_back(1);
    graph[1].push_back(2);
    graph[2].push_back(0);
    graph[2].push_back(3);
    graph[3].push_back(4);
    graph[4].push_back(5);
    graph[5].push_back(6);
    graph[6].push_back(4);
    graph[6].push_back(7);

    Tarjan tarjan;
    vector<vector<int>> sccs = tarjan.tarjanSCC(graph);

    cout << "Strongly Connected Components:" << endl;
    for (int i = 0; i < sccs.size(); i++) {
        cout << "SCC " << i + 1 << ": ";
        for (int vertex : sccs[i]) {
            cout << vertex << " ";
        }
        cout << endl;
    }

    return 0;
}
```

## Test Cases
```
Input: 
Graph with 8 vertices and the following edges:
0 -> 1
1 -> 2
2 -> 0, 3
3 -> 4
4 -> 5
5 -> 6
6 -> 4, 7

Output: 
Strongly Connected Components:
SCC 1: 0 1 2 
SCC 2: 3 
SCC 3: 4 5 6 
SCC 4: 7 
```

## Key Takeaways
- Tarjan's algorithm is used to find strongly connected components (SCCs) in a directed graph.
- The algorithm uses a depth-first search (DFS) approach and maintains a stack of vertices to keep track of the current SCC.
- The low-link value is used to determine whether a vertex belongs to the current SCC or not.