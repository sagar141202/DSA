# Course Schedule (Topological Sort)

## Problem Statement
Given the number of courses (n) and the prerequisites (prerequisites[i] = [ai, bi]), where ai is the course and bi is the prerequisite for course ai, determine if it's possible to finish all courses. The prerequisites are given as a 2D array where each pair represents a course and its prerequisite. For example, if prerequisites[i] = [0, 1], it means course 0 has course 1 as a prerequisite.

## Approach
We can use Topological Sort to solve this problem by creating a directed graph and checking for cycles. If there are no cycles, it's possible to finish all courses. We use a depth-first search (DFS) or breadth-first search (BFS) to detect cycles.

## Complexity
- Time: O(n + m)
- Space: O(n + m)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
        // Create adjacency list
        vector<vector<int>> graph(numCourses);
        vector<int> visited(numCourses, 0);
        
        // Build graph
        for (const auto& pair : prerequisites) {
            graph[pair[1]].push_back(pair[0]);
        }
        
        // Check for cycles using DFS
        for (int i = 0; i < numCourses; i++) {
            if (!dfs(graph, visited, i)) {
                return false;
            }
        }
        
        return true;
    }
    
    bool dfs(vector<vector<int>>& graph, vector<int>& visited, int course) {
        // If visited and in recursion stack, cycle detected
        if (visited[course] == -1) {
            return false;
        }
        
        // If already visited and not in recursion stack
        if (visited[course] == 1) {
            return true;
        }
        
        // Mark as visited and in recursion stack
        visited[course] = -1;
        
        // Check all neighbors
        for (const auto& neighbor : graph[course]) {
            if (!dfs(graph, visited, neighbor)) {
                return false;
            }
        }
        
        // Mark as visited and not in recursion stack
        visited[course] = 1;
        
        return true;
    }
};

int main() {
    Solution solution;
    int numCourses = 2;
    vector<vector<int>> prerequisites = {{1, 0}};
    cout << solution.canFinish(numCourses, prerequisites) << endl;  // Output: 1
    
    return 0;
}
```

## Test Cases
```
Input: numCourses = 2, prerequisites = [[1, 0]]
Output: true
Input: numCourses = 2, prerequisites = [[1, 0], [0, 1]]
Output: false
```

## Key Takeaways
- Topological Sort can be used to detect cycles in a directed graph.
- DFS or BFS can be used to implement Topological Sort.
- The problem can be solved in O(n + m) time complexity, where n is the number of courses and m is the number of prerequisites.