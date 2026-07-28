# Search Suggestions System

## Problem Statement
Given a list of strings and a prefix, return all strings that start with the prefix in lexicographical order. The system should be case-insensitive and return at most three suggestions for each prefix. For example, if the input is `["mobile", "mouse", "moneypot", "monitor", "mousepad"]` and the prefix is `"mo"`, the output should be `["mobile", "moneypot", "monitor"]`. If the prefix is `"mouse"`, the output should be `["mouse", "mousepad"]`.

## Approach
The approach is to use a Trie data structure to store the given list of strings. Then, for each prefix, traverse the Trie to find all strings that start with the prefix and return at most three suggestions in lexicographical order.

## Complexity
- Time: O(n + m * 3) where n is the total number of characters in all strings and m is the number of prefixes.
- Space: O(n) where n is the total number of characters in all strings.

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

struct TrieNode {
    unordered_map<char, TrieNode*> children;
    bool isEndOfWord;
    string word;
};

class Solution {
public:
    vector<vector<string>> suggestedProducts(vector<string>& products, string searchWord) {
        // Create Trie and insert all products
        TrieNode* root = new TrieNode();
        for (string product : products) {
            TrieNode* node = root;
            for (char c : product) {
                if (!node->children.count(c)) {
                    node->children[c] = new TrieNode();
                }
                node = node->children[c];
            }
            node->isEndOfWord = true;
            node->word = product;
        }
        
        vector<vector<string>> result;
        TrieNode* node = root;
        for (int i = 0; i < searchWord.size(); i++) {
            char c = searchWord[i];
            if (!node->children.count(c)) {
                // If prefix is not found, return empty vector for remaining prefixes
                while (i < searchWord.size()) {
                    result.push_back({});
                    i++;
                }
                break;
            }
            node = node->children[c];
            vector<string> suggestions;
            dfs(node, suggestions);
            // Sort suggestions and get at most three
            sort(suggestions.begin(), suggestions.end());
            suggestions.resize(min(3, (int)suggestions.size()));
            result.push_back(suggestions);
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

int main() {
    Solution solution;
    vector<string> products = {"mobile", "mouse", "moneypot", "monitor", "mousepad"};
    string searchWord = "mouse";
    vector<vector<string>> result = solution.suggestedProducts(products, searchWord);
    for (vector<string> suggestions : result) {
        for (string suggestion : suggestions) {
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
Output: 
["mobile", "moneypot", "monitor"]
["mobile", "moneypot", "monitor"]
["mouse", "mousepad"]
["mouse", "mousepad"]
["mouse", "mousepad"]
```

## Key Takeaways
- Use a Trie data structure to efficiently store and retrieve strings based on prefixes.
- Traverse the Trie to find all strings that start with a given prefix and return at most three suggestions in lexicographical order.
- Use depth-first search (DFS) to traverse the Trie and find all strings that start with a given prefix.