# Search Suggestions System

## Problem Statement
Given a list of strings `sentences` and a string `prefix`, return a list of strings that start with `prefix` in the order of their frequency in `sentences`. If there are multiple strings with the same frequency, return them in lexicographical order. The input `sentences` is a list of strings where each string is a sentence and the input `prefix` is a string. The output should be a list of strings that start with `prefix` and are ordered by their frequency in `sentences` and then by lexicographical order.

## Approach
The approach to solve this problem is to use a Trie data structure to store the sentences and then traverse the Trie to find the strings that start with the given prefix. We will also use a hashmap to store the frequency of each string.

## Complexity
- Time: O(N * M + K * logK)
- Space: O(N * M)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class TrieNode {
public:
    unordered_map<char, TrieNode*> children;
    string word;
};

class Solution {
public:
    vector<string> suggestedProducts(vector<string>& products, string searchWord) {
        TrieNode* root = new TrieNode();
        for (string product : products) {
            TrieNode* node = root;
            for (char c : product) {
                if (node->children.find(c) == node->children.end()) {
                    node->children[c] = new TrieNode();
                }
                node = node->children[c];
            }
            node->word = product;
        }
        
        vector<string> result;
        TrieNode* node = root;
        for (char c : searchWord) {
            if (node->children.find(c) == node->children.end()) {
                break;
            }
            node = node->children[c];
            vector<string> words;
            getWords(node, words);
            sort(words.begin(), words.end(), [](string a, string b) {
                return a < b;
            });
            int k = min(3, (int)words.size());
            for (int i = 0; i < k; i++) {
                result.push_back(words[i]);
            }
        }
        
        while (result.size() < searchWord.size()) {
            result.push_back("");
        }
        
        return result;
    }
    
    void getWords(TrieNode* node, vector<string>& words) {
        if (!node->word.empty()) {
            words.push_back(node->word);
        }
        for (auto child : node->children) {
            getWords(child.second, words);
        }
    }
};

int main() {
    Solution solution;
    vector<string> products = {"mobile", "mouse", "moneypot", "monitor", "mousepad"};
    string searchWord = "mouse";
    vector<string> result = solution.suggestedProducts(products, searchWord);
    for (string word : result) {
        cout << word << endl;
    }
    return 0;
}
```

## Test Cases
```
Input: products = ["mobile","mouse","moneypot","monitor","mousepad"], searchWord = "mouse"
Output: ["mobile","moneypot","monitor"]
Input: products = ["havana"], searchWord = "havana"
Output: ["havana","havana","havana","havana","havana","havana"]
```

## Key Takeaways
- Use a Trie data structure to store the sentences and then traverse the Trie to find the strings that start with the given prefix.
- Use a hashmap to store the frequency of each string.
- Sort the words in lexicographical order and return the top 3 words for each prefix.