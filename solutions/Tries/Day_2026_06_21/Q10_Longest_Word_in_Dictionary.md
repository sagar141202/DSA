# Longest Word in Dictionary

## Problem Statement
Given a list of strings which are all in lowercase, return the longest word that can be formed using the other words in the list. The longest word should be in the list and it should be possible to construct it from other words in the list. If there are multiple possible results, return the longest word with the smallest lexicographical order. If no such word exists, return an empty string. For example, given the list `["w","wo","wor","word"]`, the function should return `"word"` because it can be formed by `"w"`, `"wo"`, and `"wor"`.

## Approach
The approach is to use a Trie data structure to store all the words in the list. Then, we iterate through each word in the list and check if it can be formed by other words in the list by querying the Trie. We keep track of the longest word that can be formed and return it.

## Complexity
- Time: O(NM) where N is the number of words and M is the maximum length of a word
- Space: O(NM) for storing the Trie

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class TrieNode {
public:
    unordered_map<char, TrieNode*> children;
    bool isWord;
    TrieNode() : isWord(false) {}
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
- Use a Trie data structure to store all the words in the list for efficient querying.
- Iterate through each word in the list and check if it can be formed by other words in the list by querying the Trie.
- Keep track of the longest word that can be formed and return it. If there are multiple possible results, return the longest word with the smallest lexicographical order.