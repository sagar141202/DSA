# Kth Smallest Element in BST

## Problem Statement
Given the root of a binary search tree (BST) and an integer k, find the kth smallest element in the BST. The BST contains unique integers, and you can assume that k is within the range of the number of nodes in the BST (1-indexed). For example, if the BST is [5,3,6,2,4,null,null,1], the kth smallest element is 3 when k = 3, because the order of the elements in the BST (in-order traversal) is [1,2,3,4,5,6].

## Approach
We will use an in-order traversal of the BST and keep track of the current node index. When the index reaches k, we return the current node's value. This approach works because in-order traversal visits nodes in ascending order.

## Complexity
- Time: O(h + k), where h is the height of the BST and k is the input integer
- Space: O(h), for the recursive call stack in the worst case

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
    int kthSmallest(TreeNode* root, int k) {
        stack<TreeNode*> st;
        TreeNode* curr = root;
        int count = 0;
        
        // Traverse the tree using in-order traversal
        while (curr || !st.empty()) {
            // Move to the leftmost node
            while (curr) {
                st.push(curr);
                curr = curr->left;
            }
            
            // Visit the node and update count
            curr = st.top();
            st.pop();
            count++;
            
            // If count reaches k, return the node's value
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
Input: root = [5,3,6,2,4,null,null,1], k = 3
Output: 3
Input: root = [5,3,6,2,4,null,null,1], k = 1
Output: 1
```

## Key Takeaways
- In-order traversal visits nodes in ascending order, making it suitable for finding the kth smallest element in a BST.
- Using a stack to implement in-order traversal can help avoid recursive function calls and reduce space complexity.
- Keeping track of the current node index during traversal allows us to find the kth smallest element efficiently.