# Flatten Binary Tree to Linked List

## Problem Statement
Given the root of a binary tree, flatten the tree into a linked list in-place. The linked list should be made by using the right child pointers of the nodes, and the left child pointers should be set to null. For example, given the following tree:
        1
       / \
      2   5
     / \   \
    3   4   6
The flattened tree should will be:
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
You are not allowed to use any extra space.

## Approach
The idea is to recursively flatten the left and right subtrees, then connect the rightmost node of the left subtree to the root of the right subtree. We will use a recursive approach to solve this problem. We will first flatten the left subtree, then the right subtree, and finally connect them.

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
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class Solution {
public:
    void flatten(TreeNode* root) {
        // base case: if tree is empty, return
        if (root == NULL) return;
        
        // recursively flatten the left and right subtrees
        flatten(root->left);
        flatten(root->right);
        
        // if left child is not null, connect the rightmost node of the left subtree to the root of the right subtree
        if (root->left != NULL) {
            // find the rightmost node of the left subtree
            TreeNode* rightmost = root->left;
            while (rightmost->right != NULL) {
                rightmost = rightmost->right;
            }
            
            // connect the rightmost node of the left subtree to the root of the right subtree
            rightmost->right = root->right;
            root->right = root->left;
            root->left = NULL;
        }
    }
};
```

## Test Cases
```
Input: 
        1
       / \
      2   5
     / \   \
    3   4   6
Output: 
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
```

## Key Takeaways
- Use a recursive approach to solve this problem.
- First flatten the left subtree, then the right subtree, and finally connect them.
- Use the right child pointers of the nodes to connect the nodes, and set the left child pointers to null.