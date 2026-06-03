# Flatten Binary Tree to Linked List

## Problem Statement
Given the root of a binary tree, flatten the tree into a "linked list": 
- The "linked list" should use the same TreeNode class where each node's `right` child points to the next node in the sequence and the `left` child is always `nullptr`.
- Example: Given the following tree:
        1
       / \
      2   5
     / \   \
    3   4   6
The flattened tree should look like this:
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
The approach is to perform a depth-first search (DFS) on the binary tree, and for each node, append its right child to the right of its left child. This will effectively "flatten" the tree into a linked list. We will use a recursive function to traverse the tree and modify the nodes accordingly.

## Complexity
- Time: O(N)
- Space: O(N)

## C++ Solution
```cpp
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
        if (root == nullptr) return;
        flattenHelper(root);
    }

    TreeNode* flattenHelper(TreeNode* node) {
        if (node == nullptr) return nullptr;
        
        // Recursively flatten the left and right subtrees
        TreeNode* leftTail = flattenHelper(node->left);
        TreeNode* rightTail = flattenHelper(node->right);
        
        // If the left subtree is not empty, append the right subtree to the left subtree
        if (leftTail != nullptr) {
            leftTail->right = node->right;
            node->right = node->left;
            node->left = nullptr;
        }
        
        // Return the tail of the flattened subtree
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
- To flatten a binary tree into a linked list, we need to perform a depth-first search (DFS) on the tree and modify the nodes accordingly.
- We use a recursive function to traverse the tree and flatten the left and right subtrees.
- The time complexity of this solution is O(N), where N is the number of nodes in the tree, and the space complexity is also O(N) due to the recursive call stack.