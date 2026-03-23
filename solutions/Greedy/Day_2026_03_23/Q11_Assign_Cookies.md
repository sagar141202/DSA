# Assign Cookies

## Problem Statement
Given two arrays, `g` and `s`, where `g[i]` represents the greed factor of the `i-th` child and `s[j]` represents the size of the `j-th` cookie, assign cookies to the children such that the maximum number of children are satisfied. A child is satisfied if the size of the assigned cookie is greater than or equal to their greed factor. The goal is to find the maximum number of children that can be satisfied.

## Approach
The approach is to sort both arrays and then use a two-pointer technique to assign cookies to the children. The intuition is to assign the smallest possible cookie to each child to maximize the number of satisfied children.

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
        // Iterate through both arrays and assign cookies to the children
        while (child < g.size() && cookie < s.size()) {
            if (s[cookie] >= g[child]) {
                child++;
            }
            cookie++;
        }
        return child;
    }
};
```

## Test Cases
```
Input: g = [1,2,3], s = [1,2]
Output: 2
Input: g = [1,2], s = [1,2,3]
Output: 2
```

## Key Takeaways
- Sort both arrays to simplify the assignment process
- Use a two-pointer technique to assign cookies to the children
- Assign the smallest possible cookie to each child to maximize the number of satisfied children