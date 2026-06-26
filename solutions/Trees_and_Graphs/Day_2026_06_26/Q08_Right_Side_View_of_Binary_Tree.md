# Right Side View of Binary Tree

## Problem Statement
Given the root of a binary tree, return the rightmost node value at each level. The rightmost node value at each level is the last node value when traversing the level from left to right. The input tree is a binary tree where each node has a unique value, and the number of nodes in the tree is in the range [1, 100]. The node values are in the range [1, 100]. For example, given the binary tree `[1,2,3,null,5,null,4]`, the right side view is `[1,3,4]`.

## Approach
The algorithm uses a level-order traversal (BFS) to traverse the binary tree level by level. At each level, the last node value is added to the result list. This approach ensures that the rightmost node value at each level is included in the result.

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
        vector<int> result;
        if (!root) return result;
        
        queue<TreeNode*> q;
        q.push(root);
        
        while (!q.empty()) {
            int levelSize = q.size();
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
- Use level-order traversal (BFS) to traverse the binary tree level by level.
- At each level, add the last node value to the result list.
- The time complexity is O(N), where N is the number of nodes in the tree, and the space complexity is O(N) due to the queue used in the BFS traversal.