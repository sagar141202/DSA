# Right Side View of Binary Tree

## Problem Statement
Given the root of a binary tree, return the rightmost node value at each level, from top to bottom. The input tree is a binary tree where each node has a unique value and at most two children (i.e., left child and right child). The number of nodes in the tree is in the range [0, 100]. The input tree is not guaranteed to be balanced. For example, given the following binary tree:
```
    1
   / \
  2   3
 / \
4   5
```
The right side view of the binary tree is [1, 3, 5]. 

## Approach
We will use a level order traversal (BFS) approach to solve this problem, where we traverse the tree level by level and keep track of the last node at each level.

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
        if (!root) {
            return result;
        }

        queue<TreeNode*> q;
        q.push(root);

        while (!q.empty()) {
            int levelSize = q.size();
            for (int i = 0; i < levelSize; i++) {
                TreeNode* currentNode = q.front();
                q.pop();

                // If it's the last node at the current level, add it to the result
                if (i == levelSize - 1) {
                    result.push_back(currentNode->val);
                }

                if (currentNode->left) {
                    q.push(currentNode->left);
                }
                if (currentNode->right) {
                    q.push(currentNode->right);
                }
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
   / \
  2   3
 / \
4   5
Output: [1, 3, 5]

Input: 
    1
   / \
  2   3
Output: [1, 3]
```

## Key Takeaways
- Use level order traversal (BFS) to solve this problem.
- Keep track of the last node at each level to find the right side view.
- Use a queue to store nodes at each level.