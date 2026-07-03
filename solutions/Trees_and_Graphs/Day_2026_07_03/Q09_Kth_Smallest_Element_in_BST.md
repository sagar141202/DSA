# Kth Smallest Element in BST

## Problem Statement
Given the root of a binary search tree (BST) and an integer k, find the kth smallest element in the BST. The solution should be efficient and scalable for large inputs. The BST is defined such that for every node, all elements in the left subtree are smaller, and all elements in the right subtree are greater. The problem constraints are: 1 <= k <= number of nodes in the BST, and the BST has at least k nodes. For example, given the BST with root node 5, left child 3, right child 6, and left child of 3 as 2, and right child of 3 as 4, the 3rd smallest element is 4.

## Approach
The approach involves using an in-order traversal of the BST to visit nodes in ascending order, and stopping when we've found the kth smallest element. We can optimize this by using a stack to store nodes to visit, allowing us to avoid recursion. Alternatively, we can use a Morris traversal to achieve the same result without using extra space for the recursion stack.

## Complexity
- Time: O(h + k)
- Space: O(h)

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
        // Initialize stack to store nodes to visit
        stack<TreeNode*> st;
        // Initialize current node to root
        TreeNode* curr = root;
        
        // Traverse the BST
        while (curr || !st.empty()) {
            // Go as far left as possible, pushing nodes onto the stack
            while (curr) {
                st.push(curr);
                curr = curr->left;
            }
            // Visit the top node on the stack (the next smallest node)
            curr = st.top();
            st.pop();
            k--;
            // If this is the kth smallest node, return its value
            if (k == 0) return curr->val;
            // Move to the right subtree
            curr = curr->right;
        }
        // If we've reached this point, the kth smallest node was not found
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
- The kth smallest element in a BST can be found efficiently using an in-order traversal.
- A stack can be used to store nodes to visit, allowing us to avoid recursion and reduce space complexity.
- The time complexity is O(h + k), where h is the height of the tree, because we may need to traverse the height of the tree to reach the kth smallest element.