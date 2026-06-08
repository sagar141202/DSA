# Serialize and Deserialize Binary Tree

## Problem Statement
The problem requires designing a class to serialize and deserialize a binary tree. Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment. Deserialization is the reverse process, where the sequence of bits is converted back into a data structure or object. The binary tree node structure is given as follows: each node has a unique value, and it may have a left child node and a right child node. The task is to write methods `serialize` and `deserialize` to convert the binary tree into a string and vice versa. For example, given a binary tree with the following structure: 
       1
      / \
     2   3
    / \
   4   5
The serialized string can be "1,2,4,X,X,5,X,X,3,X,X," where "X" represents a null node.

## Approach
The approach involves using a pre-order traversal to serialize the binary tree, and then using the serialized string to reconstruct the binary tree during deserialization. We use a comma to separate node values and "X" to represent null nodes.

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
        ostringstream oss;
        serializeHelper(root, oss);
        return oss.str();
    }

    // Decodes your encoded data to tree.
    TreeNode* deserialize(string data) {
        istringstream iss(data);
        return deserializeHelper(iss);
    }
    
    void serializeHelper(TreeNode* node, ostringstream& oss) {
        if (node) {
            oss << node->val << ",";
            serializeHelper(node->left, oss);
            serializeHelper(node->right, oss);
        } else {
            oss << "X,";
        }
    }
    
    TreeNode* deserializeHelper(istringstream& iss) {
        string val;
        getline(iss, val, ',');
        if (val == "X") return nullptr;
        TreeNode* node = new TreeNode(stoi(val));
        node->left = deserializeHelper(iss);
        node->right = deserializeHelper(iss);
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
Output: "1,2,4,X,X,5,X,X,3,X,X,"
```

## Key Takeaways
- Use pre-order traversal for serialization and deserialization.
- Use "X" to represent null nodes in the serialized string.
- The `serialize` and `deserialize` methods should be able to handle null input and empty strings.