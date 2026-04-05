# Flatten Binary Tree to Linked List

## Problem Statement
Given the root of a binary tree, flatten the tree into a linked list in-place. The linked list should be made by using the right child pointer for the next node in the list. For example, given the following tree:
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
We will use a recursive approach to solve this problem, where we will traverse the tree and for each node, we will recursively flatten its left and right subtrees. Then we will connect the right child of the current node to the head of the flattened right subtree.

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
        flatten(root->left);
        flatten(root->right);
        
        // connect the right child of the current node to the head of the flattened right subtree
        TreeNode* temp = root->right;
        root->right = root->left;
        root->left = nullptr;
        
        // find the last node in the flattened left subtree
        while (root->right != nullptr) {
            root = root->right;
        }
        
        // connect the last node in the flattened left subtree to the head of the flattened right subtree
        root->right = temp;
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
- The problem requires in-place modification of the binary tree.
- We use a recursive approach to solve this problem.
- The time complexity of the solution is O(N), where N is the number of nodes in the tree.