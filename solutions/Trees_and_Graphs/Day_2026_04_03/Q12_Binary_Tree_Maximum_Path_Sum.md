# Binary Tree Maximum Path Sum

## Problem Statement
Given a binary tree, find the maximum path sum. The path sum is the sum of the node values in a path from any node to any other node in the tree. The path must go through at least one node, and the path can be any path in the tree (not necessarily a root-to-leaf path). For example, given the binary tree `[-10,9,20,null,null,15,7]`, the maximum path sum is `42` (from `20` to `15` to `7`).

## Approach
The approach is to use a recursive depth-first search (DFS) to calculate the maximum path sum. We will keep track of the maximum path sum seen so far, and for each node, we will calculate the maximum path sum that includes the current node.

## Complexity
- Time: O(N)
- Space: O(H), where N is the number of nodes and H is the height of the tree.

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class Solution {
public:
    int maxPathSum(TreeNode* root) {
        int max_sum = INT_MIN;
        dfs(root, max_sum);
        return max_sum;
    }
    
    int dfs(TreeNode* node, int& max_sum) {
        if (!node) return 0;
        int left = max(dfs(node->left, max_sum), 0);
        int right = max(dfs(node->right, max_sum), 0);
        max_sum = max(max_sum, node->val + left + right);
        return node->val + max(left, right);
    }
};
```

## Test Cases
```
Input: [-10,9,20,null,null,15,7]
Output: 42
Input: [1,2,3]
Output: 6
```

## Key Takeaways
- The key to this problem is to keep track of the maximum path sum seen so far, and to calculate the maximum path sum that includes the current node.
- We use a recursive DFS to traverse the tree, and for each node, we calculate the maximum path sum that includes the current node by considering the maximum path sum of the left and right subtrees.
- We use a reference to the `max_sum` variable to update it in the recursive function calls.