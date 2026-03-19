# Search Suggestions System

## Problem Statement
Given a list of strings `sentences` and a string `prefix`, return the top 3 most frequent sentences that start with the given `prefix`. If there are less than 3 sentences that start with the `prefix`, return all of them. The frequency of a sentence is the number of times it appears in the `sentences` list. If there is a tie in frequency, the sentence that appears earlier in the `sentences` list should be returned first. For example, given `sentences = ["abc", "abc", "abc", "def", "def"]` and `prefix = "abc"`, the output should be `["abc", "abc", "abc"]`. If `prefix = "def"`, the output should be `["def", "def"]`.

## Approach
The problem can be solved by first counting the frequency of each sentence, then filtering the sentences that start with the given prefix, and finally sorting them based on frequency and index. A trie data structure can be used to efficiently filter the sentences that start with the prefix.

## Complexity
- Time: O(n log n + m log m)
- Space: O(n + m)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

struct TrieNode {
    unordered_map<char, TrieNode*> children;
    bool isEndOfSentence;
};

struct Sentence {
    string sentence;
    int frequency;
    int index;
};

class Solution {
public:
    vector<string> suggestedProducts(vector<string>& products, string searchWord) {
        vector<string> result;
        TrieNode* root = new TrieNode();
        for (int i = 0; i < products.size(); i++) {
            TrieNode* node = root;
            for (char c : products[i]) {
                if (node->children.find(c) == node->children.end()) {
                    node->children[c] = new TrieNode();
                }
                node = node->children[c];
            }
            node->isEndOfSentence = true;
        }

        string prefix = "";
        for (char c : searchWord) {
            prefix += c;
            vector<Sentence> sentences;
            TrieNode* node = root;
            for (char cc : prefix) {
                if (node->children.find(cc) == node->children.end()) {
                    break;
                }
                node = node->children[cc];
            }
            if (node == nullptr) {
                result.push_back("");
                continue;
            }
            dfs(node, prefix, sentences);
            sort(sentences.begin(), sentences.end(), [](Sentence& a, Sentence& b) {
                if (a.frequency == b.frequency) {
                    return a.index < b.index;
                }
                return a.frequency > b.frequency;
            });
            vector<string> top3;
            for (int i = 0; i < min(3, (int)sentences.size()); i++) {
                top3.push_back(sentences[i].sentence);
            }
            result.push_back(top3[0]);
        }
        return result;
    }

    void dfs(TrieNode* node, string prefix, vector<Sentence>& sentences) {
        if (node->isEndOfSentence) {
            sentences.push_back({prefix, 1, 0});
        }
        for (auto& child : node->children) {
            dfs(child.second, prefix + child.first, sentences);
        }
    }
};

int main() {
    Solution solution;
    vector<string> products = {"mobile", "mouse", "moneypot", "monitor", "mousepad"};
    string searchWord = "mouse";
    vector<string> result = solution.suggestedProducts(products, searchWord);
    for (string str : result) {
        cout << str << endl;
    }
    return 0;
}
```

## Test Cases
```
Input: products = ["mobile", "mouse", "moneypot", "monitor", "mousepad"], searchWord = "mouse"
Output: ["mobile", "moneypot", "monitor"]
```

## Key Takeaways
- Use a trie data structure to efficiently filter the sentences that start with the given prefix.
- Use a depth-first search to traverse the trie and find all sentences that start with the prefix.
- Sort the sentences based on frequency and index to get the top 3 most frequent sentences.