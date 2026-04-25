# Longest Word in Dictionary

## Problem Statement
Given a list of strings which are all in lowercase, find the longest word that can be formed from other words in the list. A word can be formed from other words if it can be constructed by concatenating other words in the list. If there are multiple longest words, return the lexicographically smallest one. For example, given the list ["w","wo","wor","word"], the longest word that can be formed is "word".

## Approach
The approach is to use a Trie data structure to store the words in the list, then check each word to see if it can be formed from other words in the Trie. We use a recursive function to check if a word can be formed from other words.

## Complexity
- Time: O(N * M) where N is the number of words and M is the maximum length of a word
- Space: O(N * M) where N is the number of words and M is the maximum length of a word

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
        if (trie.search(prefix) && canBeFormed(word.substr(i), trie)) {
            return true;
        }
    }
    return false;
}

int main() {
    vector<string> words = {"w","wo","wor","word"};
    cout << longestWord(words) << endl;
    return 0;
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
- We use a Trie data structure to store the words in the list.
- We check each word to see if it can be formed from other words in the Trie using a recursive function.
- We keep track of the longest word that can be formed and return it as the result.