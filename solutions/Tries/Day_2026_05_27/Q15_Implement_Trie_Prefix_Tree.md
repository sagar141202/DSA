# Implement Trie (Prefix Tree)

## Problem Statement
Implement a trie (prefix tree) with the following methods: `insert`, `search`, and `startsWith`. The trie should store strings, and the methods should return a boolean value indicating whether the string is in the trie or not. The `insert` method inserts a new string into the trie, the `search` method checks if a string is in the trie, and the `startsWith` method checks if there is any string in the trie that starts with the given prefix. The trie should handle a large number of strings and should be efficient in terms of time and space complexity. For example, given the strings ["apple", "app", "banana"], the `search` method should return `true` for "apple" and "app", but `false` for "ban". The `startsWith` method should return `true` for "app" and "ban", but `false` for "ora".

## Approach
The approach is to use a trie data structure, which is a tree-like data structure where each node stores a character and its child nodes store the next characters in the string. We will use a map to store the child nodes of each node, and a boolean flag to indicate whether a node is the end of a word.

## Complexity
- Time: O(m) where m is the length of the string
- Space: O(n*m) where n is the number of strings and m is the average length of the strings

## C++ Solution
```cpp
#include <unordered_map>
#include <string>

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

    bool startsWith(string prefix) {
        TrieNode* node = root;
        for (char c : prefix) {
            if (node->children.find(c) == node->children.end()) {
                return false;
            }
            node = node->children[c];
        }
        return true;
    }
};
```

## Test Cases
```
Input: 
Trie trie;
trie.insert("apple");
trie.insert("app");
trie.insert("banana");
Output: 
trie.search("apple") -> true
trie.search("app") -> true
trie.search("banana") -> true
trie.search("ban") -> false
trie.startsWith("app") -> true
trie.startsWith("ban") -> true
trie.startsWith("ora") -> false
```

## Key Takeaways
- The trie data structure is suitable for storing a large number of strings with common prefixes.
- The `insert`, `search`, and `startsWith` methods can be implemented efficiently using a trie.
- The time complexity of the methods is O(m) where m is the length of the string, and the space complexity is O(n*m) where n is the number of strings and m is the average length of the strings.