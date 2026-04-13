# Assign Cookies

## Problem Statement
Assign Cookies is a problem where we have a list of child satisfaction levels and a list of cookie sizes. We need to assign cookies to the children such that the maximum number of children are satisfied. A child is satisfied if the assigned cookie size is greater than or equal to their satisfaction level. The goal is to find the maximum number of children that can be satisfied.

## Approach
We will use a greedy algorithm to solve this problem. The idea is to sort both the child satisfaction levels and the cookie sizes in ascending order. Then, we will iterate through the sorted lists and assign the smallest possible cookie to each child.

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
        // Sort the child satisfaction levels and cookie sizes in ascending order
        sort(g.begin(), g.end());
        sort(s.begin(), s.end());
        
        int child = 0, cookie = 0;
        // Assign cookies to the children
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
- Sort the input lists to apply the greedy algorithm.
- Iterate through the sorted lists to assign cookies to the children.
- The greedy algorithm ensures that the maximum number of children are satisfied.