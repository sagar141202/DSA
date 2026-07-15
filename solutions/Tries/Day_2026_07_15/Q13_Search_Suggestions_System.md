# Search Suggestions System

## Problem Statement
Given a list of strings `products` and a string `searchWord`, return a list of lists where each list contains the top 3 products that match the search word after each character is typed. The products should be sorted in lexicographical order. If there are less than 3 matching products, return all of them. If there are no matching products, return an empty list.

## Approach
We will use a Trie data structure to store the products and then perform a depth-first search to find the matching products. We will also maintain a priority queue to keep track of the top 3 matching products after each character is typed.

## Complexity
- Time: O(N * M * logM) where N is the number of products and M is the maximum length of a product
- Space: O(N * M) for storing the Trie and the priority queue

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class TrieNode {
public:
    unordered_map<char, TrieNode*> children;
    vector<string> words;
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
                node->words.push_back(product);
                // Keep only the top 3 words in lexicographical order
                sort(node->words.begin(), node->words.end());
                if (node->words.size() > 3) {
                    node->words.resize(3);
                }
            }
        }

        vector<vector<string>> result;
        TrieNode* node = root;
        for (char c : searchWord) {
            if (node->children.find(c) == node->children.end()) {
                // If no matching products, return empty list
                result.push_back({});
            } else {
                node = node->children[c];
                result.push_back(node->words);
            }
        }
        return result;
    }
};

int main() {
    Solution solution;
    vector<string> products = {"mobile", "mouse", "moneypot", "monitor", "mousepad"};
    string searchWord = "mouse";
    vector<vector<string>> result = solution.suggestedProducts(products, searchWord);
    for (const vector<string>& suggestions : result) {
        for (const string& suggestion : suggestions) {
            cout << suggestion << " ";
        }
        cout << endl;
    }
    return 0;
}
```

## Test Cases
```
Input: products = ["mobile", "mouse", "moneypot", "monitor", "mousepad"], searchWord = "mouse"
Output: [["mobile", "moneypot", "monitor"], ["mobile", "moneypot", "monitor"], ["mouse", "mousepad"], ["mouse", "mousepad"], ["mouse", "mousepad"]]
```

## Key Takeaways
- Use a Trie data structure to efficiently store and retrieve matching products
- Maintain a priority queue to keep track of the top 3 matching products after each character is typed
- Sort the matching products in lexicographical order to ensure correct results