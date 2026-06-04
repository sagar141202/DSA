# Binary Tree Maximum Path Sum

## Problem Statement
Given a binary tree, find the maximum path sum. The path sum is the sum of node values in a path from any node to any other node in the tree. The path can be in any direction (left, right, or a combination of both) and can start and end at any node. The input tree is non-empty and consists of up to 10^4 nodes. Each node's value is between -10^4 and 10^4. The absolute value of the maximum path sum is less than or equal to 10^5.

## Approach
The algorithm uses a recursive depth-first search approach to calculate the maximum path sum. It calculates the maximum path sum for each subtree and updates the global maximum path sum if the current path sum is greater. The key insight is to consider each node as the start of a path and explore all possible paths from that node.

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
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class Solution {
public:
    int maxPathSum(TreeNode* root) {
        int max_sum = INT_MIN;
        maxGain(root, max_sum);
        return max_sum;
    }
    
    int maxGain(TreeNode* node, int& max_sum) {
        if (!node) return 0;
        
        // Recursively calculate the maximum gain for the left and right subtrees
        int left_gain = max(maxGain(node->left, max_sum), 0);
        int right_gain = max(maxGain(node->right, max_sum), 0);
        
        // Update the maximum path sum if the current path sum is greater
        max_sum = max(max_sum, node->val + left_gain + right_gain);
        
        // Return the maximum gain for the current node
        return node->val + max(left_gain, right_gain);
    }
};
```

## Test Cases
```
Input: root = [1,2,3]
Output: 6
Explanation: The maximum path sum is 1 + 2 + 3 = 6.

Input: root = [-10,9,20,null,null,15,7]
Output: 42
Explanation: The maximum path sum is 20 + 15 + 7 = 42.
```

## Key Takeaways
- Use a recursive approach to calculate the maximum path sum for each subtree.
- Consider each node as the start of a path and explore all possible paths from that node.
- Update the global maximum path sum if the current path sum is greater.