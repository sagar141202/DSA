# Implement Trie (Prefix Tree)

## Problem Statement
Implement a trie (prefix tree) data structure, which is a tree-like data structure in which every node stores a string. The trie has methods to insert a string, search for a string, and check if a prefix exists. The constraints are that the trie should support lowercase English letters only, and all strings are non-empty. For example, if we insert "apple" and "app", we can then search for "apple" and it should return True, but searching for "ap" should return False. Checking if "app" is a prefix should return True.

## Approach
The algorithm uses a trie data structure with a nested Node class to represent each node in the trie. Each node contains a boolean flag to mark the end of a word and a map to store child nodes. The insert, search, and startsWith methods are implemented using recursive or iterative approaches.

## Complexity
- Time: O(m) where m is the length of the string for insert, search, and startsWith operations
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
trie.search("apple") -> True
trie.search("app") -> True
trie.search("ap") -> False
trie.search("banana") -> True
trie.startsWith("app") -> True
trie.startsWith("ap") -> True
trie.startsWith("ban") -> True
```

## Key Takeaways
- The trie data structure is useful for tasks that require frequent prefix matching, such as autocomplete and spell-checking.
- The time complexity of the insert, search, and startsWith operations in the trie is O(m), where m is the length of the input string.
- The space complexity of the trie is O(n*m), where n is the number of strings and m is the average length of the strings.