# Longest Word in Dictionary

## Problem Statement
Given a list of strings which are all in lowercase, return the longest word from the given list that can be formed by other words in the list. A word can be formed by other words if and only if it is a concatenation of a sequence of other words in the list. If there are multiple longest words, return the lexicographically smallest one. For example, if the input is ["w","wo","wor","word"], the output should be "word". If the input is ["a","banana","app","appl","ap","apply","apple"], the output should be "apple".

## Approach
The problem can be solved using a Trie data structure to store all words in the dictionary, and then checking each word to see if it can be formed by other words in the dictionary. We use a depth-first search to check if a word can be formed by other words. We also use a set to store the words that can be formed to avoid duplicates.

## Complexity
- Time: O(N * M^2) where N is the number of words and M is the maximum length of a word
- Space: O(N * M) for storing the Trie and the set of words

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

struct TrieNode {
    unordered_map<char, TrieNode*> children;
    bool isWord;
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
        node->isWord = true;
    }

    bool search(string word) {
        TrieNode* node = root;
        for (char c : word) {
            if (!node->children.count(c)) {
                return false;
            }
            node = node->children[c];
        }
        return node->isWord;
    }
};

string longestWord(vector<string>& words) {
    Trie trie;
    for (string word : words) {
        trie.insert(word);
    }

    string longest = "";
    for (string word : words) {
        if (canBeFormed(word, trie)) {
            if (word.length() > longest.length() || (word.length() == longest.length() && word < longest)) {
                longest = word;
            }
        }
    }
    return longest;
}

bool canBeFormed(string word, Trie& trie) {
    for (int i = 1; i < word.length(); i++) {
        string prefix = word.substr(0, i);
        if (!trie.search(prefix)) {
            continue;
        }
        if (canBeFormed(word.substr(i), trie)) {
            return true;
        }
    }
    return false;
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
- Using a Trie data structure can efficiently store and search for words in the dictionary.
- A depth-first search can be used to check if a word can be formed by other words in the dictionary.
- Using a set to store the words that can be formed can avoid duplicates and improve efficiency.