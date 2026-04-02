# Search Suggestions System

## Problem Statement
Given a list of strings and a prefix, design a search suggestions system that returns all strings in the list that start with the given prefix, sorted lexicographically. The system should be able to handle a large number of strings and prefixes efficiently. For example, if the list of strings is ["mobile", "mouse", "moneypot", "monitor", "mousepad"] and the prefix is "mouse", the system should return ["mouse", "mousepad"]. The prefix can be any substring of the strings in the list.

## Approach
The problem can be solved using a Trie data structure, where each node stores a list of strings that pass through it. The algorithm iterates over each string in the list, inserts it into the Trie, and then uses the Trie to find all strings that start with the given prefix.

## Complexity
- Time: O(N * M + P * M), where N is the number of strings, M is the maximum length of a string, and P is the number of prefixes.
- Space: O(N * M), where N is the number of strings and M is the maximum length of a string.

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class TrieNode {
public:
    unordered_map<char, TrieNode*> children;
    vector<string> words;
};

class SearchSuggestionsSystem {
public:
    TrieNode* root;

    SearchSuggestionsSystem() {
        root = new TrieNode();
    }

    void insert(string word) {
        TrieNode* node = root;
        for (char c : word) {
            if (node->children.find(c) == node->children.end()) {
                node->children[c] = new TrieNode();
            }
            node = node->children[c];
            node->words.push_back(word);
        }
    }

    vector<string> search(string prefix) {
        TrieNode* node = root;
        for (char c : prefix) {
            if (node->children.find(c) == node->children.end()) {
                return {};
            }
            node = node->children[c];
        }
        sort(node->words.begin(), node->words.end());
        return node->words;
    }
};

int main() {
    SearchSuggestionsSystem system;
    vector<string> words = {"mobile", "mouse", "moneypot", "monitor", "mousepad"};
    for (string word : words) {
        system.insert(word);
    }
    string prefix = "mouse";
    vector<string> result = system.search(prefix);
    for (string word : result) {
        cout << word << " ";
    }
    return 0;
}
```

## Test Cases
```
Input: words = ["mobile", "mouse", "moneypot", "monitor", "mousepad"], prefix = "mouse"
Output: ["mouse", "mousepad"]
Input: words = ["havana"], prefix = "havana"
Output: ["havana"]
Input: words = ["bag", "baggage", "basket", "box"], prefix = "bag"
Output: ["bag", "baggage"]
```

## Key Takeaways
- Tries can be used to efficiently store and retrieve strings with common prefixes.
- The Trie data structure can be used to solve a variety of string-related problems, such as autocomplete and spell-checking.
- The time complexity of the Trie operations (insert and search) depends on the length of the strings and the number of strings, making it suitable for large datasets.