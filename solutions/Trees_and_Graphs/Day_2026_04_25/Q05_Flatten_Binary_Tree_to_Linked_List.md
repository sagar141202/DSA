# Flatten Binary Tree to Linked List

## Problem Statement
Given the root of a binary tree, flatten the tree into a linked list in-place. The left child of a node should become the right child, and the original right child should become the left child of the left child's rightmost node. The transformation should be done in a way that the original tree's values are preserved, and the resulting linked list is right-leaning. For example, given the following tree:
       1
      / \
     2   5
    / \   \
   3   4   6
The output should be:
1 -> 2 -> 3 -> 4 -> 5 -> 6

## Approach
The algorithm involves a recursive or iterative approach to traverse the tree and reassign the child pointers. We can use a recursive solution that flattens the left and right subtrees and then combines them. Alternatively, an iterative solution using a stack can also be used.

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
        if (!root) return;
        flatten(root->left);
        flatten(root->right);
        // Reassign the child pointers
        TreeNode* temp = root->right;
        root->right = root->left;
        root->left = nullptr;
        // Find the rightmost node in the new right subtree
        TreeNode* rightmost = root->right;
        while (rightmost && rightmost->right) {
            rightmost = rightmost->right;
        }
        // Reassign the right child of the rightmost node
        if (rightmost) {
            rightmost->right = temp;
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
Output: 1 -> 2 -> 3 -> 4 -> 5 -> 6
```

## Key Takeaways
- Recursion or iteration can be used to solve this problem.
- The solution involves reassigning child pointers to transform the tree into a linked list.
- The time complexity is O(n), where n is the number of nodes in the tree, and the space complexity is O(n) due to the recursive call stack or the iterative use of a stack.