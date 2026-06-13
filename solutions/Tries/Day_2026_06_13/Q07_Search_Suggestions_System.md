# Search Suggestions System

## Problem Statement
Given a list of strings, implement a search suggestions system that returns all strings in the list that start with a given prefix. The system should return at most 3 suggestions for each character typed. For example, if the list of strings is ["mobile", "mouse", "moneypot", "monitor", "mousepad"] and the prefix is "mo", the system should return ["mobile", "moneypot", "monitor"]. If the prefix is "mouse", the system should return ["mouse", "mousepad"]. The input list of strings is not empty and contains only lowercase English letters. The length of each string does not exceed 10 characters.

## Approach
We will use a trie data structure to store the list of strings, and then traverse the trie to find all strings that start with the given prefix. We will keep track of the number of suggestions found and stop once we have found 3 suggestions.

## Complexity
- Time: O(N * M) where N is the number of strings and M is the maximum length of a string
- Space: O(N * M) where N is the number of strings and M is the maximum length of a string

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class TrieNode {
public:
    unordered_map<char, TrieNode*> children;
    bool isEndOfWord;
    string word;

    TrieNode() : isEndOfWord(false) {}
};

class Solution {
public:
    vector<vector<string>> suggestedProducts(vector<string>& products, string searchWord) {
        // Create a trie and insert all products into it
        TrieNode* root = new TrieNode();
        for (const auto& product : products) {
            TrieNode* node = root;
            for (char c : product) {
                if (node->children.find(c) == node->children.end()) {
                    node->children[c] = new TrieNode();
                }
                node = node->children[c];
            }
            node->isEndOfWord = true;
            node->word = product;
        }

        // Search for suggestions
        vector<vector<string>> result;
        TrieNode* node = root;
        for (char c : searchWord) {
            if (node->children.find(c) == node->children.end()) {
                break;
            }
            node = node->children[c];

            // Find all suggestions starting from the current node
            vector<string> suggestions;
            dfs(node, suggestions);
            // Sort suggestions and keep only the first 3
            sort(suggestions.begin(), suggestions.end());
            suggestions.resize(3);
            result.push_back(suggestions);
        }

        // Fill the result with empty vectors if the search word is longer than the suggestions
        while (result.size() < searchWord.size()) {
            result.push_back({});
        }

        return result;
    }

    void dfs(TrieNode* node, vector<string>& suggestions) {
        if (node->isEndOfWord) {
            suggestions.push_back(node->word);
        }
        for (auto& child : node->children) {
            dfs(child.second, suggestions);
        }
    }
};
```

## Test Cases
```
Input: products = ["mobile","mouse","moneypot","monitor","mousepad"], searchWord = "mouse"
Output: [["mobile","moneypot","monitor"],["mobile","moneypot","monitor"],["mouse","mousepad"],["mouse","mousepad"],["mouse","mousepad"]]
```

## Key Takeaways
- The trie data structure is useful for storing and searching a large list of strings with common prefixes.
- The dfs function is used to traverse the trie and find all strings that start with a given prefix.
- The result is sorted and limited to the first 3 suggestions for each character typed.