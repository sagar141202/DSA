# Alien Dictionary

## Problem Statement
There is a new alien language that uses the English alphabet, but the order of letters is unknown. You are given a list of words in this alien language, where each word is a valid English word. The task is to determine the correct order of the alphabet in this alien language. The constraints are: (1) the input list of words contains at least one word, (2) the length of each word is between 1 and 10, (3) the maximum number of words is 100, and (4) the maximum number of unique characters is 26. For example, given the words ["wrt", "wrf", "er", "ett", "rftt"], the correct order of the alphabet is "w-e-r-t-f" and then "t" is before "f" in this alien language.

## Approach
The algorithm uses a topological sorting approach to solve this problem. We create a graph where each character is a node, and a directed edge from node A to node B means that A comes before B in the alien dictionary. We then use a depth-first search or breadth-first search to perform the topological sorting.

## Complexity
- Time: O(N*M) where N is the number of words and M is the maximum length of a word
- Space: O(1) since the space complexity is constant with respect to the input size (at most 26 unique characters)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

vector<char> alienOrder(vector<string>& words) {
    // Create a graph where each character is a node
    unordered_map<char, unordered_set<char>> graph;
    unordered_map<char, int> indegree;
    
    // Populate the graph and indegree map
    for (int i = 0; i < words.size() - 1; i++) {
        string word1 = words[i];
        string word2 = words[i + 1];
        
        // Find the first different character
        int j = 0;
        while (j < word1.size() && j < word2.size() && word1[j] == word2[j]) {
            j++;
        }
        
        if (j < word1.size() && j < word2.size()) {
            // Add an edge from the character in word1 to the character in word2
            graph[word1[j]].insert(word2[j]);
            indegree[word2[j]]++;
        } else if (j == word1.size() && j < word2.size()) {
            // If word1 is a prefix of word2, we don't need to do anything
            continue;
        } else {
            // If word2 is a prefix of word1, the input is invalid
            return {};
        }
    }
    
    // Initialize a queue with nodes that have an indegree of 0
    queue<char> q;
    for (char c = 'a'; c <= 'z'; c++) {
        if (indegree.count(c) == 0) {
            q.push(c);
        }
    }
    
    // Perform the topological sorting
    vector<char> result;
    while (!q.empty()) {
        char c = q.front();
        q.pop();
        result.push_back(c);
        
        // Decrease the indegree of all neighbors of c
        for (char neighbor : graph[c]) {
            indegree[neighbor]--;
            if (indegree[neighbor] == 0) {
                q.push(neighbor);
            }
        }
    }
    
    // If the result size is not equal to the number of unique characters, the input is invalid
    if (result.size() != indegree.size()) {
        return {};
    }
    
    return result;
}

// Example usage:
int main() {
    vector<string> words = {"wrt", "wrf", "er", "ett", "rftt"};
    vector<char> result = alienOrder(words);
    for (char c : result) {
        cout << c;
    }
    return 0;
}
```

## Test Cases
```
Input: ["wrt", "wrf", "er", "ett", "rftt"]
Output: "wertf"
Input: ["z", "x"]
Output: "zx"
Input: ["z", "x", "z"]
Output: "" (invalid input)
```

## Key Takeaways
- Use a topological sorting approach to solve the alien dictionary problem.
- Create a graph where each character is a node, and a directed edge from node A to node B means that A comes before B in the alien dictionary.
- Use a queue to perform the topological sorting, starting with nodes that have an indegree of 0.