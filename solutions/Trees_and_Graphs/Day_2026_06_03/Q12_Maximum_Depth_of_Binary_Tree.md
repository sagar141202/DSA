# Maximum Depth of Binary Tree

## Problem Statement
Given a binary tree, find the maximum depth of the tree. The maximum depth of a binary tree is the number of nodes along the longest path from the root node down to the farthest leaf node. The path must start at the root and end at a leaf node. The depth of a tree is the maximum number of edges on a path between the root and a leaf. For example, the maximum depth of the tree with the following structure:
       1
      / \
     2   3
    / \
   4   5
is 3.

## Approach
We will use a recursive depth-first search (DFS) approach to find the maximum depth of the binary tree. The idea is to recursively calculate the depth of the left and right subtrees and return the maximum of the two plus one for the current node. This approach ensures that we visit each node exactly once and calculate the maximum depth correctly.

## Complexity
- Time: O(N)
- Space: O(H)

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
        // Base case: if the tree is empty, return 0
        if (root == NULL) {
            return 0;
        }
        // Recursively calculate the depth of the left and right subtrees
        int leftDepth = maxDepth(root->left);
        int rightDepth = maxDepth(root->right);
        // Return the maximum of the two depths plus one for the current node
        return max(leftDepth, rightDepth) + 1;
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
  / \
 6   7
Output: 4
```

## Key Takeaways
- The maximum depth of a binary tree can be calculated using a recursive DFS approach.
- The time complexity of this approach is O(N), where N is the number of nodes in the tree.
- The space complexity of this approach is O(H), where H is the height of the tree.