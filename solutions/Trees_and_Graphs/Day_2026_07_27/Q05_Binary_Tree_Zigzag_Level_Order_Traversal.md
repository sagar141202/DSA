# Binary Tree Zigzag Level Order Traversal

## Problem Statement
Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. The solution should be able to handle trees with up to 10^4 nodes and node values ranging from 0 to 10^4. For example, given the binary tree [3,9,20,null,null,15,7], the zigzag level order traversal is [[3],[20,9],[15,7]]. The input tree is guaranteed to be non-empty.

## Approach
The algorithm uses a level order traversal approach with a queue to traverse the tree level by level. It utilizes a flag to track the direction of traversal at each level, alternating between left-to-right and right-to-left. This allows the algorithm to efficiently generate the zigzag level order traversal.

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
Input: [3,9,20,null,null,15,7]
Output: [[3],[20,9],[15,7]]
Input: [1]
Output: [[1]]
Input: [1,2,3,4,null,null,5]
Output: [[1],[3,2],[4,5]]
```

## Key Takeaways
- Use a queue to efficiently perform level order traversal.
- Utilize a flag to alternate the direction of traversal at each level.
- Apply the zigzag pattern by inserting nodes at the beginning or end of the level vector based on the current direction.