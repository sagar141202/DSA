# Word Ladder

## Problem Statement
Given two words (`beginWord` and `endWord`), and a dictionary of words, find the length of the shortest transformation sequence from `beginWord` to `endWord`, such that each word in the sequence is in the dictionary and each word is a transformation of the previous word by changing one letter at a time. If no transformation sequence is possible, return 0. For example, given `beginWord = "hit"`, `endWord = "cog"`, and `wordList = ["hot","dot","dog","lot","log","cog"]`, the output should be `5` because one possible transformation sequence is `"hit" -> "hot" -> "dot" -> "dog" -> "cog"`.

## Approach
The algorithm uses a Breadth-First Search (BFS) approach to explore all possible transformations of the current word. It generates all possible words that can be formed by changing one letter of the current word and checks if the generated word is in the dictionary. If it is, it adds the word to the queue for further exploration.

## Complexity
- Time: O(N * M^2) where N is the number of words in the dictionary and M is the length of each word
- Space: O(N * M) for storing the dictionary and the queue

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int ladderLength(string beginWord, string endWord, vector<string>& wordList) {
        // Create a set of words for O(1) lookup
        unordered_set<string> wordSet(wordList.begin(), wordList.end());
        
        // If endWord is not in the wordSet, return 0
        if (wordSet.find(endWord) == wordSet.end()) {
            return 0;
        }
        
        // Create a queue for BFS and add the beginWord
        queue<string> q;
        q.push(beginWord);
        
        // Create a set to store visited words
        unordered_set<string> visited;
        visited.insert(beginWord);
        
        // Initialize the length of the transformation sequence
        int length = 1;
        
        while (!q.empty()) {
            // Get the size of the current level
            int size = q.size();
            
            // Process all words at the current level
            for (int i = 0; i < size; i++) {
                string word = q.front();
                q.pop();
                
                // If the current word is the endWord, return the length
                if (word == endWord) {
                    return length;
                }
                
                // Generate all possible transformations of the current word
                for (int j = 0; j < word.size(); j++) {
                    string temp = word;
                    
                    // Try all possible characters
                    for (char c = 'a'; c <= 'z'; c++) {
                        temp[j] = c;
                        
                        // If the generated word is in the wordSet and not visited, add it to the queue
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
        
        // If no transformation sequence is possible, return 0
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
- Use a BFS approach to explore all possible transformations of the current word.
- Use a set to store visited words to avoid revisiting them.
- Generate all possible transformations of the current word by changing one letter at a time.