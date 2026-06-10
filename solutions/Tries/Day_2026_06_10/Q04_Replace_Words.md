# Replace Words

## Problem Statement
In this problem, we are given a list of words and a sentence. We need to replace all the words in the sentence that are present in the list with a special character, say '#'. The replacement should be done such that the word is replaced as a whole and not as a part of another word. For example, if we have a list of words ["cat", "bat", "rat"] and a sentence "the cat sat on the mat", the output should be "the # sat on the mat". The constraints are that the list of words and the sentence are non-empty and contain only lowercase English letters.

## Approach
The approach to solve this problem is to use a Trie data structure to store the list of words. We then iterate over each word in the sentence and check if it is present in the Trie. If it is, we replace it with '#'. We use a Trie to efficiently check for the presence of words in the list.

## Complexity
- Time: O(N + M) where N is the number of words in the list and M is the number of words in the sentence.
- Space: O(N) for storing the Trie.

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class TrieNode {
public:
    unordered_map<char, TrieNode*> children;
    bool isEndOfWord;
    TrieNode() : isEndOfWord(false) {}
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
        node->isEndOfWord = true;
    }
    bool search(string word) {
        TrieNode* node = root;
        for (char c : word) {
            if (node->children.find(c) == node->children.end()) {
                return false;
            }
            node = node->children[c];
        }
        return node->isEndOfWord;
    }
};

string replaceWords(vector<string>& dictionary, string sentence) {
    Trie trie;
    for (string word : dictionary) {
        trie.insert(word);
    }
    istringstream iss(sentence);
    string word, result;
    while (iss >> word) {
        if (trie.search(word)) {
            result += "# ";
        } else {
            result += word + " ";
        }
    }
    return result.substr(0, result.size() - 1);
}

int main() {
    vector<string> dictionary = {"cat", "bat", "rat"};
    string sentence = "the cat sat on the mat";
    cout << replaceWords(dictionary, sentence) << endl;
    return 0;
}
```

## Test Cases
```
Input: dictionary = ["cat","bat","rat"], sentence = "the cat sat on the mat"
Output: "the # sat on the mat"
```

## Key Takeaways
- Using a Trie data structure can efficiently solve string matching problems.
- The Trie data structure can be used to store a list of words and check for their presence in a sentence.
- The time complexity of the solution is linear with respect to the total number of characters in the input.