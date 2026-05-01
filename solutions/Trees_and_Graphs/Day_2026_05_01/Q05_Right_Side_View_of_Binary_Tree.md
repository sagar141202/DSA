# Right Side View of Binary Tree

## Problem Statement
Given the root of a binary tree, return the rightmost node value at each level, from left to right. The input tree is a binary tree where each node has a value and two children (left and right). The tree is not guaranteed to be balanced, and the number of nodes can range from 0 to 10^4. For example, given the binary tree [1,2,3,null,5,null,4], the right side view is [1,3,4].

## Approach
We will use a level-order traversal (BFS) to solve this problem, where we process each level of the tree from left to right and store the last node value at each level. This approach ensures that we capture the rightmost node value at each level.

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
        if (!root) return {};
        
        vector<int> result;
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
Input: [1]
Output: [1]
Input: []
Output: []
```

## Key Takeaways
- Use level-order traversal (BFS) to process the tree level by level.
- Store the last node value at each level to capture the rightmost node value.
- Utilize a queue data structure to manage the nodes at each level.