# Flatten Binary Tree to Linked List

## Problem Statement
Given the root of a binary tree, flatten the tree into a linked list in-place. The linked list should be in the same order as a pre-order traversal of the tree. The definition for a Node is public class TreeNode { int val; TreeNode left; TreeNode right; TreeNode() {} TreeNode(int val) { this.val = val; } TreeNode(int val, TreeNode left, TreeNode right) { this.val = val; this.left = left; this.right = right; } }. For example, given the following tree: 
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
We will use a recursive approach to solve this problem by first flattening the left and right subtrees, then appending the right subtree to the left subtree. This approach ensures the resulting linked list is in pre-order traversal order.

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
        if (!root) return;
        flatten(root->left);
        flatten(root->right);
        
        // If the left subtree is not null, append the right subtree to the left subtree
        if (root->left) {
            // Find the rightmost node in the left subtree
            TreeNode* rightmost = root->left;
            while (rightmost->right) {
                rightmost = rightmost->right;
            }
            
            // Append the right subtree to the left subtree
            rightmost->right = root->right;
            root->right = root->left;
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
- The key to solving this problem is to first flatten the left and right subtrees, then append the right subtree to the left subtree.
- This approach ensures the resulting linked list is in pre-order traversal order.
- The time complexity of this solution is O(n), where n is the number of nodes in the tree, because each node is visited once.