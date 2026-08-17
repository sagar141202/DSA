# Serialize and Deserialize Binary Tree

## Problem Statement
Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment. Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure. For example, you can use a pre-order traversal to serialize the binary tree to a string, and then use the string to reconstruct the binary tree. The pre-order traversal of a binary tree is a traversal method where the current node is visited before its child nodes. The pre-order traversal of the above binary tree is "1,2,3,None,None,4,5,None,None,None,None". The "None" represents a null node.

## Approach
The approach is to use a pre-order traversal to serialize the binary tree into a string, where "None" represents a null node. Then, use the string to reconstruct the binary tree by recursively creating nodes and assigning their values.

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
        ostringstream os;
        serializeHelper(root, os);
        return os.str();
    }

    // Decodes your encoded data to tree.
    TreeNode* deserialize(string data) {
        istringstream is(data);
        return deserializeHelper(is);
    }
    
    void serializeHelper(TreeNode* node, ostringstream& os) {
        if (!node) {
            os << "None,";
        } else {
            os << node->val << ",";
            serializeHelper(node->left, os);
            serializeHelper(node->right, os);
        }
    }
    
    TreeNode* deserializeHelper(istringstream& is) {
        string val;
        getline(is, val, ',');
        if (val == "None") {
            return NULL;
        }
        TreeNode* node = new TreeNode(stoi(val));
        node->left = deserializeHelper(is);
        node->right = deserializeHelper(is);
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
Output: "1,2,None,None,3,4,None,None,5,None,None"
```

## Key Takeaways
- Serialization is the process of converting an object into a stream of bytes.
- Pre-order traversal can be used for serialization and deserialization of binary trees.
- Recursive approaches can be used to simplify the implementation of serialization and deserialization algorithms.