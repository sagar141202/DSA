# Flatten Binary Tree to Linked List

## Problem Statement
Given the root of a binary tree, flatten the tree into a linked list in-place. The linked list should be made by using the right child pointer of each node to point to the next node in the sequence. The left child pointer of each node should be set to NULL. For example, given the following tree:
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
Note that the tree is flattened in pre-order (root, left, right).

## Approach
The approach is to use a recursive pre-order traversal to flatten the binary tree into a linked list. We will keep track of the previous node and update its right child to the current node. The left child of the current node will be set to NULL.

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
        if (root == NULL) return;
        flattenHelper(root);
    }
    
    TreeNode* flattenHelper(TreeNode* node) {
        if (node == NULL) return NULL;
        TreeNode* left = flattenHelper(node->left);
        TreeNode* right = flattenHelper(node->right);
        if (left != NULL) {
            TreeNode* temp = left;
            while (temp->right != NULL) temp = temp->right;
            temp->right = node->right;
            node->right = left;
            node->left = NULL;
        }
        return right == NULL ? (left == NULL ? node : temp) : temp;
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
- Use recursive pre-order traversal to flatten the binary tree.
- Keep track of the previous node to update its right child pointer.
- Set the left child pointer of each node to NULL.