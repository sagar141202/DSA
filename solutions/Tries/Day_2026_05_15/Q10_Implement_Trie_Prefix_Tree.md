# Implement Trie (Prefix Tree)

## Problem Statement
Implement a Trie (Prefix Tree) data structure that supports the following operations: `insert`, `search`, and `startsWith`. The Trie should be able to store a collection of strings and provide efficient lookup, insertion, and prefix matching. The `insert` operation inserts a new string into the Trie, the `search` operation checks if a given string is in the Trie, and the `startsWith` operation checks if there is any string in the Trie that starts with a given prefix. The Trie should handle a large number of strings and provide fast lookup and insertion times.

## Approach
The algorithm uses a Trie data structure with nodes containing a boolean flag to mark the end of a word and a map to store child nodes. The `insert` operation iterates through the characters of the input string, creating new nodes as needed. The `search` and `startsWith` operations traverse the Trie based on the input string, checking for the presence of the string or prefix.

## Complexity
- Time: O(m) where m is the length of the input string
- Space: O(n*m) where n is the number of strings and m is the average length of the strings

## C++ Solution
```cpp
#include <unordered_map>
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
- Use an unordered_map to store child nodes for efficient lookup.
- Use a boolean flag to mark the end of a word.
- Traverse the Trie iteratively for `insert`, `search`, and `startsWith` operations.