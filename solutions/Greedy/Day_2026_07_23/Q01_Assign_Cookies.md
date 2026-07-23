# Assign Cookies

## Problem Statement
Assign Cookies is a problem where we have a list of child's greed factors and a list of cookie sizes. We need to assign a cookie to each child such that the child's greed factor is satisfied. The goal is to find the maximum number of children that can be satisfied. The constraints are: each child can only be assigned one cookie, and each cookie can only be assigned to one child. For example, if we have the greed factors [1,2,3] and cookie sizes [1,2], we can satisfy 2 children.

## Approach
The approach to solve this problem is to use a greedy algorithm, sorting both the child's greed factors and the cookie sizes in ascending order. We then iterate through both lists, assigning the smallest possible cookie to each child.

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
        // Sort both the child's greed factors and the cookie sizes in ascending order
        sort(g.begin(), g.end());
        sort(s.begin(), s.end());
        
        int child = 0, cookie = 0;
        // Iterate through both lists, assigning the smallest possible cookie to each child
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
- Sort both lists to ensure we're always comparing the smallest possible values.
- Use a two-pointer technique to iterate through both lists simultaneously.
- The greedy algorithm works because we're always choosing the smallest possible cookie for each child, ensuring the maximum number of children are satisfied.