# Assign Cookies

## Problem Statement
Assign Cookies is a problem where we have a list of child satisfaction levels and a list of cookie sizes. We need to assign cookies to children such that each child gets a cookie that satisfies their satisfaction level. The goal is to find the maximum number of children that can be satisfied. The constraints are: each child can only get one cookie, and each cookie can only be assigned to one child. For example, if we have child satisfaction levels [1,2,3] and cookie sizes [1,1], we can only satisfy 2 children.

## Approach
The algorithm uses a greedy approach by sorting both the child satisfaction levels and the cookie sizes in ascending order. Then, it iterates over the sorted lists, assigning the smallest possible cookie to each child. This approach ensures that we maximize the number of satisfied children.

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
        // Sort child satisfaction levels and cookie sizes in ascending order
        sort(g.begin(), g.end());
        sort(s.begin(), s.end());
        
        int child = 0; // Pointer for child satisfaction levels
        int cookie = 0; // Pointer for cookie sizes
        
        // Iterate over the sorted lists
        while (child < g.size() && cookie < s.size()) {
            // If the current cookie can satisfy the current child, assign it
            if (s[cookie] >= g[child]) {
                child++; // Move to the next child
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
- Sort the input lists to apply the greedy approach effectively.
- Use two pointers to iterate over the sorted lists and assign cookies to children.
- The algorithm's time complexity is dominated by the sorting step.