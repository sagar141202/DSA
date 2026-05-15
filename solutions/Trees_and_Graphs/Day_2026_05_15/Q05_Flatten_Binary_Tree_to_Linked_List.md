# Flatten Binary Tree to Linked List

## Problem Statement
Given the root of a binary tree, flatten the tree into a linked list in-place. The linked list should be made by using the right child pointer and should be done in a way that the left child of each node should be set to nullptr. The nodes should be connected from left to right. For example, given the following tree:
        1
       / \
      2   5
     / \   \
    3   4   6
The flattened tree should will look like:
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
The input tree is guaranteed to be non-empty.

## Approach
The approach to solve this problem is to use a recursive function that traverses the tree and appends the left subtree to the right subtree. This can be done by finding the rightmost node in the left subtree and appending the right subtree to it.

## Complexity
- Time: O(N)
- Space: O(N)

## C++ Solution
```cpp
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    void flatten(TreeNode* root) {
        if (!root) return;
        flatten(root->left);
        flatten(root->right);
        if (root->left) {
            // Find the rightmost node in the left subtree
            TreeNode* rightmost = root->left;
            while (rightmost->right) {
                rightmost = rightmost->right;
            }
            // Append the right subtree to the rightmost node
            rightmost->right = root->right;
            // Set the right child of the root to the left child
            root->right = root->left;
            // Set the left child of the root to nullptr
            root->left = nullptr;
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
- The key to solving this problem is to use a recursive function to traverse the tree and append the left subtree to the right subtree.
- The rightmost node in the left subtree is used to append the right subtree.
- The left child of the root is set to nullptr after appending the right subtree.