# Longest Word in Dictionary

## Problem Statement
Given a list of strings which are all in lowercase, return the longest word that can be formed by other words in the list. If multiple words can be formed, return the longest word with the highest alphabetical order. If no words can be formed, return an empty string. The list of words will contain at least one word and will not contain any duplicates. The length of each word will not exceed 1000 characters.

## Approach
We will use a Trie data structure to store all the words in the dictionary. Then, we will iterate over each word in the dictionary and check if it can be formed by other words in the Trie. We will keep track of the longest word that can be formed and return it as the result.

## Complexity
- Time: O(N * M) where N is the number of words and M is the maximum length of a word
- Space: O(N * M) for storing the Trie

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

struct TrieNode {
    unordered_map<char, TrieNode*> children;
    bool isEndOfWord;
    TrieNode() : isEndOfWord(false) {}
};

class Solution {
public:
    string longestWord(vector<string>& words) {
        TrieNode* root = new TrieNode();
        for (const string& word : words) {
            TrieNode* node = root;
            for (char c : word) {
                if (node->children.find(c) == node->children.end()) {
                    node->children[c] = new TrieNode();
                }
                node = node->children[c];
            }
            node->isEndOfWord = true;
        }

        string longest;
        function<bool(TrieNode*, string)> dfs = [&](TrieNode* node, string word) {
            if (!node->isEndOfWord) return false;
            if (word.size() > longest.size() || (word.size() == longest.size() && word > longest)) {
                longest = word;
            }
            for (auto& child : node->children) {
                dfs(child.second, word + child.first);
            }
            return true;
        };

        dfs(root, "");
        return longest;
    }
};
```

## Test Cases
```
Input: ["w","wo","wor","word"]
Output: "word"
Input: ["a","banana","app","appl","ap","apply","apple"]
Output: "apple"
```

## Key Takeaways
- Using a Trie data structure can efficiently store and query a large number of strings.
- Depth-First Search (DFS) can be used to traverse the Trie and find the longest word that can be formed by other words.
- Keeping track of the longest word found so far can help to return the correct result in case of multiple possible solutions.