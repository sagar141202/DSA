# Word Ladder

## Problem Statement
Given two words (`beginWord` and `endWord`), and a dictionary's word list, find the length of the shortest transformation sequence from `beginWord` to `endWord`, such that:
- Only one letter can be changed at a time.
- Each intermediate word must exist in the dictionary.
- If there is no possible transformation, return 0.
For example, given `beginWord = "hit"`, `endWord = "cog"`, and `wordList = ["hot","dot","dog","lot","log","cog"]`, one possible transformation is `"hit" -> "hot" -> "dot" -> "dog" -> "cog"`, so the output is 5.

## Approach
We use a Breadth-First Search (BFS) algorithm to explore all possible transformations from the `beginWord`. We generate all possible words by changing one character at a time and check if the new word is in the dictionary.

## Complexity
- Time: O(N * M^2), where N is the number of words in the dictionary and M is the length of each word.
- Space: O(N * M), for storing the dictionary and the queue.

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
        int length = 1;
        
        // Perform BFS
        while (!q.empty()) {
            int size = q.size();
            for (int i = 0; i < size; i++) {
                string word = q.front();
                q.pop();
                
                // If we've reached the endWord, return the length
                if (word == endWord) {
                    return length;
                }
                
                // Generate all possible transformations of the current word
                for (int j = 0; j < word.size(); j++) {
                    string temp = word;
                    for (char c = 'a'; c <= 'z'; c++) {
                        temp[j] = c;
                        // If the new word is in the dictionary, add it to the queue and remove it from the dictionary
                        if (wordSet.find(temp) != wordSet.end()) {
                            q.push(temp);
                            wordSet.erase(temp);
                        }
                    }
                }
            }
            length++;
        }
        
        // If we've reached this point, there is no possible transformation
        return 0;
    }
};

int main() {
    Solution solution;
    string beginWord = "hit";
    string endWord = "cog";
    vector<string> wordList = {"hot","dot","dog","lot","log","cog"};
    cout << solution.ladderLength(beginWord, endWord, wordList) << endl;
    return 0;
}
```

## Test Cases
```
Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
Output: 5
Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
Output: 0
```

## Key Takeaways
- Use a BFS algorithm to explore all possible transformations from the `beginWord`.
- Use a set to store the dictionary for O(1) lookups.
- Generate all possible transformations of the current word by changing one character at a time.