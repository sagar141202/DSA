# Binary Tree Zigzag Level Order Traversal

## Problem Statement
Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. The zigzag level order traversal starts from the leftmost node of the first level, then moves to the right, then moves to the leftmost node of the next level, and so on. For example, given the binary tree `[3,9,20,null,null,15,7]`, the zigzag level order traversal would be `[[3],[20,9],[15,7]]`. The constraints are: the number of nodes in the tree is in the range `[0, 2000]`, `-100 <= Node.val <= 100`.

## Approach
The algorithm uses a breadth-first search (BFS) approach with a queue to traverse the tree level by level. It also uses a flag to track the direction of traversal at each level. The flag is toggled after each level to achieve the zigzag effect.

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
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

class Solution {
public:
    vector<vector<int>> zigzagLevelOrder(TreeNode* root) {
        if (!root) return {};
        
        vector<vector<int>> result;
        queue<TreeNode*> q;
        q.push(root);
        bool leftToRight = true;
        
        while (!q.empty()) {
            int size = q.size();
            vector<int> level;
            
            for (int i = 0; i < size; i++) {
                TreeNode* node = q.front();
                q.pop();
                
                if (leftToRight) {
                    level.push_back(node->val);
                } else {
                    level.insert(level.begin(), node->val);
                }
                
                if (node->left) q.push(node->left);
                if (node->right) q.push(node->right);
            }
            
            result.push_back(level);
            leftToRight = !leftToRight;
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
- Use a queue to perform BFS traversal of the binary tree.
- Use a flag to track the direction of traversal at each level.
- Toggle the direction flag after each level to achieve the zigzag effect.
- Use `vector` to store the result and `queue` to store the nodes at each level.