# Right Side View of Binary Tree

## Problem Statement
Given the root of a binary tree, return the rightmost node value at each level. The rightmost node value at each level is the last node value when traversing the level from left to right. The input tree is a binary tree where each node has a value and two children (left and right). The number of nodes in the tree is in the range [0, 100], and the values of the nodes are in the range [-100, 100]. For example, given the following binary tree: 
       1
     /   \
    2     3
   / \     / \
  4   5   6   7
The right side view of this tree is [1, 3, 7].

## Approach
The solution uses a level order traversal (BFS) approach to traverse the tree level by level. At each level, it stores the last node value, which represents the rightmost node at that level. This approach ensures that the rightmost node at each level is captured.

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

        // Perform level order traversal
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
Input: 
       1
     /   \
    2     3
   / \     / \
  4   5   6   7
Output: [1, 3, 7]
```

## Key Takeaways
- Use level order traversal (BFS) to capture the rightmost node at each level.
- Store the last node value at each level to get the right side view.
- The time complexity is O(N), where N is the number of nodes in the tree, and the space complexity is O(N) due to the use of the queue.