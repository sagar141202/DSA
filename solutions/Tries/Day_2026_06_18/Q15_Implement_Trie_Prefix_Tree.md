# Implement Trie (Prefix Tree)

## Problem Statement
Implement a Trie (Prefix Tree) data structure that supports the following operations: `insert`, `search`, and `startsWith`. The Trie should store a collection of strings, and the operations should be performed efficiently. The constraints are: 1 <= word.length <= 10, word consists of lowercase English letters, and the maximum number of operations is 10^4. For example, if we insert the words "apple", "app", and "banana" into the Trie, then searching for "app" should return True, searching for "banana" should return True, and searching for "ban" should return False.

## Approach
The algorithm uses a Trie data structure with a nested map to store the child nodes and a boolean flag to mark the end of a word. The `insert` operation iterates through the characters of the word, creating new nodes if necessary. The `search` and `startsWith` operations traverse the Trie based on the input string.

## Complexity
- Time: O(m) where m is the length of the word
- Space: O(n*m) where n is the number of words and m is the average length of the words

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
["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
[[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
Output: 
[null, null, true, false, true, null, true]
```

## Key Takeaways
- Tries are suitable for storing a collection of strings and performing prefix-based operations efficiently.
- The Trie data structure uses a nested map to store the child nodes, allowing for fast lookups and insertions.
- The `insert`, `search`, and `startsWith` operations have a time complexity of O(m), where m is the length of the word.