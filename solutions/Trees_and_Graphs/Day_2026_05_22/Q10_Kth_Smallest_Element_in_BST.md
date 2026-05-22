# Kth Smallest Element in BST

## Problem Statement
Given the root of a binary search tree (BST) and an integer k, find the kth smallest element in the BST. The BST is guaranteed to have k nodes. The problem can be solved by using an in-order traversal of the tree and keeping track of the current node index. The tree nodes have unique values and are defined as follows: each node has a value, a left child, and a right child. For example, if we have the following tree: 
       5
      / \
     3   6
    / \
   2   4
  /
 1
and k = 3, then the output will be 3.

## Approach
We can solve this problem by performing an in-order traversal of the binary search tree, which visits nodes in ascending order. We use a stack to implement the traversal iteratively. Once we've visited k nodes, we return the value of the kth node.

## Complexity
- Time: O(h + k), where h is the height of the tree
- Space: O(h), where h is the height of the tree

## C++ Solution
```cpp
#include <stack>
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
    int kthSmallest(TreeNode* root, int k) {
        stack<TreeNode*> s;
        TreeNode* curr = root;
        while (curr || !s.empty()) {
            // go as far left as possible
            while (curr) {
                s.push(curr);
                curr = curr->left;
            }
            // backtracking
            curr = s.top();
            s.pop();
            k--;
            if (k == 0) {
                return curr->val;
            }
            curr = curr->right;
        }
        return -1; // if k is larger than the number of nodes
    }
};
```

## Test Cases
```
Input: root = [3,1,4,null,2], k = 1
Output: 1
Input: root = [5,3,6,2,4,null,null,1], k = 3
Output: 3
```

## Key Takeaways
- In-order traversal visits nodes in ascending order for a binary search tree.
- Using a stack allows for an iterative solution instead of recursive.
- The time complexity is O(h + k) because we visit at most h + k nodes, where h is the height of the tree.