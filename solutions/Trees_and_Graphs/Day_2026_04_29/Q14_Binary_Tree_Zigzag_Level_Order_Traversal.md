# Binary Tree Zigzag Level Order Traversal

## Problem Statement
Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. The solution should be able to handle trees with up to 10^4 nodes and node values ranging from 0 to 10^4. For example, given a binary tree with the following structure:
```
    3
   / \
  9  20
    /  \
   15   7
```
The zigzag level order traversal would be `[[3], [20, 9], [15, 7]]`. The first level is from left to right, the second level is from right to left, and so on.

## Approach
We will utilize a level order traversal (BFS) approach, using a queue to keep track of nodes at each level and a flag to determine the order of traversal at each level. The flag will be toggled after each level to achieve the zigzag effect.

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
Output: [[1]]

Input: 
    1
   / \
  2   3
Output: [[1], [3, 2]]
```

## Key Takeaways
- Using a queue for level order traversal is essential for solving this problem efficiently.
- The use of a flag (`leftToRight`) helps in toggling the order of traversal at each level, thus achieving the zigzag effect.
- Inserting elements at the beginning of a vector can be done using the `insert` method with the `begin` iterator as the position.