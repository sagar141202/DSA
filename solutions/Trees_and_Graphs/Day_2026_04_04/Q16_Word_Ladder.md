# Word Ladder

## Problem Statement
The Word Ladder problem is a classic problem in the field of graph theory and artificial intelligence. Given two words (begin_word and end_word) and a dictionary of words, find the length of the shortest transformation sequence from begin_word to end_word. A transformation sequence is a sequence of words where each word is obtained by changing one character from the previous word, and each word in the sequence is present in the dictionary. If no such sequence exists, return 0. The constraints are: 1 <= begin_word.length <= 10, 1 <= end_word.length <= 10, begin_word and end_word consist of lowercase English letters, and dictionary contains only lowercase English letters.

## Approach
The algorithm uses a Breadth-First Search (BFS) approach to traverse the graph of words. It starts with the begin_word and explores all possible transformations by changing one character at a time. The BFS traversal ensures that the shortest transformation sequence is found.

## Complexity
- Time: O(N*M^2) where N is the number of words in the dictionary and M is the length of each word
- Space: O(N*M) for storing the queue and the set of visited words

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
            
            // Process each word in the current level
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
                        
                        // If the transformed word is in the wordSet and not visited
                        if (wordSet.find(temp) != wordSet.end() && visited.find(temp) == visited.end()) {
                            // Add the transformed word to the queue and mark it as visited
                            q.push(temp);
                            visited.insert(temp);
                        }
                    }
                }
            }
            
            // Increment the length of the transformation sequence
            length++;
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
- The Word Ladder problem can be solved using a BFS approach to find the shortest transformation sequence.
- The use of a set to store visited words ensures that each word is processed only once.
- The algorithm has a time complexity of O(N*M^2) and a space complexity of O(N*M), where N is the number of words in the dictionary and M is the length of each word.