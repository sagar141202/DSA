# Word Ladder

## Problem Statement
Given two words (`beginWord` and `endWord`), and a dictionary of words, find the length of the shortest transformation sequence from `beginWord` to `endWord` such that each word in the sequence is in the dictionary and only one character can be changed at a time. If no such sequence exists, return 0. The dictionary does not contain duplicates and contains only lowercase English letters. The length of each word is the same.

## Approach
The problem can be solved using a Breadth-First Search (BFS) algorithm, where each word is a node and two words are connected if they differ by one character. We start from the `beginWord` and explore all possible transformations until we reach the `endWord`.

## Complexity
- Time: O(N * M^2) where N is the number of words in the dictionary and M is the length of each word
- Space: O(N) for storing the words in the dictionary and the BFS queue

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int ladderLength(string beginWord, string endWord, vector<string>& wordList) {
        // Create a set of words for O(1) lookup
        unordered_set<string> wordSet(wordList.begin(), wordList.end());
        
        // If endWord is not in the dictionary, return 0
        if (wordSet.find(endWord) == wordSet.end()) {
            return 0;
        }
        
        // Initialize the BFS queue with the beginWord
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
                            // Add the transformation to the BFS queue
                            q.push(temp);
                            // Remove the transformation from the word set to avoid duplicates
                            wordSet.erase(temp);
                        }
                    }
                }
            }
            // Increment the distance after exploring all words at the current level
            distance++;
        }
        
        // If no transformation sequence is found, return 0
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
- Use a set to store the words in the dictionary for O(1) lookup.
- Use a queue to perform BFS and explore all possible transformations of each word.
- Remove each word from the set after exploring its transformations to avoid duplicates.