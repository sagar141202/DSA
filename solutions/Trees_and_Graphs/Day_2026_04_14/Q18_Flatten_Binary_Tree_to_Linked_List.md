# Flatten Binary Tree to Linked List

## Problem Statement
Given the root of a binary tree, flatten the tree into a linked list in-place. The linked list should be made by using the right child pointers of the nodes, and the left child pointers should be set to nullptr. For example, given the following tree:
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
The function should not return anything (i.e., it should return void), but it should modify the input tree in-place.

## Approach
The algorithm involves a recursive approach, where we traverse the tree and append the right subtree to the left subtree. We then update the right child of the current node to its former left child and set the left child to nullptr. This process continues recursively until the entire tree is flattened.

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
        // Base case: if the tree is empty
        if (!root) return;
        
        // Recursively flatten the left and right subtrees
        flatten(root->left);
        flatten(root->right);
        
        // If the left subtree is not empty
        if (root->left) {
            // Find the rightmost node in the left subtree
            TreeNode* rightmost = root->left;
            while (rightmost->right) rightmost = rightmost->right;
            
            // Append the right subtree to the rightmost node in the left subtree
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
- Recursively traversing the tree allows us to handle the tree in a bottom-up manner.
- Updating the child pointers of each node is essential to correctly flatten the tree.
- The time complexity is linear because we visit each node exactly once.