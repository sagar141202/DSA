# Binary Tree Zigzag Level Order Traversal

## Problem Statement
Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. The solution should handle trees of any size and structure. For example, given a binary tree with the following structure:
```
    3
   / \
  9  20
    /  \
   15   7
```
The zigzag level order traversal would be `[[3], [20, 9], [15, 7]]`. The constraints for this problem are that the input tree is a valid binary tree, and the output should be a vector of vectors where each inner vector represents a level in the tree.

## Approach
The algorithm uses a level order traversal (BFS) approach with a deque to store nodes at each level. It iterates through the tree level by level, alternating the order of nodes at each level.

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
        if (!root) return {};
        
        vector<vector<int>> result;
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
```

## Key Takeaways
- The use of a queue allows for efficient level order traversal.
- Alternating the `leftToRight` flag at each level achieves the zigzag effect.
- Using `vector.insert` to add elements at the beginning when traversing from right to left is less efficient than using `deque` for this purpose. However, the provided solution demonstrates a straightforward approach with vectors. For optimal performance, consider using a `deque` instead.