# Implement Trie (Prefix Tree)

## Problem Statement
Implement a Trie (Prefix Tree) data structure that supports the following operations: `insert`, `search`, and `startsWith`. The Trie should store a collection of strings, and the `insert` operation should add a new string to the Trie. The `search` operation should return `true` if the string is in the Trie, and `false` otherwise. The `startsWith` operation should return `true` if there is any string in the Trie that starts with the given prefix, and `false` otherwise. The strings will only contain lowercase English letters.

## Approach
The algorithm uses a Trie data structure with a nested unordered map to store the child nodes. The `insert` operation iterates through each character in the string and adds a new node to the Trie if the character does not exist. The `search` and `startsWith` operations traverse the Trie based on the input string and return the result based on whether the string or prefix is found.

## Complexity
- Time: O(m) where m is the length of the string
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
private:
    TrieNode* root;

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
- Tries are suitable for tasks that involve frequent prefix matching, such as autocomplete and spell-checking.
- The time complexity of Trie operations is linear with respect to the length of the input string.
- The space complexity of a Trie can be high if the input strings are long or if there are many strings with common prefixes.