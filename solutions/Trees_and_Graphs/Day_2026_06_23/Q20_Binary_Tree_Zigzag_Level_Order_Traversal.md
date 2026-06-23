# Binary Tree Zigzag Level Order Traversal

## Problem Statement
Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. The solution should be implemented in a way that it traverses the tree level by level, but with a twist: at each level, it alternates the direction of traversal. For example, if the tree has the following structure:
```
    3
   / \
  9  20
    /  \
   15   7
```
The zigzag level order traversal would be `[3, 20, 9, 15, 7]`. The constraints are that the number of nodes in the tree will not exceed 100, and the values of the nodes will be between 0 and 100.

## Approach
The algorithm uses a level order traversal (BFS) approach, utilizing a queue to store nodes at each level. It keeps track of the current level and reverses the order of nodes at each odd level. This ensures the zigzag pattern in the traversal.

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
        bool isReverse = false;
        
        while (!q.empty()) {
            int size = q.size();
            vector<int> level;
            
            for (int i = 0; i < size; i++) {
                TreeNode* node = q.front();
                q.pop();
                
                if (isReverse) {
                    level.insert(level.begin(), node->val);
                } else {
                    level.push_back(node->val);
                }
                
                if (node->left) q.push(node->left);
                if (node->right) q.push(node->right);
            }
            
            result.push_back(level);
            isReverse = !isReverse;
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
```

## Key Takeaways
- Utilize a queue for level order traversal to process nodes level by level.
- Keep track of the current level to decide whether to reverse the order of nodes at that level.
- Use a boolean flag (`isReverse`) to alternate the direction of traversal at each level.