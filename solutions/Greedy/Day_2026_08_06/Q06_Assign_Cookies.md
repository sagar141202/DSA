# Assign Cookies

## Problem Statement
Assign Cookies problem is a classic Greedy algorithm problem. We are given two arrays, `g` and `s`, where `g[i]` represents the greed factor of the `i-th` child and `s[j]` represents the size of the `j-th` cookie. We need to find the maximum number of children who can be satisfied with the given cookies. A child can be satisfied if the size of the cookie is greater than or equal to their greed factor. We need to assign the cookies in such a way that the maximum number of children are satisfied.

## Approach
The approach to solve this problem is to sort both the `g` and `s` arrays in ascending order. Then, we iterate through the sorted arrays and try to assign the smallest possible cookie to each child. If the cookie size is greater than or equal to the child's greed factor, we assign the cookie to the child and move to the next child.

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
        
        int child = 0, cookie = 0;
        // Iterate through the sorted arrays
        while (child < g.size() && cookie < s.size()) {
            // If the cookie size is greater than or equal to the child's greed factor, assign the cookie
            if (s[cookie] >= g[child]) {
                child++;
            }
            // Move to the next cookie
            cookie++;
        }
        // Return the maximum number of children who can be satisfied
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
- Sort the input arrays to apply the Greedy algorithm.
- Assign the smallest possible cookie to each child to maximize the number of satisfied children.
- The time complexity is dominated by the sorting operation.