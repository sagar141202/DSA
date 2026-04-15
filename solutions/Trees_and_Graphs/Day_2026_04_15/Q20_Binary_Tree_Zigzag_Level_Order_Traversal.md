# Binary Tree Zigzag Level Order Traversal

## Problem Statement
Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. The solution should handle trees of any size and structure. For example, given the following binary tree: 
```
    3
   / \
  9  20
    /  \
   15   7
```
The zigzag level order traversal should return `[[3],[20,9],[15,7]]`. The traversal should start from the root, then move to the next level from right to left, then from left to right, and so on.

## Approach
The algorithm uses a level order traversal (BFS) approach with a queue to store nodes at each level. It utilizes a flag to track the direction of traversal at each level. The flag is toggled after each level to alternate the direction.

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
Output: [[3],[20,9],[15,7]]
```

## Key Takeaways
- Use a queue for level order traversal to efficiently process nodes level by level.
- Utilize a flag to keep track of the traversal direction at each level, toggling it after each level to achieve the zigzag effect.
- For each level, store the node values in a vector, and then add this vector to the result based on the current traversal direction.