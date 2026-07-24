# Longest Word in Dictionary

## Problem Statement
Given a list of strings which are all in lowercase, find the longest word that can be formed from other words in the list. If multiple words can be formed, return the longest one with the smallest lexicographical order. If no words can be formed, return an empty string. The input list will have at least one element and will not contain duplicates.

## Approach
The approach is to use a Trie data structure to store all the words in the dictionary, and then check each word to see if it can be formed from other words in the dictionary. We use a recursive function to check if a word can be formed from other words.

## Complexity
- Time: O(N * M) where N is the number of words and M is the maximum length of a word
- Space: O(N * M) for storing the Trie

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

struct TrieNode {
    unordered_map<char, TrieNode*> children;
    bool isWord;
};

class Solution {
public:
    string longestWord(vector<string>& words) {
        // Create a Trie and insert all words
        TrieNode* root = new TrieNode();
        for (string word : words) {
            TrieNode* node = root;
            for (char c : word) {
                if (node->children.find(c) == node->children.end()) {
                    node->children[c] = new TrieNode();
                }
                node = node->children[c];
            }
            node->isWord = true;
        }

        string longest = "";
        for (string word : words) {
            if (canBeFormed(root, word)) {
                if (word.length() > longest.length() || (word.length() == longest.length() && word < longest)) {
                    longest = word;
                }
            }
        }
        return longest;
    }

    bool canBeFormed(TrieNode* root, string word) {
        TrieNode* node = root;
        for (int i = 0; i < word.length(); i++) {
            if (node->children.find(word[i]) == node->children.end()) {
                return false;
            }
            node = node->children[word[i]];
            if (node->isWord && i < word.length() - 1) {
                if (!canBeFormed(root, word.substr(i + 1))) {
                    return false;
                }
            }
        }
        return true;
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
- Use a Trie data structure to efficiently store and check words
- Use a recursive function to check if a word can be formed from other words
- Always check the lexicographical order when there are multiple words with the same length