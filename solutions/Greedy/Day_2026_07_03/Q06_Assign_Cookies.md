# Assign Cookies

## Problem Statement
Assign Cookies problem is a classic problem in Greedy algorithms. We are given two arrays, `g` and `s`, where `g[i]` represents the greed factor of the `i-th` child and `s[j]` represents the size of the `j-th` cookie. We need to find the maximum number of children who can be satisfied with the given cookies. A child can be satisfied if we assign a cookie that is greater than or equal to their greed factor. The goal is to maximize the number of satisfied children.

## Approach
The approach is to sort both the greed factors and the cookie sizes in ascending order, then use two pointers to assign cookies to children. We start by assigning the smallest cookie to the child with the smallest greed factor and move towards the larger cookies and children.

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
        // Sort the greed factors and cookie sizes in ascending order
        sort(g.begin(), g.end());
        sort(s.begin(), s.end());
        
        int child = 0; // Pointer for children
        int cookie = 0; // Pointer for cookies
        
        // Assign cookies to children
        while (child < g.size() && cookie < s.size()) {
            if (s[cookie] >= g[child]) {
                child++; // Child is satisfied, move to the next child
            }
            cookie++; // Move to the next cookie
        }
        
        return child; // Return the number of satisfied children
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
- Sort the input arrays to apply the Greedy approach.
- Use two pointers to keep track of the current child and cookie.
- Assign a cookie to a child only if the cookie size is greater than or equal to the child's greed factor.