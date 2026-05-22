# Longest Word in Dictionary

## Problem Statement
Given a list of strings which are all in lowercase, return the longest word that can be formed from other words in the list. If there are multiple such words, return the lexicographically largest one. For example, if the input is `["w","wo","wor","word"]`, the output should be `"word"`. If the input is `["a","banana","app","appl","ap","apply","apple"]`, the output should be `"apple"`. The length of each word is in the range `[1, 1000]` and the number of words in the input list is in the range `[1, 1000]`.

## Approach
We can use a Trie data structure to store the words in the list. Then, we can iterate over each word in the list and check if it can be formed from other words in the Trie. The word with the maximum length that can be formed from other words is the answer. We use a depth-first search approach to check if a word can be formed from other words in the Trie.

## Complexity
- Time: O(N * M) where N is the number of words and M is the maximum length of a word
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
    string longest;
    for (string word : words) {
        if (word.length() > longest.length() || (word.length() == longest.length() && word > longest)) {
            bool canBeFormed = true;
            for (int i = 1; i < word.length(); i++) {
                string prefix = word.substr(0, i);
                if (!trie.search(prefix)) {
                    canBeFormed = false;
                    break;
                }
            }
            if (canBeFormed) {
                longest = word;
            }
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
- Use a Trie data structure to store the words in the list.
- Iterate over each word in the list and check if it can be formed from other words in the Trie.
- The word with the maximum length that can be formed from other words is the answer.