# Binary Tree Maximum Path Sum

## Problem Statement
Given a binary tree, find the maximum path sum. The path must start and end at any node in the tree, and the path can only go through nodes in the tree. The path can be from a node to any of its descendants, or from a node to any of its ancestors. The path can also be a single node. The maximum path sum is the maximum sum of all node values in a path.

## Approach
The algorithm uses a recursive depth-first search approach to find the maximum path sum. It calculates the maximum path sum for each node by considering the maximum path sum of its left and right subtrees. The maximum path sum is updated at each node if the current path sum is greater than the maximum path sum found so far.

## Complexity
- Time: O(N)
- Space: O(H), where N is the number of nodes in the tree and H is the height of the tree

## C++ Solution
```cpp
#include <iostream>
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
    int maxPathSum(TreeNode* root) {
        int max_sum = INT_MIN;
        dfs(root, max_sum);
        return max_sum;
    }
    
    int dfs(TreeNode* node, int& max_sum) {
        if (!node) return 0;
        
        // Calculate the maximum path sum for the left and right subtrees
        int left_sum = max(dfs(node->left, max_sum), 0);
        int right_sum = max(dfs(node->right, max_sum), 0);
        
        // Update the maximum path sum if the current path sum is greater
        max_sum = max(max_sum, node->val + left_sum + right_sum);
        
        // Return the maximum path sum for the current node
        return node->val + max(left_sum, right_sum);
    }
};
```

## Test Cases
```
Input: [1,2,3]
Output: 6
Input: [-10,9,20,null,null,15,7]
Output: 42
```

## Key Takeaways
- The maximum path sum can be negative if all node values are negative.
- The algorithm uses a recursive approach to calculate the maximum path sum for each node.
- The time complexity is O(N) where N is the number of nodes in the tree, and the space complexity is O(H) where H is the height of the tree.