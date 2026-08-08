# Alien Dictionary

## Problem Statement
There is a new alien language that uses the English alphabet. However, the order among the letters is unknown to you. You receive a list of words in the alien language, where each word is written in the alien alphabet. The words are sorted lexicographically in the alien language. Determine the order of the letters in the alien alphabet. For example, if the words are ["wrt", "wrf", "er", "ett", "rftt"], the order of the letters is "wertf". If the order is invalid, return an empty string. The length of each word is between 1 and 50. The number of words is between 1 and 100.

## Approach
The approach to solve this problem is to use a topological sorting algorithm. We can create a directed graph where each node represents a letter, and there is an edge from node A to node B if A comes before B in the alien alphabet. We can then use the topological sorting algorithm to find the order of the letters.

## Complexity
- Time: O(NM) where N is the number of words and M is the maximum length of a word
- Space: O(1) as the size of the graph is limited to 26 nodes (English alphabet)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

vector<char> alienOrder(vector<string>& words) {
    // Create a graph with 26 nodes
    vector<vector<int>> graph(26);
    vector<int> indegree(26, 0);

    // Build the graph
    for (int i = 0; i < words.size() - 1; i++) {
        string word1 = words[i];
        string word2 = words[i + 1];
        int len = min(word1.size(), word2.size());
        for (int j = 0; j < len; j++) {
            if (word1[j] != word2[j]) {
                int u = word1[j] - 'a';
                int v = word2[j] - 'a';
                graph[u].push_back(v);
                indegree[v]++;
                break;
            }
        }
        // If word1 is a prefix of word2, the order is invalid
        if (word1.size() > word2.size() && word1.substr(0, word2.size()) == word2) {
            return {};
        }
    }

    // Topological sorting
    queue<int> q;
    for (int i = 0; i < 26; i++) {
        if (indegree[i] == 0) {
            q.push(i);
        }
    }
    vector<char> order;
    while (!q.empty()) {
        int u = q.front();
        q.pop();
        order.push_back(u + 'a');
        for (int v : graph[u]) {
            indegree[v]--;
            if (indegree[v] == 0) {
                q.push(v);
            }
        }
    }

    // If the order is invalid
    if (order.size() != 26) {
        return {};
    }
    return order;
}

int main() {
    vector<string> words = {"wrt", "wrf", "er", "ett", "rftt"};
    vector<char> order = alienOrder(words);
    for (char c : order) {
        cout << c;
    }
    return 0;
}
```

## Test Cases
```
Input: ["wrt", "wrf", "er", "ett", "rftt"]
Output: "wertf"
```

## Key Takeaways
- Use topological sorting to find the order of the letters in the alien alphabet.
- Build a graph where each node represents a letter, and there is an edge from node A to node B if A comes before B in the alien alphabet.
- Check for invalid orders by verifying that the length of the order is equal to 26 and that there are no cycles in the graph.