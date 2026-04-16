# Serialize and Deserialize Binary Tree

## Problem Statement
Serialization is the process of converting a data structure into a linear format, while deserialization is the process of reconstructing the original data structure from the serialized format. In this problem, we are given a binary tree and asked to implement a solution to serialize and deserialize it. The binary tree node structure is defined as `TreeNode *left` and `TreeNode *right`, and we can assume that the tree is a binary tree where each node has a unique value. The constraints are that the number of nodes in the tree will not exceed 100, and the values of the nodes will be in the range of 0 to 100. For example, given a binary tree with the following structure: 
       1
      / \
     2   3
    / \
   4   5
The serialized representation of the tree would be "1,2,4,X,X,5,X,X,3,X,X", where "X" represents a null node.

## Approach
We will use a recursive approach to traverse the binary tree in a pre-order manner and serialize it into a string. Then, we will use a similar recursive approach to deserialize the string back into a binary tree. The key idea is to use a comma to separate the node values and "X" to represent null nodes.

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
        if (val == "X") {
            return NULL;
        }
        TreeNode* node = new TreeNode(stoi(val));
        node->left = deserializeHelper(iss);
        node->right = deserializeHelper(iss);
        return node;
    }
};
```

## Test Cases
```
Input: root = [1,2,3,null,null,4,5]
Output: "1,2,X,X,3,4,X,X,5,X,X"
```

## Key Takeaways
- Use pre-order traversal to serialize the binary tree into a string.
- Use a recursive approach to deserialize the string back into a binary tree.
- Utilize "X" to represent null nodes in the serialized string.