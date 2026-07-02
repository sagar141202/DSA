# Flatten Binary Tree to Linked List

## Problem Statement
Given the root of a binary tree, flatten the tree into a linked list in-place. The left child of a node should become the right child, and the original right child should become the left child of the left child's rightmost node. The tree is guaranteed to be non-empty, and all nodes will have a unique value. For example, given the following tree:
        1
       / \
      2   5
     / \   \
    3   4   6
The flattened tree should look like:
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
To solve this problem, we will use a recursive approach to traverse the tree and rearrange the nodes. We will first flatten the left and right subtrees, then move the right subtree to the rightmost node of the left subtree.

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
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

class Solution {
public:
    void flatten(TreeNode* root) {
        // Base case: if the tree is empty, return
        if (!root) return;
        
        // Recursively flatten the left and right subtrees
        flatten(root->left);
        flatten(root->right);
        
        // If the left subtree is not empty, move the right subtree to the rightmost node of the left subtree
        if (root->left) {
            // Find the rightmost node of the left subtree
            TreeNode* rightmost = root->left;
            while (rightmost->right) rightmost = rightmost->right;
            
            // Move the right subtree to the rightmost node of the left subtree
            rightmost->right = root->right;
            root->right = root->left;
            root->left = nullptr;
        }
    }
};
```

## Test Cases
```
Input: [1,2,5,3,4,null,6]
Output: [1,null,2,null,3,null,4,null,5,null,6]
```

## Key Takeaways
- The key to solving this problem is to use a recursive approach to traverse the tree and rearrange the nodes.
- We need to first flatten the left and right subtrees before moving the right subtree to the rightmost node of the left subtree.
- The time complexity is O(N), where N is the number of nodes in the tree, because we visit each node exactly once.