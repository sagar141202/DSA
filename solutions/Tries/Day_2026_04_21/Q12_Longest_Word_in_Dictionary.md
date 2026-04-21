# Longest Word in Dictionary

## Problem Statement
Given a list of strings which are all in lowercase, return the longest word that can be formed by other words in the list. If there are multiple longest words, return the lexicographically smallest one. A word can only be formed by other words in the list if it can be split into a sequence of words where each word is in the list. For example, "cat" can be split into ["cat"] and "catsanddog" can be split into ["cat", "sand", "dog"].

## Approach
The problem can be solved by using a Trie data structure to store the given list of words, and then checking each word in the list to see if it can be formed by other words in the list. We use a recursive function to check if a word can be split into a sequence of words.

## Complexity
- Time: O(N * M) where N is the number of words and M is the average length of a word
- Space: O(N * M) for storing the Trie

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

struct TrieNode {
    unordered_map<char, TrieNode*> children;
    bool isEndOfWord;
};

class Trie {
public:
    TrieNode* root;
    Trie() {
        root = new TrieNode();
    }
    void insert(string word) {
        TrieNode* node = root;
        for (char c : word) {
            if (!node->children.count(c)) {
                node->children[c] = new TrieNode();
            }
            node = node->children[c];
        }
        node->isEndOfWord = true;
    }
    bool search(string word) {
        TrieNode* node = root;
        for (char c : word) {
            if (!node->children.count(c)) {
                return false;
            }
            node = node->children[c];
        }
        return node->isEndOfWord;
    }
};

class Solution {
public:
    string longestWord(vector<string>& words) {
        sort(words.begin(), words.end(), [](string a, string b) {
            return a.size() != b.size() ? a.size() < b.size() : a < b;
        });
        Trie trie;
        for (string word : words) {
            trie.insert(word);
        }
        string res = "";
        for (string word : words) {
            if (canBeFormed(word, trie)) {
                if (word.size() > res.size() || (word.size() == res.size() && word < res)) {
                    res = word;
                }
            }
        }
        return res;
    }
    bool canBeFormed(string word, Trie& trie) {
        if (word.empty()) {
            return true;
        }
        for (int i = 1; i <= word.size(); i++) {
            if (trie.search(word.substr(0, i)) && canBeFormed(word.substr(i), trie)) {
                return true;
            }
        }
        return false;
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
- We use a Trie to store the given list of words for efficient lookup.
- We sort the list of words by length and then lexicographically to ensure that we find the longest word that can be formed by other words.
- We use a recursive function to check if a word can be split into a sequence of words.