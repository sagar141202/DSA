# Flatten Binary Tree to Linked List

## Problem Statement
Given the root of a binary tree, flatten the tree into a linked list in-place. The linked list should be made by using the right child pointer of each node to point to the next node in the sequence. The left child pointer should be set to NULL. For example, given the following tree:
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
We will use a recursive approach to solve this problem. The idea is to recursively flatten the left and right subtrees, and then connect the flattened subtrees to the current node. We will keep track of the last node in the flattened subtree to connect it to the current node.

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
        // Base case: if the tree is empty, return
        if (!root) return;
        
        // Recursively flatten the left and right subtrees
        flatten(root->left);
        flatten(root->right);
        
        // If the left subtree is not empty, connect it to the right subtree
        if (root->left) {
            // Find the last node in the left subtree
            TreeNode* last = root->left;
            while (last->right) last = last->right;
            
            // Connect the last node in the left subtree to the right subtree
            last->right = root->right;
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
- We use a recursive approach to flatten the binary tree into a linked list.
- We keep track of the last node in the flattened subtree to connect it to the current node.
- The time complexity is O(n), where n is the number of nodes in the tree, and the space complexity is O(n) due to the recursive call stack.