# Flatten Binary Tree to Linked List

## Problem Statement
Given the root of a binary tree, flatten the tree into a linked list in-place. The flattening should be done in such a way that the left child of each node should become the right child of the same node, and the original right child of the node should become the right child of the new right child. The tree is flattened in a way that the left subtree of each node is appended to the right subtree of the same node. For example, given the following tree:
        1
       / \
      2   5
     / \   \
    3   4   6
The flattened tree should be:
1
 \
  2
   \
    3
     \
      4
       \
        5
         \
          6

## Approach
The algorithm involves recursively flattening the left and right subtrees and then appending the flattened left subtree to the right subtree. We use a recursive approach to solve this problem, where we first flatten the left and right subtrees and then rearrange the nodes.

## Complexity
- Time: O(n)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

// Definition for a binary tree node.
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

class Solution {
public:
    void flatten(TreeNode* root) {
        flattenHelper(root);
    }
    
    TreeNode* flattenHelper(TreeNode* node) {
        if (node == nullptr) {
            return nullptr;
        }
        
        TreeNode* leftTail = flattenHelper(node->left);
        TreeNode* rightTail = flattenHelper(node->right);
        
        if (leftTail != nullptr) {
            leftTail->right = node->right;
            node->right = node->left;
            node->left = nullptr;
        }
        
        return rightTail == nullptr ? leftTail : rightTail;
    }
};
```

## Test Cases
```
Input: [1,2,5,3,4,null,6]
Output: [1,null,2,null,3,null,4,null,5,null,6]
```

## Key Takeaways
- Recursively flatten the left and right subtrees before rearranging the nodes.
- Use a helper function to keep track of the tail of the flattened subtree.
- Update the left and right child pointers of each node accordingly.