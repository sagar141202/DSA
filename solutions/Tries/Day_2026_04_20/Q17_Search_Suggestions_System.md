# Search Suggestions System

## Problem Statement
Given a list of strings and a prefix, design a search suggestions system that returns all strings in the list that start with the given prefix, sorted lexicographically. The system should be case-insensitive and return at most 3 suggestions for each prefix. For example, if the list of strings is ["abc", "abd", "abf", "xyz"] and the prefix is "ab", the system should return ["abc", "abd", "abf"].

## Approach
The approach is to use a Trie data structure to store the list of strings. Then, for each prefix, traverse the Trie to find all strings that start with the prefix. Finally, sort the suggestions lexicographically and return at most 3 of them. The use of a Trie allows for efficient prefix matching.

## Complexity
- Time: O(N + M), where N is the total length of all strings and M is the length of the prefix
- Space: O(N), where N is the total length of all strings

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

struct TrieNode {
    unordered_map<char, TrieNode*> children;
    vector<string> suggestions;
};

class Solution {
public:
    vector<vector<string>> suggestedProducts(vector<string>& products, string searchWord) {
        // Create a Trie and insert all products
        TrieNode* root = new TrieNode();
        for (const string& product : products) {
            TrieNode* node = root;
            for (char c : product) {
                if (node->children.find(c) == node->children.end()) {
                    node->children[c] = new TrieNode();
                }
                node = node->children[c];
            }
            node->suggestions.push_back(product);
        }

        // Traverse the Trie for each prefix of the search word
        vector<vector<string>> result;
        TrieNode* node = root;
        for (int i = 0; i < searchWord.size(); i++) {
            if (node->children.find(searchWord[i]) == node->children.end()) {
                break;
            }
            node = node->children[searchWord[i]];
            // Sort the suggestions and add at most 3 to the result
            sort(node->suggestions.begin(), node->suggestions.end());
            vector<string> suggestions;
            for (int j = 0; j < min(3, (int)node->suggestions.size()); j++) {
                suggestions.push_back(node->suggestions[j]);
            }
            result.push_back(suggestions);
        }

        // Add empty vectors for the remaining prefixes
        while (result.size() < searchWord.size()) {
            result.push_back({});
        }

        return result;
    }
};
```

## Test Cases
```
Input: products = ["mobile","mouse","moneypot","monitor","mousepad"], searchWord = "mouse"
Output: [["mobile","moneypot","monitor"],["mobile","moneypot","monitor"],["mouse","mousepad"],["mouse","mousepad"],["mouse","mousepad"]]
```

## Key Takeaways
- Use a Trie to efficiently store and retrieve strings with common prefixes.
- Traverse the Trie for each prefix of the search word to find matching strings.
- Sort the suggestions lexicographically and return at most 3 of them for each prefix.