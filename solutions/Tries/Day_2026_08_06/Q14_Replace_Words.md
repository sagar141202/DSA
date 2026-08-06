# Replace Words

## Problem Statement
In this problem, we are given a sentence and a list of words to replace. We need to replace each word in the sentence with the shortest prefix from the list of words that is also a prefix of the word. If no such prefix exists, the word remains unchanged. The sentence is a string of words separated by spaces, and the list of words is an array of strings. For example, given the sentence "the cat and the dog" and the list of words ["cat", "dog", "the"], the output should be "the cat and the dog" because "the" is replaced with "the", "cat" is replaced with "cat", "and" remains unchanged, and "dog" is replaced with "dog".

## Approach
We will use a Trie data structure to store the list of words. Then, we will iterate over each word in the sentence and check if it has a prefix in the Trie. If it does, we replace the word with the shortest prefix.

## Complexity
- Time: O(n*m) where n is the number of words in the sentence and m is the maximum length of a word
- Space: O(k) where k is the total number of characters in the list of words

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class TrieNode {
public:
    unordered_map<char, TrieNode*> children;
    bool isEndOfWord;
    string word;

    TrieNode() : isEndOfWord(false) {}
};

class Solution {
public:
    string replaceWords(vector<string>& dictionary, string sentence) {
        TrieNode* root = new TrieNode();
        for (const auto& word : dictionary) {
            TrieNode* node = root;
            for (char c : word) {
                if (node->children.find(c) == node->children.end()) {
                    node->children[c] = new TrieNode();
                }
                node = node->children[c];
            }
            node->isEndOfWord = true;
            node->word = word;
        }

        istringstream iss(sentence);
        string word;
        string result;
        while (iss >> word) {
            TrieNode* node = root;
            string prefix;
            for (char c : word) {
                if (node->children.find(c) == node->children.end()) {
                    break;
                }
                prefix += c;
                node = node->children[c];
                if (node->isEndOfWord) {
                    break;
                }
            }
            if (node->isEndOfWord) {
                result += prefix + " ";
            } else {
                result += word + " ";
            }
        }
        result.pop_back(); // remove the last space
        return result;
    }
};

int main() {
    Solution solution;
    vector<string> dictionary = {"cat", "dog", "the"};
    string sentence = "the cat and the dog";
    cout << solution.replaceWords(dictionary, sentence) << endl;
    return 0;
}
```

## Test Cases
```
Input: dictionary = ["cat","bat","rat"], sentence = "the cattle was rattled by the battery"
Output: "the cat was rat by the bat"
```

## Key Takeaways
- Using a Trie data structure can efficiently store and retrieve prefixes of words.
- Iterating over each word in the sentence and checking for prefixes in the Trie can replace words with their shortest prefixes.