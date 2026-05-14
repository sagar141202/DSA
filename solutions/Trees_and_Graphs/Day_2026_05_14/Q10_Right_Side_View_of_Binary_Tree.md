# Right Side View of Binary Tree

## Problem Statement
Given the root of a binary tree, return the rightmost node value at each depth level, from top to bottom. The input tree is non-empty and has at most 2000 nodes. Each node has a unique value between 1 and 10^5. The tree is not guaranteed to be balanced, and the height of the tree is at most 2000.

## Approach
The algorithm uses a level-order traversal approach, where we traverse the tree level by level and store the last node value at each level. We utilize a queue to keep track of nodes at each level. The rightmost node value at each level is the last node we visit.

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
    vector<int> rightSideView(TreeNode* root) {
        // Initialize result vector and queue
        vector<int> result;
        if (!root) return result;
        queue<TreeNode*> q;
        q.push(root);
        
        // Perform level-order traversal
        while (!q.empty()) {
            int levelSize = q.size();
            // Store the last node value at each level
            for (int i = 0; i < levelSize; i++) {
                TreeNode* node = q.front();
                q.pop();
                if (i == levelSize - 1) {
                    result.push_back(node->val);
                }
                if (node->left) q.push(node->left);
                if (node->right) q.push(node->right);
            }
        }
        return result;
    }
};
```

## Test Cases
```
Input: [1,2,3,null,5,null,4]
Output: [1,3,4]
Input: [1,null,3]
Output: [1,3]
```

## Key Takeaways
- Use level-order traversal to visit nodes level by level.
- Store the last node value at each level to get the right side view.
- Utilize a queue to keep track of nodes at each level.