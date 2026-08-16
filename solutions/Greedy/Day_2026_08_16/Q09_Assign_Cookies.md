# Assign Cookies

## Problem Statement
Assign Cookies is a problem where we have a list of child satisfaction levels and a list of cookie sizes. We need to assign a cookie to each child such that the child's satisfaction level is met. The goal is to find the maximum number of children that can be satisfied. The constraints are: each child can only be assigned one cookie, and each cookie can only be assigned to one child. For example, if we have child satisfaction levels [1,2,3] and cookie sizes [1,1], we can only satisfy 2 children.

## Approach
The algorithm uses a greedy approach by sorting both the child satisfaction levels and the cookie sizes. It then iterates through the sorted lists, assigning the smallest possible cookie to each child.

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
        // Sort both the child satisfaction levels and the cookie sizes
        sort(g.begin(), g.end());
        sort(s.begin(), s.end());
        
        int child = 0, cookie = 0;
        // Iterate through the sorted lists
        while (child < g.size() && cookie < s.size()) {
            // If the current cookie can satisfy the current child, assign it
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
- Sort both lists to apply the greedy approach.
- Assign the smallest possible cookie to each child to maximize the number of satisfied children.
- Use two pointers to iterate through the sorted lists.