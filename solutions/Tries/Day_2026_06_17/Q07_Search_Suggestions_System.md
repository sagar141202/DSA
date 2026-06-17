# Search Suggestions System

## Problem Statement
Given a list of strings `sentences` and a string `prefix`, design a search suggestions system that returns the top 3 most frequent sentences that start with the given `prefix`. The system should return the sentences in any order, but they must be the top 3 most frequent. If there are less than 3 sentences that start with the given `prefix`, return all of them. The `sentences` list and the `prefix` string will contain only lowercase English letters.

## Approach
The approach to solve this problem involves using a Trie data structure to store the sentences and their frequencies. We then traverse the Trie to find all sentences that start with the given prefix and sort them based on their frequencies.

## Complexity
- Time: O(N + MlogM) where N is the total number of characters in all sentences and M is the number of sentences that start with the given prefix.
- Space: O(N) where N is the total number of characters in all sentences.

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class TrieNode {
public:
    unordered_map<char, TrieNode*> children;
    string sentence;
    int frequency;
};

class Trie {
public:
    TrieNode* root;
    Trie() {
        root = new TrieNode();
    }

    void insert(string sentence) {
        TrieNode* node = root;
        for (char c : sentence) {
            if (node->children.find(c) == node->children.end()) {
                node->children[c] = new TrieNode();
            }
            node = node->children[c];
        }
        node->sentence = sentence;
        node->frequency++;
    }

    vector<string> startsWith(string prefix) {
        TrieNode* node = root;
        for (char c : prefix) {
            if (node->children.find(c) == node->children.end()) {
                return {};
            }
            node = node->children[c];
        }
        vector<pair<string, int>> sentences;
        dfs(node, sentences);
        sort(sentences.begin(), sentences.end(), [](auto& a, auto& b) {
            return a.second > b.second;
        });
        vector<string> result;
        for (int i = 0; i < min(3, (int)sentences.size()); i++) {
            result.push_back(sentences[i].first);
        }
        return result;
    }

    void dfs(TrieNode* node, vector<pair<string, int>>& sentences) {
        if (!node->sentence.empty()) {
            sentences.push_back({node->sentence, node->frequency});
        }
        for (auto& child : node->children) {
            dfs(child.second, sentences);
        }
    }
};

vector<string> suggestedProducts(vector<string>& products, string searchWord) {
    Trie trie;
    for (string product : products) {
        trie.insert(product);
    }
    vector<string> result;
    for (int i = 1; i <= searchWord.size(); i++) {
        string prefix = searchWord.substr(0, i);
        result.insert(result.end(), trie.startsWith(prefix).begin(), trie.startsWith(prefix).end());
    }
    return result;
}
```

## Test Cases
```
Input: products = ["mobile","mouse","moneypot","monitor","mousepad"], searchWord = "mouse"
Output: ["mobile","moneypot","monitor","mouse","mousepad","mouse"]
```

## Key Takeaways
- Using a Trie data structure can efficiently store and retrieve strings with common prefixes.
- The dfs function is used to traverse the Trie and find all sentences that start with a given prefix.
- Sorting the sentences based on their frequencies is necessary to return the top 3 most frequent sentences.