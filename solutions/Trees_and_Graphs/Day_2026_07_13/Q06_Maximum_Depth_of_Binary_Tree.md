# Maximum Depth of Binary Tree

## Problem Statement
Given a binary tree, find its maximum depth. The maximum depth of a binary tree is the number of nodes along the longest path from the root node down to the farthest leaf node. The path must start at the root and end at any leaf node. The number of nodes at each level of the tree is not limited, and the tree can be empty. For example, the maximum depth of the binary tree `[3, 9, 20, null, null, 15, 7]` is 3.

## Approach
To find the maximum depth, we can use a recursive approach by calculating the maximum depth of the left and right subtrees and adding 1 for the current node. We can also use an iterative approach using a queue to perform a level-order traversal. The algorithm will traverse the tree level by level, keeping track of the current level number.

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
    int maxDepth(TreeNode* root) {
        // Base case: if the tree is empty, return 0
        if (root == nullptr) {
            return 0;
        }
        
        // Recursive case: calculate the maximum depth of the left and right subtrees
        int leftDepth = maxDepth(root->left);
        int rightDepth = maxDepth(root->right);
        
        // Return the maximum depth of the two subtrees plus 1 for the current node
        return max(leftDepth, rightDepth) + 1;
    }
};
```

## Test Cases
```
Input: [3, 9, 20, null, null, 15, 7]
Output: 3
Input: [1, null, 2]
Output: 2
Input: []
Output: 0
```

## Key Takeaways
- The maximum depth of a binary tree can be found using a recursive or iterative approach.
- The recursive approach involves calculating the maximum depth of the left and right subtrees and adding 1 for the current node.
- The iterative approach involves using a queue to perform a level-order traversal and keeping track of the current level number.