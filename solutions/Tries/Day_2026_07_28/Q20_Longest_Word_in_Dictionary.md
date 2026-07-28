# Longest Word in Dictionary

## Problem Statement
Given a list of strings which are all in lowercase, return the longest word that can be formed from other words in the list. If multiple words can be formed, return the longest one with the lexicographically smallest letters. The length of each word is between 3 and 10. The input list will not be empty and will contain at least one word that can be formed from other words. For example, given the list `["w","wo","wor","word"]`, the function should return `"word"`.

## Approach
The problem can be solved using a Trie data structure to store the given words and then checking each word to see if it can be formed from other words in the Trie. We will use a depth-first search approach to check for the existence of prefixes of each word.

## Complexity
- Time: O(N * M) where N is the number of words and M is the average length of a word
- Space: O(N * M) for storing the Trie

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

class Trie {
public:
    TrieNode* root;
    Trie() : root(new TrieNode()) {}
    
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

string longestWord(vector<string>& words) {
    Trie trie;
    for (string word : words) {
        trie.insert(word);
    }
    
    string longest;
    for (string word : words) {
        if (word.length() < 3) continue;
        bool canBeFormed = true;
        for (int i = 1; i < word.length(); i++) {
            string prefix = word.substr(0, i);
            if (!trie.search(prefix)) {
                canBeFormed = false;
                break;
            }
        }
        if (canBeFormed && (longest.empty() || word.length() > longest.length() || (word.length() == longest.length() && word < longest))) {
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
- We use a Trie data structure to store the given words for efficient prefix matching.
- We iterate through each word and check if it can be formed from other words by searching for prefixes in the Trie.
- We keep track of the longest word that can be formed and update it if we find a longer word or a word with the same length but lexicographically smaller.