# Binary Tree Zigzag Level Order Traversal

## Problem Statement
Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. The zigzag level order traversal is defined as follows: for each given tree level, the first node from the left is the first node in that level, and the last node from the left is the last node in that level, then the next level is the reverse of the previous level, and so on. For example, given the binary tree `[3,9,20,null,null,15,7]`, the zigzag level order traversal is `[[3],[20,9],[15,7]]`. The constraints are: the number of nodes in the tree is in the range `[0, 2000]`, `-100 <= Node.val <= 100`.

## Approach
The algorithm uses a level order traversal (BFS) approach with a queue to store the nodes at each level. It iterates through each level, storing the node values in a vector. If the current level is even, the vector is added to the result as is; if the level is odd, the vector is reversed before being added to the result.

## Complexity
- Time: O(N)
- Space: O(N)

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
    vector<vector<int>> zigzagLevelOrder(TreeNode* root) {
        vector<vector<int>> result;
        if (!root) return result;
        
        queue<TreeNode*> q;
        q.push(root);
        int level = 0;
        
        while (!q.empty()) {
            int size = q.size();
            vector<int> level_values;
            
            for (int i = 0; i < size; i++) {
                TreeNode* node = q.front();
                q.pop();
                level_values.push_back(node->val);
                
                if (node->left) q.push(node->left);
                if (node->right) q.push(node->right);
            }
            
            if (level % 2 == 1) {
                reverse(level_values.begin(), level_values.end());
            }
            
            result.push_back(level_values);
            level++;
        }
        
        return result;
    }
};
```

## Test Cases
```
Input: [3,9,20,null,null,15,7]
Output: [[3],[20,9],[15,7]]
Input: [1]
Output: [[1]]
Input: []
Output: []
```

## Key Takeaways
- The use of a queue allows for efficient level order traversal.
- Reversing the level values when the level is odd achieves the zigzag pattern.
- This solution handles trees of varying sizes and node values within the given constraints.