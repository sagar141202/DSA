# Maximum Depth of Binary Tree

## Problem Statement
Given the root of a binary tree, find the maximum depth of the tree. The maximum depth of a binary tree is the number of nodes along the longest path from the root node down to the farthest leaf node. The path must consist of parent-child relationships, and it cannot contain duplicate nodes. The tree can be empty, in which case the maximum depth is 0. For example, the maximum depth of the tree with the following structure:
       3
      / \
     9   20
        /  \
       15   7
is 3.

## Approach
The algorithm uses a recursive depth-first search (DFS) approach to traverse the tree and calculate the maximum depth. It checks if the current node is null, and if so, returns 0. Otherwise, it recursively calculates the maximum depth of the left and right subtrees and returns the maximum of the two plus 1.

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
        // Recursively calculate the maximum depth of the left and right subtrees
        int leftDepth = maxDepth(root->left);
        int rightDepth = maxDepth(root->right);
        // Return the maximum of the two plus 1
        return max(leftDepth, rightDepth) + 1;
    }
};
```

## Test Cases
```
Input: [3,9,20,null,null,15,7]
Output: 3
Input: [1,null,2]
Output: 2
Input: []
Output: 0
```

## Key Takeaways
- The maximum depth of a binary tree can be calculated using a recursive DFS approach.
- The time complexity of the solution is O(N), where N is the number of nodes in the tree.
- The space complexity of the solution is O(H), where H is the height of the tree.