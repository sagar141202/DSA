# Kth Smallest Element in BST

## Problem Statement
Given the root of a binary search tree (BST) and an integer k, find the kth smallest element in the BST. The solution should return the value of the kth smallest element. The input BST is guaranteed to have k nodes, and k is between 1 and the number of nodes in the BST. For example, if the input BST is:
       5
      / \
     3   6
    / \
   2   4
and k = 3, the output should be 3, which is the 3rd smallest element in the BST.

## Approach
The algorithm uses in-order traversal of the BST to visit nodes in ascending order. It keeps track of the current node index and returns the node value when the index matches k. The in-order traversal is implemented recursively or iteratively using a stack.

## Complexity
- Time: O(h + k), where h is the height of the BST
- Space: O(h), for the recursive call stack or iterative stack

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
    int kthSmallest(TreeNode* root, int k) {
        stack<TreeNode*> s;
        TreeNode* curr = root;
        while (curr || !s.empty()) {
            // go as far left as possible
            while (curr) {
                s.push(curr);
                curr = curr->left;
            }
            // visit the node
            curr = s.top();
            s.pop();
            k--;
            if (k == 0) {
                return curr->val;
            }
            // move to the right subtree
            curr = curr->right;
        }
        // should not reach here
        return -1;
    }
};
```

## Test Cases
```
Input: root = [5,3,6,2,4], k = 3
Output: 3
Input: root = [5,3,6,2,4], k = 1
Output: 2
```

## Key Takeaways
- Use in-order traversal to visit nodes in ascending order
- Keep track of the current node index to find the kth smallest element
- Implement in-order traversal recursively or iteratively using a stack to avoid recursion stack overflow for large inputs