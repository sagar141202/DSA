# Implement Trie (Prefix Tree)

## Problem Statement
Implement a Trie (Prefix Tree) data structure that supports the following operations: `insert`, `search`, and `startsWith`. The Trie should store a collection of strings and provide methods to check if a string is in the Trie, and if there is any string in the Trie that starts with a given prefix. The Trie should be case-sensitive and consider 'a' and 'A' as different characters. For example, given the strings "apple", "app", and "banana", the Trie should be able to correctly identify if "app" is a word in the Trie, if "banana" is a word in the Trie, and if there are any words that start with the prefix "ban".

## Approach
The approach to solving this problem is to create a Trie data structure using a nested unordered map to store the characters of the strings. Each node in the Trie will have a boolean flag to indicate if the node represents the end of a word. The `insert` operation will iterate through each character of the string and add it to the Trie if it doesn't exist. The `search` operation will also iterate through each character of the string and return true if the string is found in the Trie. The `startsWith` operation will return true if the prefix is found in the Trie.

## Complexity
- Time: O(m) where m is the length of the string for `insert`, `search`, and `startsWith` operations
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
cout << trie.search("apple") << endl;  // Output: 1 (true)
cout << trie.search("app") << endl;     // Output: 1 (true)
cout << trie.search("banana") << endl;   // Output: 1 (true)
cout << trie.search("ban") << endl;      // Output: 0 (false)
cout << trie.startsWith("ban") << endl;  // Output: 1 (true)
cout << trie.startsWith("app") << endl;  // Output: 1 (true)
```

## Key Takeaways
- Use a nested unordered map to store the characters of the strings in the Trie.
- Each node in the Trie should have a boolean flag to indicate if the node represents the end of a word.
- The `insert`, `search`, and `startsWith` operations should iterate through each character of the string and update the Trie accordingly.