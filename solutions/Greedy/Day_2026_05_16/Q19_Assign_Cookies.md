# Assign Cookies

## Problem Statement
Assign Cookies is a problem where we have a list of children and a list of cookies. Each child has a greed factor, which is the minimum size of the cookie they will accept. We need to assign cookies to children such that the maximum number of children are satisfied. The constraint is that we cannot assign a cookie to a child if the cookie's size is less than the child's greed factor. The goal is to find the maximum number of children that can be satisfied.

## Approach
The approach to solve this problem is to use a greedy algorithm, sorting both the children's greed factors and the cookies' sizes in ascending order. We then iterate through the sorted lists, assigning the smallest possible cookie to each child.

## Complexity
- Time: O(n log n + m log m)
- Space: O(1)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int findContentChildren(vector<int>& g, vector<int>& s) {
        // Sort the children's greed factors and the cookies' sizes in ascending order
        sort(g.begin(), g.end());
        sort(s.begin(), s.end());
        
        int child = 0; // Pointer to the current child
        int cookie = 0; // Pointer to the current cookie
        
        // Iterate through the sorted lists, assigning the smallest possible cookie to each child
        while (child < g.size() && cookie < s.size()) {
            if (s[cookie] >= g[child]) {
                // If the current cookie can satisfy the current child, move to the next child
                child++;
            }
            // Move to the next cookie
            cookie++;
        }
        
        // Return the maximum number of children that can be satisfied
        return child;
    }
};
```

## Test Cases
```
Input: g = [1,2,3], s = [1,1]
Output: 1
Input: g = [1,2], s = [1,2,3]
Output: 2
```

## Key Takeaways
- Sort the input lists to apply the greedy algorithm.
- Use two pointers to iterate through the sorted lists and assign cookies to children.
- The time complexity is dominated by the sorting operation, which is O(n log n + m log m) in this case.