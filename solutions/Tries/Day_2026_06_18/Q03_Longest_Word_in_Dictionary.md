# Longest Word in Dictionary

## Problem Statement
Given a list of strings which are all in lowercase, find the longest word that can be formed by other words in the list. The longest word should be the word that has the maximum length. If there are multiple words with the same maximum length, return the lexicographically smallest word. A word can be formed by other words if it can be constructed by concatenating other words in the list. For example, "cat" can be formed by "ca" and "t". The input list will not contain duplicate words.

## Approach
The approach is to use a Trie data structure to store all the words in the list. Then, for each word in the list, check if it can be formed by other words in the Trie. We can use a depth-first search to check if a word can be formed by other words.

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
    string longest = "";
    for (string word : words) {
        bool canBeFormed = true;
        for (int i = 1; i < word.size(); i++) {
            string prefix = word.substr(0, i);
            if (!trie.search(prefix)) {
                canBeFormed = false;
                break;
            }
        }
        if (canBeFormed && word.size() > longest.size()) {
            longest = word;
        } else if (canBeFormed && word.size() == longest.size() && word < longest) {
            longest = word;
        }
    }
    return longest;
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
- Use a Trie data structure to store all the words in the list for efficient lookup.
- Check if a word can be formed by other words by searching for prefixes in the Trie.
- Keep track of the longest word that can be formed by other words and update it if a longer word is found.