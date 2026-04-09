# Maximum Depth of Binary Tree

## Problem Statement
Given the root of a binary tree, find the maximum depth of the tree. The maximum depth of a binary tree is the number of nodes along the longest path from the root node down to the farthest leaf node. The path must start at the root and end at any leaf node. The number of nodes in the path is the depth of the tree. The tree has at most 10^4 nodes, and the height of the tree is at most 10^4.

## Approach
We can solve this problem by using a recursive depth-first search (DFS) approach. The idea is to recursively calculate the maximum depth of the left and right subtrees and return the maximum of the two plus one for the current node. This approach ensures that we traverse all nodes in the tree and calculate the maximum depth correctly.

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
        // Base case: if the tree is empty, return 0
        if (root == nullptr) {
            return 0;
        }
        
        // Recursively calculate the maximum depth of the left and right subtrees
        int leftDepth = maxDepth(root->left);
        int rightDepth = maxDepth(root->right);
        
        // Return the maximum of the two plus one for the current node
        return max(leftDepth, rightDepth) + 1;
    }
};
```

## Test Cases
```
Input: root = [3,9,20,null,null,15,7]
Output: 3
```

## Key Takeaways
- The maximum depth of a binary tree can be calculated using a recursive DFS approach.
- The time complexity of this approach is O(n), where n is the number of nodes in the tree.
- The space complexity of this approach is O(h), where h is the height of the tree.