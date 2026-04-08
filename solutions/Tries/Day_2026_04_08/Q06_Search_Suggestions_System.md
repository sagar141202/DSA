# Search Suggestions System

## Problem Statement
Given a list of strings `products` and a string `searchWord`, return a list of strings represented as a list of 2D char array, where each 2D char array contains suggestions for the `i`-th letter of `searchWord`. The suggestions should be a list of strings from `products` that start with the letters of `searchWord` up to the `i`-th letter.

## Approach
Use a Trie data structure to store the products, then for each prefix of the search word, traverse the Trie and find all matching products. The approach involves iterating over the search word, and for each prefix, finding all words in the Trie that start with that prefix.

## Complexity
- Time: O(n * m * 26^m) where n is the number of products and m is the length of the search word
- Space: O(n * m) for storing the Trie

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

struct TrieNode {
    unordered_map<char, TrieNode*> children;
    vector<string> words;
};

class Solution {
public:
    vector<vector<string>> suggestedProducts(vector<string>& products, string searchWord) {
        // Create the Trie and insert all products
        TrieNode* root = new TrieNode();
        for (string& product : products) {
            TrieNode* node = root;
            for (char c : product) {
                if (!node->children.count(c)) {
                    node->children[c] = new TrieNode();
                }
                node = node->children[c];
                node->words.push_back(product);
                // Keep only the first 3 suggestions
                sort(node->words.begin(), node->words.end());
                if (node->words.size() > 3) {
                    node->words.resize(3);
                }
            }
        }

        // Find suggestions for each prefix of the search word
        vector<vector<string>> result;
        TrieNode* node = root;
        for (char c : searchWord) {
            if (!node->children.count(c)) {
                // If the character is not in the Trie, return empty vectors
                vector<vector<string>> empty(searchWord.size() - result.size());
                result.insert(result.end(), empty.begin(), empty.end());
                break;
            }
            node = node->children[c];
            result.push_back(node->words);
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
- Keep track of the suggestions for each node in the Trie to avoid unnecessary computation.
- Sort the suggestions at each node to ensure they are in lexicographical order.