# Search Suggestions System

## Problem Statement
Given a list of strings `sentences` and a string `prefix`, design a search suggestions system that returns the top 3 most frequent sentences that start with the given `prefix`. The frequency of a sentence is the number of times it appears in the `sentences` list. If there are less than 3 sentences that start with the `prefix`, return all of them. The output should be in descending order of frequency.

## Approach
The approach to solve this problem is to use a Trie data structure to store the sentences and their frequencies, then traverse the Trie to find the sentences that start with the given prefix. We use a hashmap to store the frequency of each sentence.

## Complexity
- Time: O(n + m log m)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class TrieNode {
public:
    unordered_map<char, TrieNode*> children;
    bool isEndOfSentence;
    string sentence;
    int frequency;

    TrieNode() : isEndOfSentence(false), frequency(0) {}
};

class Trie {
public:
    TrieNode* root;

    Trie() : root(new TrieNode()) {}

    void insert(string sentence) {
        TrieNode* node = root;
        for (char c : sentence) {
            if (!node->children.count(c)) {
                node->children[c] = new TrieNode();
            }
            node = node->children[c];
        }
        node->isEndOfSentence = true;
        node->sentence = sentence;
        node->frequency++;
    }

    vector<string> search(string prefix) {
        TrieNode* node = root;
        for (char c : prefix) {
            if (!node->children.count(c)) {
                return {};
            }
            node = node->children[c];
        }

        vector<pair<string, int>> sentences;
        dfs(node, sentences);

        sort(sentences.begin(), sentences.end(), [](const auto& a, const auto& b) {
            return a.second > b.second;
        });

        vector<string> result;
        for (int i = 0; i < min(3, (int)sentences.size()); i++) {
            result.push_back(sentences[i].first);
        }
        return result;
    }

    void dfs(TrieNode* node, vector<pair<string, int>>& sentences) {
        if (node->isEndOfSentence) {
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
        vector<string> suggestions = trie.search(prefix);
        result.push_back(suggestions);
    }
    return result;
}
```

## Test Cases
```
Input: products = ["mobile","mouse","moneypot","monitor","mousepad"], searchWord = "mouse"
Output: [["mobile","moneypot","monitor"],["mobile","moneypot","monitor"],["mouse","mousepad"],["mouse","mousepad"],["mouse","mousepad"]]
```

## Key Takeaways
- Use a Trie data structure to store the sentences and their frequencies.
- Traverse the Trie to find the sentences that start with the given prefix.
- Use a hashmap to store the frequency of each sentence.