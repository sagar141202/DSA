# Search Suggestions System

## Problem Statement
Given a list of strings `products` and a string `searchWord`, return a list of strings that match the search word. The search word can be a prefix of a product name. The system returns the first three matching products for each prefix of the search word. For example, if the search word is "mobile" and the products are ["mobile", "mouse", "moneypot", "monitor", "mousepad"], the system should return [["mobile", "moneypot", "monitor"], ["mobile", "moneypot", "mouse"], ["mouse", "mobile", "moneypot"], ["mouse", "mobile", "monitor"], ["mouse", "mousepad", "moneypot"], ["mousepad"]]. If there are less than three matching products for a prefix, return all the matching products.

## Approach
The approach to solve this problem is to use a Trie data structure to store the products. Then, for each prefix of the search word, we can find the matching products by traversing the Trie. We will use a depth-first search to find all the matching products for each prefix.

## Complexity
- Time: O(n * m * 26^m) where n is the number of products and m is the length of the search word
- Space: O(n * m) where n is the number of products and m is the average length of a product name

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class TrieNode {
public:
    unordered_map<char, TrieNode*> children;
    vector<string> products;
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
                node->products.push_back(product);
                // Sort products at each node to ensure correct order
                sort(node->products.begin(), node->products.end());
                // Keep only the first three products at each node
                if (node->products.size() > 3) {
                    node->products.resize(3);
                }
            }
        }

        vector<vector<string>> result;
        TrieNode* node = root;
        for (char c : searchWord) {
            if (node->children.find(c) == node->children.end()) {
                // If the character is not in the Trie, break the loop
                break;
            }
            node = node->children[c];
            result.push_back(node->products);
        }

        // If the search word is longer than the result, add empty vectors
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
Output: [["mobile","moneypot","monitor"],["mobile","moneypot","mouse"],["mouse","mobile","moneypot"],["mouse","mobile","monitor"],["mouse","mousepad","moneypot"],["mousepad"]]
```

## Key Takeaways
- Use a Trie data structure to efficiently store and retrieve products based on prefixes.
- Sort products at each node in the Trie to ensure correct order.
- Keep only the first three products at each node to meet the problem's requirements.