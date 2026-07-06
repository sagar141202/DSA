# Search Suggestions System

## Problem Statement
Given a list of strings `products` and a string `searchWord`, return a list of strings representing the search suggestions system. The search suggestions system is designed to return a list of strings that match the prefix of the `searchWord`. The list of strings should be sorted in lexicographical order. If there are more than 3 matching strings, return only the first 3. The `searchWord` can contain a '#' character, which is a special character that can be used to reset the search. When a '#' character is encountered, the search should start from the beginning of the `searchWord`.

## Approach
The approach is to use a Trie data structure to store the `products` and then traverse the Trie based on the `searchWord`. We will iterate over each character in the `searchWord` and find all the matching strings in the Trie.

## Complexity
- Time: O(n * m * 26) where n is the number of products and m is the maximum length of a product
- Space: O(n * m) where n is the number of products and m is the maximum length of a product

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
        // Create a Trie and insert all products
        TrieNode* root = new TrieNode();
        for (string product : products) {
            TrieNode* node = root;
            for (char c : product) {
                if (node->children.find(c) == node->children.end()) {
                    node->children[c] = new TrieNode();
                }
                node = node->children[c];
                // Add the product to the suggestions of the current node
                node->suggestions.push_back(product);
                // Sort the suggestions and keep only the first 3
                sort(node->suggestions.begin(), node->suggestions.end());
                if (node->suggestions.size() > 3) {
                    node->suggestions.resize(3);
                }
            }
        }

        // Traverse the Trie based on the searchWord
        vector<vector<string>> result;
        TrieNode* node = root;
        for (char c : searchWord) {
            if (c == '#') {
                // Reset the search
                node = root;
            } else {
                if (node->children.find(c) == node->children.end()) {
                    // If the character is not in the Trie, break the loop
                    break;
                }
                node = node->children[c];
                result.push_back(node->suggestions);
            }
        }

        // Add empty vectors for the remaining characters
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
- Use a Trie data structure to store the products and traverse it based on the searchWord.
- Keep track of the suggestions for each node in the Trie and sort them in lexicographical order.
- Use a '#' character to reset the search and start from the beginning of the searchWord.