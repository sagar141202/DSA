# Assign Cookies

## Problem Statement
Given an array of integers representing the number of cookies each child wants and an array of integers representing the number of cookies each cookie has, assign cookies to children such that the maximum number of children are satisfied. A child is satisfied if they receive a cookie that is greater than or equal to the number of cookies they want. The goal is to find the maximum number of children that can be satisfied.

## Approach
The approach to this problem is to sort both the children's preferences and the cookies in ascending order, then use two pointers to iterate over the sorted arrays. We assign a cookie to a child if the cookie is greater than or equal to the child's preference.

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
        // Sort both arrays in ascending order
        sort(g.begin(), g.end());
        sort(s.begin(), s.end());
        
        int child = 0, cookie = 0;
        // Iterate over the sorted arrays
        while (child < g.size() && cookie < s.size()) {
            // If a cookie satisfies a child, move to the next child
            if (s[cookie] >= g[child]) {
                child++;
            }
            // Move to the next cookie
            cookie++;
        }
        // Return the number of satisfied children
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
- Sort both arrays to ensure the smallest children are satisfied first with the smallest cookies.
- Use two pointers to iterate over the sorted arrays, assigning cookies to children as needed.
- The time complexity is dominated by the sorting operations, while the space complexity is constant as no additional space is used that scales with input size.