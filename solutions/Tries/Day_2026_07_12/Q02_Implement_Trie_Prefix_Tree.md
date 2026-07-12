# Implement Trie (Prefix Tree)

## Problem Statement
Implement a Trie (Prefix Tree) data structure that supports the following operations: `insert(String word)`, `search(String word)`, and `startsWith(String prefix)`. The Trie should store a dynamic set of strings, where each string is composed of lowercase English letters. The `insert` operation adds a new string to the Trie, the `search` operation checks if a given string is present in the Trie, and the `startsWith` operation checks if there is any string in the Trie that starts with the given prefix. The Trie should be case-sensitive and should handle duplicate strings.

## Approach
The algorithm uses a nested hashmap to represent the Trie, where each node is a hashmap that maps characters to child nodes. The `insert` operation iterates through each character in the word, creating new nodes as necessary. The `search` and `startsWith` operations use a similar approach, traversing the Trie based on the input string or prefix.

## Complexity
- Time: O(m), where m is the length of the input string or prefix
- Space: O(n*m), where n is the number of strings in the Trie and m is the average length of the strings

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

private:
    TrieNode* root;
};
```

## Test Cases
```
Input: Trie trie; trie.insert("apple"); trie.insert("app"); trie.insert("banana")
Output: trie.search("apple") -> true, trie.search("app") -> true, trie.search("banana") -> true, trie.search("ban") -> false
Input: trie.startsWith("app")
Output: true
Input: trie.startsWith("ban")
Output: true
Input: trie.startsWith("ora")
Output: false
```

## Key Takeaways
- Tries are useful for storing and retrieving strings with common prefixes.
- The `insert` operation can be optimized by reusing existing nodes in the Trie.
- The `search` and `startsWith` operations can be optimized by pruning the search space based on the input string or prefix.