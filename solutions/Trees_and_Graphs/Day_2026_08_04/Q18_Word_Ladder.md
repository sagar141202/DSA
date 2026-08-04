# Word Ladder

## Problem Statement
Given two words (beginWord and endWord), and a dictionary's word list, find the length of the shortest transformation sequence from beginWord to endWord, such that:
- Only one letter can be changed at a time.
- Each intermediate word must exist in the dictionary.
- beginWord is not the same as endWord.
- If there is no transformation sequence, return 0.
For example, given:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
The output should be 5, as one of the shortest transformation sequences is: "hit" -> "hot" -> "dot" -> "dog" -> "cog".

## Approach
We can solve this problem using a Breadth-First Search (BFS) algorithm, where each word in the dictionary is a node, and two nodes are connected if they differ by one character. We start from the beginWord and explore all possible transformations level by level until we find the endWord.

## Complexity
- Time: O(N*M^2) where N is the number of words in the dictionary and M is the length of each word.
- Space: O(N) for storing the dictionary and the queue.

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int ladderLength(string beginWord, string endWord, vector<string>& wordList) {
        // Create a set for O(1) lookups
        unordered_set<string> wordSet(wordList.begin(), wordList.end());
        
        // If endWord is not in the dictionary, return 0
        if (wordSet.find(endWord) == wordSet.end()) {
            return 0;
        }
        
        // Initialize the queue with the beginWord
        queue<string> q;
        q.push(beginWord);
        
        // Initialize the distance to the beginWord as 1
        int distance = 1;
        
        // Perform BFS
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
                        if (wordSet.find(temp) != wordSet.end()) {
                            // Add the transformed word to the queue and remove it from the set
                            q.push(temp);
                            wordSet.erase(temp);
                        }
                    }
                }
            }
            // Increment the distance after exploring all words at the current level
            distance++;
        }
        
        // If there is no transformation sequence, return 0
        return 0;
    }
};
```

## Test Cases
```
Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
Output: 5
Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
Output: 0
```

## Key Takeaways
- Use a BFS algorithm to explore all possible transformations level by level.
- Use a set to store the dictionary for O(1) lookups and to avoid duplicates in the queue.
- Generate all possible transformations of each word by changing one character at a time.