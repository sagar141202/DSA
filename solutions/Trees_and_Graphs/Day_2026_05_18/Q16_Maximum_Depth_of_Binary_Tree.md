# Maximum Depth of Binary Tree

## Problem Statement
Given the root of a binary tree, find the maximum depth of the tree. The maximum depth of a binary tree is the number of nodes along the longest path from the root node down to the farthest leaf node. The path must start at the root and end at any leaf node. The number of nodes in the path is the depth of the tree. For example, the maximum depth of the tree with the following structure:
       3
      / \
     9  20
       /  \
      15   7
is 3, because the longest path from the root to a leaf node is 3 -> 20 -> 15 or 3 -> 20 -> 7.

## Approach
The approach to solve this problem is to use a recursive depth-first search (DFS) algorithm to traverse the tree and calculate the maximum depth. We will recursively calculate the maximum depth of the left and right subtrees and return the maximum of the two plus one for the current node.

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
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

class Solution {
public:
    int maxDepth(TreeNode* root) {
        // base case: if the tree is empty, return 0
        if (root == nullptr) {
            return 0;
        }
        
        // recursively calculate the maximum depth of the left and right subtrees
        int leftDepth = maxDepth(root->left);
        int rightDepth = maxDepth(root->right);
        
        // return the maximum of the two depths plus one for the current node
        return max(leftDepth, rightDepth) + 1;
    }
};
```

## Test Cases
```
Input: 
       3
      / \
     9  20
       /  \
      15   7
Output: 3

Input: 
    1
   / \
  2   3
 / \
4   5
Output: 3
```

## Key Takeaways
- The maximum depth of a binary tree can be calculated using a recursive DFS algorithm.
- The time complexity of the solution is O(n), where n is the number of nodes in the tree, because we visit each node once.
- The space complexity of the solution is O(h), where h is the height of the tree, because of the recursive call stack.