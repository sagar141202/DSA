# Maximum Depth of Binary Tree

## Problem Statement
Given a binary tree, find its maximum depth. The maximum depth of a binary tree is the number of nodes along the longest path from the root node down to the farthest leaf node. The problem assumes that the binary tree is represented as a tree where each node has a value and two children (left and right). The input tree is not guaranteed to be balanced, and the nodes can have any integer value. For example, the maximum depth of the binary tree with the following structure: 
       1
      / \
     2   3
    / \
   4   5
is 3.

## Approach
The approach to solve this problem is to use recursion to traverse the tree and keep track of the maximum depth encountered. The algorithm checks if the current node is a leaf node, and if so, returns 1. Otherwise, it recursively calculates the maximum depth of the left and right subtrees and returns the maximum of the two plus 1.

## Complexity
- Time: O(n)
- Space: O(h)

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
    int maxDepth(TreeNode* root) {
        // base case: if the tree is empty, return 0
        if (root == NULL) {
            return 0;
        } else {
            // recursively calculate the maximum depth of the left and right subtrees
            int leftDepth = maxDepth(root->left);
            int rightDepth = maxDepth(root->right);
            // return the maximum of the two plus 1
            return max(leftDepth, rightDepth) + 1;
        }
    }
};
```

## Test Cases
```
Input: 
       1
      / \
     2   3
    / \
   4   5
Output: 3

Input: 
    1
   / \
  2   3
 / \
4   5
/
6
Output: 4
```

## Key Takeaways
- The maximum depth of a binary tree can be calculated using recursion.
- The time complexity of the solution is O(n), where n is the number of nodes in the tree, because each node is visited once.
- The space complexity of the solution is O(h), where h is the height of the tree, because of the recursive call stack.