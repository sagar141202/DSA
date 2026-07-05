# Longest Word in Dictionary

## Problem Statement
Given a list of strings which are all in lowercase, find the longest word that can be formed using the other words in the list as prefixes. If there are multiple longest words, return the lexicographically smallest one. The list does not contain duplicates and all words are in lowercase. For example, given the list `["w","wo","wor","word"]`, the function should return `"word"` because it can be formed by the other words `["w","wo","wor"]` as prefixes.

## Approach
The approach to solve this problem is to use a Trie data structure to store all the words in the dictionary. Then, we iterate over each word in the dictionary and check if it can be formed by other words as prefixes by traversing the Trie.

## Complexity
- Time: O(N*M) where N is the number of words and M is the maximum length of a word
- Space: O(N*M) for storing the Trie

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class TrieNode {
public:
    unordered_map<char, TrieNode*> children;
    bool isEndOfWord;
    TrieNode() : isEndOfWord(false) {}
};

class Solution {
public:
    string longestWord(vector<string>& words) {
        // Create a Trie and insert all words
        TrieNode* root = new TrieNode();
        for (const string& word : words) {
            TrieNode* node = root;
            for (char c : word) {
                if (!node->children.count(c)) {
                    node->children[c] = new TrieNode();
                }
                node = node->children[c];
            }
            node->isEndOfWord = true;
        }
        
        // Find the longest word that can be formed by other words as prefixes
        string longest;
        for (const string& word : words) {
            TrieNode* node = root;
            bool isPrefix = true;
            for (int i = 0; i < word.size(); ++i) {
                char c = word[i];
                if (!node->children.count(c) || !node->children[c]->isEndOfWord) {
                    isPrefix = false;
                    break;
                }
                node = node->children[c];
            }
            if (isPrefix && word.size() > longest.size()) {
                longest = word;
            } else if (isPrefix && word.size() == longest.size() && word < longest) {
                longest = word;
            }
        }
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
- The Trie data structure is useful for problems involving prefixes and suffixes of strings.
- We need to carefully handle the case where there are multiple longest words and return the lexicographically smallest one.
- The time complexity of this solution is O(N*M) where N is the number of words and M is the maximum length of a word.