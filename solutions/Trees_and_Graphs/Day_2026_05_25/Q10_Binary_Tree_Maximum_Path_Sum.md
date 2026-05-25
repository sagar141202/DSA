# Binary Tree Maximum Path Sum

## Problem Statement
Given a binary tree, find the maximum path sum. The path sum is the sum of node values in a path from any node to any other node in the tree. The path can be from a node to its descendant, or from a node to its ancestor, but it cannot be a path that starts and ends at the same node. For example, in the tree with nodes [1,2,3], the maximum path sum is 6, which is the sum of the node values in the path [1,3]. The input tree will have at most 1000 nodes, and each node will have a value between -1000 and 1000.

## Approach
The algorithm uses a recursive depth-first search to calculate the maximum path sum. It keeps track of the maximum path sum found so far and updates it whenever a larger path sum is found. The key insight is to consider each node as the root of a subtree and calculate the maximum path sum for that subtree.

## Complexity
- Time: O(n)
- Space: O(h)

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
        int left = max(0, dfs(node->left, max_sum));
        int right = max(0, dfs(node->right, max_sum));
        max_sum = max(max_sum, node->val + left + right);
        return node->val + max(left, right);
    }
};
```

## Test Cases
```
Input: [-10,9,20,null,null,15,7]
Output: 42
```

## Key Takeaways
- Use recursive depth-first search to calculate the maximum path sum.
- Keep track of the maximum path sum found so far and update it whenever a larger path sum is found.
- Consider each node as the root of a subtree and calculate the maximum path sum for that subtree.