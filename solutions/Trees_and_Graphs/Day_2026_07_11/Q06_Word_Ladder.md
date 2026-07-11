# Word Ladder

## Problem Statement
Given two words (`beginWord` and `endWord`), and a dictionary of words, find the length of the shortest transformation sequence from `beginWord` to `endWord` such that only one letter can be changed at a time and each intermediate word must exist in the dictionary. If there is no possible transformation, return 0. The transformation sequence should not contain the same word twice, and the words in the sequence should be in lowercase.

## Approach
The problem can be solved using a Breadth-First Search (BFS) algorithm, where each word is a node in the graph, and two nodes are connected if the corresponding words differ by one character. The BFS traversal starts from the `beginWord` and explores all possible transformations until it reaches the `endWord`.

## Complexity
- Time: O(N * M^2), where N is the number of words in the dictionary and M is the length of each word
- Space: O(N * M), for storing the words in the dictionary and the transformation sequence

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int ladderLength(string beginWord, string endWord, vector<string>& wordList) {
        // Create a set of words for efficient lookups
        unordered_set<string> wordSet(wordList.begin(), wordList.end());
        
        // Check if the endWord exists in the wordSet
        if (wordSet.find(endWord) == wordSet.end()) {
            return 0;
        }
        
        // Initialize the queue with the beginWord
        queue<string> q;
        q.push(beginWord);
        
        // Initialize the distance (number of transformations)
        int distance = 1;
        
        // Perform BFS traversal
        while (!q.empty()) {
            int size = q.size();
            for (int i = 0; i < size; i++) {
                string word = q.front();
                q.pop();
                
                // If the current word is the endWord, return the distance
                if (word == endWord) {
                    return distance;
                }
                
                // Generate all possible transformations of the current word
                for (int j = 0; j < word.size(); j++) {
                    string temp = word;
                    for (char c = 'a'; c <= 'z'; c++) {
                        temp[j] = c;
                        // Check if the transformed word exists in the wordSet
                        if (wordSet.find(temp) != wordSet.end()) {
                            // Add the transformed word to the queue and remove it from the wordSet
                            q.push(temp);
                            wordSet.erase(temp);
                        }
                    }
                }
            }
            // Increment the distance after each level of BFS traversal
            distance++;
        }
        
        // If there is no possible transformation, return 0
        return 0;
    }
};

int main() {
    Solution solution;
    string beginWord = "hit";
    string endWord = "cog";
    vector<string> wordList = {"hot", "dot", "dog", "lot", "log", "cog"};
    cout << solution.ladderLength(beginWord, endWord, wordList) << endl;
    return 0;
}
```

## Test Cases
```
Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
Output: 5
```

## Key Takeaways
- The Word Ladder problem can be solved using a BFS algorithm, which is suitable for finding the shortest path in an unweighted graph.
- The use of a set data structure allows for efficient lookups and removals of words during the BFS traversal.
- The algorithm generates all possible transformations of each word by replacing one character at a time, which ensures that the transformation sequence is valid according to the problem constraints.