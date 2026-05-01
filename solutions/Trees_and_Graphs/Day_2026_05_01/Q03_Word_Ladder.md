# Word Ladder

## Problem Statement
Given two words (`beginWord` and `endWord`), and a dictionary's word list, find the length of the shortest transformation sequence from `beginWord` to `endWord`, such that:
- Only one letter can be changed at a time.
- Each transformed word must exist in the dictionary.
- The transformation sequence must start with `beginWord` and end with `endWord`.
If there is no such transformation sequence, return 0.
Example: `beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]`, the output is `5` because one of the shortest transformation sequences is `"hit" -> "hot" -> "dot" -> "dog" -> "cog"`.

## Approach
The approach to solve this problem is to use a Breadth-First Search (BFS) algorithm to explore all possible transformations of the given word.
We will use a queue to keep track of the words to be processed and a set to keep track of the visited words.

## Complexity
- Time: O(N * M^2) where N is the number of words and M is the length of each word
- Space: O(N * M) for storing the queue and the set of visited words

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int ladderLength(string beginWord, string endWord, vector<string>& wordList) {
        // Create a set of words for O(1) lookup
        unordered_set<string> wordSet(wordList.begin(), wordList.end());
        
        // If the endWord is not in the wordSet, return 0
        if (wordSet.find(endWord) == wordSet.end()) {
            return 0;
        }
        
        // Create a queue for BFS and add the beginWord
        queue<string> q;
        q.push(beginWord);
        
        // Create a set to keep track of visited words
        unordered_set<string> visited;
        visited.insert(beginWord);
        
        // Initialize the length of the transformation sequence
        int length = 1;
        
        while (!q.empty()) {
            // Get the size of the queue
            int size = q.size();
            
            // Process each word at the current level
            for (int i = 0; i < size; i++) {
                string word = q.front();
                q.pop();
                
                // If the word is the endWord, return the length
                if (word == endWord) {
                    return length;
                }
                
                // Generate all possible transformations of the word
                for (int j = 0; j < word.size(); j++) {
                    string temp = word;
                    for (char c = 'a'; c <= 'z'; c++) {
                        temp[j] = c;
                        // If the transformed word is in the wordSet and not visited, add it to the queue
                        if (wordSet.find(temp) != wordSet.end() && visited.find(temp) == visited.end()) {
                            q.push(temp);
                            visited.insert(temp);
                        }
                    }
                }
            }
            
            // Increment the length of the transformation sequence
            length++;
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
- Use BFS to explore all possible transformations of the given word.
- Keep track of visited words to avoid infinite loops.
- Use a set to store the word list for O(1) lookup.