# Search Suggestions System

## Problem Statement
Given a list of strings `sentences` and a string `prefix`, design a search suggestions system that returns the top 3 most frequent sentences that start with the given `prefix`. The frequency of a sentence is the number of times it appears in the `sentences` list. If there are less than 3 sentences that start with the given `prefix`, return all of them. The system should be case-insensitive and should ignore punctuation. For example, if `sentences = ["hello world", "hello", "hello world", "hello world"]` and `prefix = "hel"` then the output should be `["hello world", "hello world", "hello world"]`. If `sentences = ["hello world", "hello", "hello world", "hello world"]` and `prefix = "hel"` then the output should be `["hello world", "hello world", "hello world", "hello"]`.

## Approach
Use a Trie data structure to store the sentences and their frequencies. Then, use a priority queue to get the top 3 most frequent sentences that start with the given prefix. The Trie allows for efficient retrieval of sentences that start with a given prefix.

## Complexity
- Time: O(n log k) where n is the total number of characters in all sentences and k is the number of sentences that start with the given prefix
- Space: O(n) where n is the total number of characters in all sentences

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

struct TrieNode {
    unordered_map<char, TrieNode*> children;
    vector<string> sentences;
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
        node->sentences.push_back(sentence);
    }

    vector<string> search(string prefix) {
        TrieNode* node = root;
        for (char c : prefix) {
            if (node->children.find(c) == node->children.end()) {
                return {};
            }
            node = node->children[c];
        }
        vector<string> sentences;
        dfs(node, sentences);
        unordered_map<string, int> freq;
        for (string sentence : sentences) {
            freq[sentence]++;
        }
        priority_queue<pair<int, string>> pq;
        for (auto& it : freq) {
            pq.push({it.second, it.first});
        }
        vector<string> result;
        while (!pq.empty() && result.size() < 3) {
            result.push_back(pq.top().second);
            pq.pop();
        }
        return result;
    }

    void dfs(TrieNode* node, vector<string>& sentences) {
        for (string sentence : node->sentences) {
            sentences.push_back(sentence);
        }
        for (auto& it : node->children) {
            dfs(it.second, sentences);
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

int main() {
    vector<string> products = {"mobile", "mouse", "moneypot", "monitor", "mousepad"};
    string searchWord = "mouse";
    vector<vector<string>> result = suggestedProducts(products, searchWord);
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
Output: [["mobile", "moneypot", "monitor"], ["mobile", "moneypot", "monitor"], ["mouse", "mousepad"], ["mouse", "mousepad"], ["mouse", "mousepad"]]
```

## Key Takeaways
- Use a Trie data structure to store the sentences and their frequencies for efficient retrieval of sentences that start with a given prefix.
- Use a priority queue to get the top 3 most frequent sentences that start with the given prefix.
- The Trie allows for efficient retrieval of sentences that start with a given prefix, making the time complexity O(n log k) where n is the total number of characters in all sentences and k is the number of sentences that start with the given prefix.