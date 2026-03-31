# Serialize and Deserialize Binary Tree

## Problem Statement
Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment. Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure. The encoded string should be as compact as possible. For example, you can serialize the following binary tree: 
```
    1
   / \
  2   3
     / \
    4   5
```
to `"1,2,X,X,3,4,X,X,5,X,X"`, where `X` represents `null` node. 

## Approach
We will use a recursive Depth-First Search (DFS) approach to traverse the tree and serialize it into a string. For deserialization, we will use a recursive approach to reconstruct the tree from the serialized string.

## Complexity
- Time: O(N)
- Space: O(N)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

// Definition for a binary tree node.
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class Codec {
public:
    // Encodes a tree to a single string.
    string serialize(TreeNode* root) {
        ostringstream out;
        serializeHelper(root, out);
        return out.str();
    }

    // Decodes your encoded data to tree.
    TreeNode* deserialize(string data) {
        istringstream in(data);
        return deserializeHelper(in);
    }

    void serializeHelper(TreeNode* node, ostringstream& out) {
        if (node) {
            out << node->val << ",";
            serializeHelper(node->left, out);
            serializeHelper(node->right, out);
        } else {
            out << "X,";
        }
    }

    TreeNode* deserializeHelper(istringstream& in) {
        string val;
        getline(in, val, ',');
        if (val == "X") {
            return nullptr;
        }
        TreeNode* node = new TreeNode(stoi(val));
        node->left = deserializeHelper(in);
        node->right = deserializeHelper(in);
        return node;
    }
};
```

## Test Cases
```
Input: 
     1
    / \
   2   3
      / \
     4   5
Output: 1,2,X,X,3,4,X,X,5,X,X
```

## Key Takeaways
- Use recursive DFS to serialize and deserialize the binary tree.
- Use a delimiter (e.g., ",") to separate node values in the serialized string.
- Handle null nodes by using a sentinel value (e.g., "X") in the serialized string.