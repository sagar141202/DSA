# Replace Words
## Problem Statement
In this problem, we are given a list of words and a sentence. The task is to replace all the words in the sentence with their corresponding abbreviations if they exist in the list. The abbreviation of a word is the word itself with all characters after the first character replaced with 'a'. For example, the abbreviation of "cat" would be "caaaaa...". We need to find the shortest possible abbreviation that uniquely identifies a word.

## Approach
We can solve this problem by using a Trie data structure to store the list of words. Then we iterate through each word in the sentence and check if it exists in the Trie. If it does, we find the shortest unique abbreviation for the word.

## Complexity
- Time: O(n*m) where n is the number of words in the list and m is the average length of a word
- Space: O(n*m) for storing the Trie

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;
using ll = long long;

struct TrieNode {
    unordered_map<char, TrieNode*> children;
    bool isEndOfWord;
};

class Trie {
public:
    TrieNode* root;

    Trie() {
        root = new TrieNode();
    }

    void insert(string word) {
        TrieNode* node = root;
        for (char c : word) {
            if (node->children.find(c) == node->children.end()) {
                node->children[c] = new TrieNode();
            }
            node = node->children[c];
        }
        node->isEndOfWord = true;
    }

    string getShortestUniqueAbbreviation(string word) {
        TrieNode* node = root;
        string abbreviation = "";
        for (char c : word) {
            abbreviation += c;
            node = node->children[c];
            if (node->children.size() == 0) {
                break;
            }
        }
        return abbreviation + string(word.size() - abbreviation.size(), 'a');
    }
};

string replaceWords(vector<string>& dictionary, string sentence) {
    Trie trie;
    for (string word : dictionary) {
        trie.insert(word);
    }

    istringstream iss(sentence);
    string word;
    string result = "";
    while (iss >> word) {
        string abbreviation = trie.getShortestUniqueAbbreviation(word);
        if (abbreviation != word + string(word.size(), 'a')) {
            result += abbreviation + " ";
        } else {
            result += word + " ";
        }
    }
    return result.substr(0, result.size() - 1);
}

int main() {
    vector<string> dictionary = {"cat", "bat", "rat"};
    string sentence = "the cattle was rattled by the battery";
    cout << replaceWords(dictionary, sentence) << endl;
    return 0;
}
```

## Test Cases
```
Input: dictionary = ["cat","bat","rat"], sentence = "the cattle was rattled by the battery"
Output: "the cat was rattled by the bat"
```

## Key Takeaways
- Using a Trie data structure allows us to efficiently store and retrieve words.
- The getShortestUniqueAbbreviation function in the Trie class helps us find the shortest unique abbreviation for a word.