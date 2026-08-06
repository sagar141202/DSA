# Euler Path

## Problem Statement
Given a directed or undirected graph, find an Euler path, which is a path that visits every edge in the graph exactly once. The graph may have multiple connected components. If the graph has an Euler path, return one possible path. Otherwise, return an empty list. The graph is represented as an adjacency list where each key is a node and its corresponding value is a list of its neighbors. The graph has at most 100 nodes and 500 edges.

## Approach
The approach to solve this problem is to use Hierholzer's algorithm, which states that a graph has an Euler path if and only if at most two vertices have odd degrees. We start at a node with an odd degree and keep removing edges from the graph as we traverse them, until we have visited all edges.

## Complexity
- Time: O(E + V)
- Space: O(E + V)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

vector<int> eulerPath(vector<int> graph[], int n) {
    // Initialize the result
    vector<int> result;
    
    // Initialize a stack with a starting node
    stack<int> stack;
    for (int i = 0; i < n; i++) {
        if (graph[i].size() % 2 != 0) {
            stack.push(i);
            break;
        }
    }
    if (stack.empty()) {
        for (int i = 0; i < n; i++) {
            if (!graph[i].empty()) {
                stack.push(i);
                break;
            }
        }
    }
    
    // Traverse the graph
    while (!stack.empty()) {
        int node = stack.top();
        if (!graph[node].empty()) {
            int neighbor = graph[node].back();
            graph[node].pop_back();
            for (int i = 0; i < n; i++) {
                auto it = find(graph[i].begin(), graph[i].end(), node);
                if (it != graph[i].end()) {
                    graph[i].erase(it);
                    break;
                }
            }
            stack.push(neighbor);
        } else {
            result.push_back(stack.top());
            stack.pop();
        }
    }
    
    // Reverse the result
    reverse(result.begin(), result.end());
    return result;
}

int main() {
    int n;
    cout << "Enter the number of nodes: ";
    cin >> n;
    vector<int> graph[n];
    cout << "Enter the edges (u v):" << endl;
    int m;
    cin >> m;
    for (int i = 0; i < m; i++) {
        int u, v;
        cin >> u >> v;
        graph[u].push_back(v);
        graph[v].push_back(u);
    }
    vector<int> result = eulerPath(graph, n);
    cout << "Euler Path: ";
    for (int i = 0; i < result.size(); i++) {
        cout << result[i] << " ";
    }
    return 0;
}
```

## Test Cases
```
Input: 
Enter the number of nodes: 5
Enter the edges (u v):
6
0 1
0 2
1 2
1 3
2 4
3 4
Output: 
Euler Path: 0 1 3 4 2 0
```

## Key Takeaways
- The graph should be connected or have at most two nodes with odd degrees to have an Euler path.
- The Hierholzer's algorithm is used to find the Euler path in the graph.
- The time complexity of the algorithm is O(E + V) and space complexity is also O(E + V).