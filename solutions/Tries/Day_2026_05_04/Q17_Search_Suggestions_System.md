# Search Suggestions System

## Problem Statement
Given a list of strings `products` and a string `searchWord`, return a list of strings that match the search word in the following way: for each character in the search word, suggest all products from the list that start with the character sequence that has been typed so far. The results should be returned in lexicographical order, and no more than three results should be returned for each prefix of the search word. For example, if the search word is "mobile" and the list of products is ["mobile", "mouse", "moneypot", "monitor", "mousepad"], the output should be [["mobile", "moneypot", "monitor"], ["mobile", "moneypot", "monitor"], ["mobile", "mouse", "moneypot"], ["mobile", "mouse"], ["mouse", "mousepad"]].

## Approach
The problem can be solved using a Trie data structure, where each node in the Trie represents a prefix of the search word. We can store the products that match each prefix in the corresponding node. Then, for each character in the search word, we can traverse the Trie and return the products that match the current prefix.

## Complexity
- Time: O(n + m log m)
- Space: O(n + m)

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
        // Create a Trie node
        TrieNode* root = new TrieNode();
        
        // Insert products into the Trie
        for (string product : products) {
            TrieNode* node = root;
            for (char c : product) {
                if (node->children.find(c) == node->children.end()) {
                    node->children[c] = new TrieNode();
                }
                node = node->children[c];
                node->products.push_back(product);
                // Keep only the first three products for each prefix
                sort(node->products.begin(), node->products.end());
                if (node->products.size() > 3) {
                    node->products.resize(3);
                }
            }
        }
        
        vector<vector<string>> result;
        TrieNode* node = root;
        for (char c : searchWord) {
            if (node->children.find(c) == node->children.end()) {
                // If the character is not in the Trie, return empty vectors
                while (result.size() < searchWord.size()) {
                    result.push_back({});
                }
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
Output: [["mobile","moneypot","monitor"],["mobile","moneypot","monitor"],["mouse","moneypot","monitor"],["mouse","mousepad"],["mouse","mousepad"]]
```

## Key Takeaways
- Use a Trie data structure to store the products that match each prefix of the search word.
- Keep only the first three products for each prefix to meet the problem's requirements.
- Traverse the Trie for each character in the search word to get the products that match the current prefix.