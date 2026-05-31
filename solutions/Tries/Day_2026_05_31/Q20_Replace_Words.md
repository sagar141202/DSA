# Replace Words
## Problem Statement
In this problem, we are given a list of words in a dictionary and a sentence. We need to replace all the words in the sentence that are present in the dictionary with a shorter version. The shorter version of a word is the shortest prefix of the word that is not present in the dictionary. For example, if the word "cat" is present in the dictionary, its shorter version will be the shortest prefix of "cat" that is not present in the dictionary, which could be "ca" if "ca" is not in the dictionary. The task is to replace all the words in the sentence with their shorter versions.

## Approach
The approach to solve this problem is to use a Trie data structure to store the words in the dictionary. Then, for each word in the sentence, we check all its prefixes in the Trie and find the shortest prefix that is not present in the Trie. We replace the word with this shortest prefix.

## Complexity
- Time: O(N * M) where N is the number of words in the sentence and M is the maximum length of a word
- Space: O(N * M) for storing the Trie

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class TrieNode {
public:
    unordered_map<char, TrieNode*> children;
    bool endOfWord;
    TrieNode() : endOfWord(false) {}
};

class Trie {
public:
    TrieNode* root;
    Trie() : root(new TrieNode()) {}
    void insert(string word) {
        TrieNode* node = root;
        for (char c : word) {
            if (node->children.find(c) == node->children.end()) {
                node->children[c] = new TrieNode();
            }
            node = node->children[c];
        }
        node->endOfWord = true;
    }
    string getShortestPrefix(string word) {
        TrieNode* node = root;
        string prefix = "";
        for (char c : word) {
            prefix += c;
            if (node->children.find(c) == node->children.end() || node->endOfWord) {
                return prefix;
            }
            node = node->children[c];
        }
        return word;
    }
};

string replaceWords(vector<string>& dictionary, string sentence) {
    Trie trie;
    for (string word : dictionary) {
        trie.insert(word);
    }
    stringstream ss(sentence);
    string word, result = "";
    while (ss >> word) {
        result += trie.getShortestPrefix(word) + " ";
    }
    return result.substr(0, result.size() - 1);
}

int main() {
    vector<string> dictionary = {"cat","bat","rat"};
    string sentence = "the cattle was rattled by the battery";
    cout << replaceWords(dictionary, sentence) << endl;
    return 0;
}
```

## Test Cases
```
Input: dictionary = ["cat","bat","rat"], sentence = "the cattle was rattled by the battery"
Output: "the cat was rat by the bat"
```

## Key Takeaways
- We use a Trie data structure to efficiently store and query the dictionary words.
- We iterate through each word in the sentence and find its shortest prefix that is not present in the Trie.
- The time complexity of the solution is O(N * M) where N is the number of words in the sentence and M is the maximum length of a word.