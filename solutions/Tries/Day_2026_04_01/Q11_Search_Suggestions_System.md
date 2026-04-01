# Search Suggestions System

## Problem Statement
Given a list of strings `products` and a string `searchWord`, return a list of strings that match the search word as a prefix, sorted in lexicographical order. The search word is typed character by character, and after each character, a list of suggestions is provided. The task is to return a 2D list where each sublist contains the top three suggestions at each step.

## Approach
The approach to solve this problem is to use a Trie data structure to store the products and then traverse the Trie for each prefix of the search word to get the suggestions. We use a recursive function to build the Trie and a depth-first search (DFS) to get the suggestions.

## Complexity
- Time: O(n * m * 26) where n is the number of products and m is the maximum length of a product
- Space: O(n * m) for storing the Trie

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class TrieNode {
public:
    unordered_map<char, TrieNode*> children;
    vector<string> suggestions;
};

class Solution {
public:
    vector<vector<string>> suggestedProducts(vector<string>& products, string searchWord) {
        // Build the Trie
        TrieNode* root = new TrieNode();
        for (auto product : products) {
            TrieNode* node = root;
            for (char c : product) {
                if (node->children.find(c) == node->children.end()) {
                    node->children[c] = new TrieNode();
                }
                node = node->children[c];
                // Store the product in the node's suggestions
                node->suggestions.push_back(product);
                // Sort and limit the suggestions to 3
                sort(node->suggestions.begin(), node->suggestions.end());
                if (node->suggestions.size() > 3) {
                    node->suggestions.resize(3);
                }
            }
        }

        // Traverse the Trie for each prefix of the search word
        vector<vector<string>> result;
        TrieNode* node = root;
        for (char c : searchWord) {
            if (node->children.find(c) != node->children.end()) {
                node = node->children[c];
                result.push_back(node->suggestions);
            } else {
                // If the prefix is not found, return an empty list for the remaining characters
                while (result.size() < searchWord.size()) {
                    result.push_back({});
                }
                break;
            }
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
- Use a Trie data structure to efficiently store and retrieve the products based on prefixes.
- Use a recursive function to build the Trie and a DFS to get the suggestions.
- Sort and limit the suggestions to 3 at each node to improve performance.