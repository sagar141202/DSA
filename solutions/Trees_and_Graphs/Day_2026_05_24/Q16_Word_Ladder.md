# Word Ladder

## Problem Statement
Given two words, `beginWord` and `endWord`, and a dictionary of words, find the length of the shortest transformation sequence from `beginWord` to `endWord` such that each word in the sequence is in the dictionary and each word is a single edit away from the previous word. If there is no possible sequence, return 0. The dictionary is not guaranteed to contain either `beginWord` or `endWord`. The transformation sequence should only contain words from the dictionary.

## Approach
The algorithm uses a Breadth-First Search (BFS) approach to explore all possible transformations from the `beginWord`. It checks each word in the dictionary to see if it is a single edit away from the current word, and if so, adds it to the queue for further exploration. The process continues until the `endWord` is found or the queue is empty.

## Complexity
- Time: O(N * M^2), where N is the number of words in the dictionary and M is the length of each word
- Space: O(N * M), where N is the number of words in the dictionary and M is the length of each word

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int ladderLength(string beginWord, string endWord, vector<string>& wordList) {
        // Create a set of words for O(1) lookup
        unordered_set<string> wordSet(wordList.begin(), wordList.end());
        
        // Check if endWord is in the wordSet
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
                            q.push(temp);
                            wordSet.erase(temp);
                        }
                    }
                }
            }
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
- Use a BFS approach to explore all possible transformations from the `beginWord`.
- Use a set to store the words in the dictionary for O(1) lookup.
- Generate all possible transformations of the current word by replacing each character with all possible characters.