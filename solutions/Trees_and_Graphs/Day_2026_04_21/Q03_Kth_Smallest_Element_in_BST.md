# Kth Smallest Element in BST

## Problem Statement
Given the root of a binary search tree (BST) and an integer k, find the kth smallest element in the BST. The solution should return the value of the kth smallest element, or -1 if the kth smallest element does not exist. The BST is guaranteed to have at most 10^4 nodes, and k is guaranteed to be between 1 and the number of nodes in the BST. For example, given the BST with the following structure:
       5
      / \
     3   6
    / \
   2   4
  /
 1
The 3rd smallest element is 3.

## Approach
The algorithm uses an in-order traversal of the BST to visit the nodes in ascending order. It keeps track of the current node index and returns the node's value when the index matches k. The traversal is performed recursively or iteratively using a stack.

## Complexity
- Time: O(n)
- Space: O(n)

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
        int count = 0;
        
        while (curr || !s.empty()) {
            // Traverse to the leftmost node
            while (curr) {
                s.push(curr);
                curr = curr->left;
            }
            
            // Visit the node
            curr = s.top();
            s.pop();
            count++;
            
            // Check if this is the kth smallest element
            if (count == k) {
                return curr->val;
            }
            
            // Move to the right subtree
            curr = curr->right;
        }
        
        // If k is larger than the number of nodes, return -1
        return -1;
    }
};
```

## Test Cases
```
Input: root = [5,3,6,2,4,1], k = 3
Output: 3
```

## Key Takeaways
- In-order traversal visits nodes in ascending order for a BST.
- Using a stack allows for efficient iterative traversal of the BST.
- The solution has a time complexity of O(n) due to the traversal of all nodes in the worst case.