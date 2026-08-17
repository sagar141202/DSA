# Longest Word in Dictionary

## Problem Statement
Given a list of strings which contains a list of dictionary words, find the longest word in the dictionary that can be formed by removing characters from another string in the list while preserving the order of characters. For example, "abc" can be formed from "ahbgdc" but "acb" cannot. The function should return the longest word that can be formed in this manner.

## Approach
The algorithm uses a Trie data structure to store the dictionary words, and then checks each word in the list to see if it can be formed from another word in the list. The word with the maximum length that can be formed is returned. The Trie is used to efficiently check if a word is a subsequence of another word.

## Complexity
- Time: O(N*M) where N is the number of words in the dictionary and M is the maximum length of a word
- Space: O(N*M) for storing the Trie

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
            if (node->children.find(c) == node->children.end()) {
                node->children[c] = new TrieNode();
            }
            node = node->children[c];
        }
        node->isEndOfWord = true;
    }

    bool search(string word) {
        TrieNode* node = root;
        for (char c : word) {
            if (node->children.find(c) == node->children.end()) {
                return false;
            }
            node = node->children[c];
        }
        return node->isEndOfWord;
    }
};

string longestWord(vector<string>& words) {
    Trie trie;
    for (string word : words) {
        trie.insert(word);
    }

    string longest = "";
    for (string word : words) {
        bool canBeFormed = true;
        for (int i = 0; i < word.size(); i++) {
            string sub = word.substr(0, i+1);
            if (!trie.search(sub)) {
                canBeFormed = false;
                break;
            }
        }
        if (canBeFormed && word.size() > longest.size()) {
            longest = word;
        }
    }
    return longest;
}
```

## Test Cases
```
Input: ["w","wo","wor","word"]
Output: "word"

Input: ["a","banana","app","appl","ap","apply","apple"]
Output: "apple"
```

## Key Takeaways
- Tries can be used to efficiently store and retrieve strings with common prefixes.
- The problem can be solved by checking each word in the dictionary to see if it can be formed from another word in the list.
- The longest word that can be formed is returned as the result.