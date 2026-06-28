# Binary Tree Zigzag Level Order Traversal

## Problem Statement
Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. The solution should return a list of lists where each sublist contains the node values at a given level, and the levels alternate between left-to-right and right-to-left order. For example, given a binary tree with the following structure:
```
    3
   / \
  9  20
    /  \
   15   7
```
The zigzag level order traversal would be `[[3], [20, 9], [15, 7]]`. The input tree is guaranteed to have at most 2000 nodes, and the values of the nodes are guaranteed to be within the range of a 32-bit signed integer.

## Approach
The algorithm uses a level-order traversal (BFS) approach, utilizing a queue to keep track of nodes at each level. It also uses a flag to determine the order of traversal at each level.

## Complexity
- Time: O(N)
- Space: O(N)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    vector<vector<int>> zigzagLevelOrder(TreeNode* root) {
        vector<vector<int>> result;
        if (!root) return result;
        
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
Input: 
    3
   / \
  9  20
    /  \
   15   7
Output: [[3], [20, 9], [15, 7]]

Input: 
    1
   / \
  2   3
 / \
4   5
Output: [[1], [3, 2], [4, 5]]
```

## Key Takeaways
- Utilize a queue for level-order traversal to ensure nodes are processed level by level.
- Use a flag (`leftToRight`) to alternate the order of node values at each level.
- Insert node values at the beginning of the level vector when traversing from right to left to maintain the correct order.