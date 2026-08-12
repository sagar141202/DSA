# Alien Dictionary

## Problem Statement
There is a new alien language that uses the English alphabet. However, the order among the letters is unknown to you. You receive a list of non-empty words from this language, where the words are sorted lexicographically in this alien language. Determine the order of the letters in this alien language. The input is a list of strings, where each string represents a word in the alien language. The output should be a string representing the order of the letters in the alien language. For example, given the words ["wrt", "wrf", "er", "ett", "rftt"], the order of the letters is "wertf".

## Approach
The approach to solve this problem is to use a topological sorting algorithm with a directed graph. We create a graph where each node represents a letter, and a directed edge from node A to node B means that A comes before B in the alien language. We then use a topological sort to find the order of the letters.

## Complexity
- Time: O(N * M + 26 * 26)
- Space: O(26 * 26 + 26)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

vector<string> alien_dict;
vector<int> indegree(26, 0);
vector<vector<int>> graph(26, vector<int>(26, 0));
string result = "";

void build_graph() {
    for (int i = 0; i < alien_dict.size() - 1; i++) {
        string word1 = alien_dict[i];
        string word2 = alien_dict[i + 1];
        int len1 = word1.size();
        int len2 = word2.size();
        int min_len = min(len1, len2);
        for (int j = 0; j < min_len; j++) {
            if (word1[j] != word2[j]) {
                int node1 = word1[j] - 'a';
                int node2 = word2[j] - 'a';
                if (graph[node1][node2] == 0) {
                    graph[node1][node2] = 1;
                    indegree[node2]++;
                }
                break;
            }
        }
    }
}

void topological_sort() {
    queue<int> q;
    for (int i = 0; i < 26; i++) {
        if (indegree[i] == 0) {
            q.push(i);
        }
    }
    while (!q.empty()) {
        int node = q.front();
        q.pop();
        result += (char)(node + 'a');
        for (int i = 0; i < 26; i++) {
            if (graph[node][i] == 1) {
                indegree[i]--;
                if (indegree[i] == 0) {
                    q.push(i);
                }
            }
        }
    }
}

int main() {
    alien_dict = {"wrt", "wrf", "er", "ett", "rftt"};
    build_graph();
    topological_sort();
    cout << result << endl;
    return 0;
}
```

## Test Cases
```
Input: ["wrt", "wrf", "er", "ett", "rftt"]
Output: "wertf"
```

## Key Takeaways
- The alien dictionary problem can be solved using a topological sorting algorithm with a directed graph.
- The time complexity is O(N * M + 26 * 26), where N is the number of words and M is the maximum length of a word.
- The space complexity is O(26 * 26 + 26), which is used to store the graph and the indegree array.