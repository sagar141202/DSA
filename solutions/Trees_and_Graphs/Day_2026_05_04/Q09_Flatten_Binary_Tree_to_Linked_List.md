# Flatten Binary Tree to Linked List

## Problem Statement
Given the root of a binary tree, flatten the tree into a linked list in-place. The linked list should be made by using the right child pointers of each node to point to the next node in the list. The left child of each node should be set to nullptr. For example, given the following tree:
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
The algorithm involves recursively flattening the left and right subtrees, then rearranging the nodes to form a linked list. This is done by making the right child of each node point to the next node in the list. The key insight is to reverse the preorder traversal of the tree to achieve this.

## Complexity
- Time: O(n)
- Space: O(n)

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
        if (root == nullptr) return;
        flatten(root->left);
        flatten(root->right);
        if (root->left != nullptr) {
            // find the rightmost node in the left subtree
            TreeNode* rightmost = root->left;
            while (rightmost->right != nullptr) {
                rightmost = rightmost->right;
            }
            // reassign the right child of the rightmost node to the original right child of the root
            rightmost->right = root->right;
            // reassign the right child of the root to the original left child
            root->right = root->left;
            // set the left child of the root to nullptr
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
- To flatten a binary tree into a linked list, we need to rearrange the nodes to make the right child of each node point to the next node in the list.
- We can achieve this by recursively flattening the left and right subtrees, then reassigning the child pointers of the root node.
- The time complexity is O(n), where n is the number of nodes in the tree, since we visit each node once. The space complexity is O(n) due to the recursive call stack.