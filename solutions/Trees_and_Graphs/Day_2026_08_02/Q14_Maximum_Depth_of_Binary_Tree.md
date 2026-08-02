# Maximum Depth of Binary Tree

## Problem Statement
Given the root of a binary tree, find the maximum depth of the tree. The maximum depth of a binary tree is the number of nodes along the longest path from the root node down to the farthest leaf node. The path must start at the root and end at any leaf node. The number of nodes in the path is the depth of the tree. For example, the maximum depth of the binary tree in the figure is 3. The constraints are: the number of nodes in the tree is in the range [0, 104], and -100 <= Node.val <= 100.

## Approach
The algorithm uses a recursive depth-first search (DFS) approach to traverse the tree and calculate the maximum depth. It checks if the current node is NULL, in which case it returns 0, and otherwise returns the maximum depth of the left and right subtrees plus 1. This approach ensures that all nodes are visited and the maximum depth is calculated correctly.

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
        // Recursive case: return the maximum depth of the left and right subtrees plus 1
        else {
            return 1 + max(maxDepth(root->left), maxDepth(root->right));
        }
    }
};
```

## Test Cases
```
Input: root = [3,9,20,null,null,15,7]
Output: 3
Input: root = [1,null,2]
Output: 2
```

## Key Takeaways
- The maximum depth of a binary tree can be calculated using a recursive DFS approach.
- The time complexity is O(N), where N is the number of nodes in the tree, because each node is visited once.
- The space complexity is O(H), where H is the height of the tree, because of the recursive call stack.