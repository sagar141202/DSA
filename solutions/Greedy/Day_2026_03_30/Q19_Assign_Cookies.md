# Assign Cookies

## Problem Statement
Assign Cookies is a problem where we have a list of child's greed factors and a list of cookie sizes. We need to assign cookies to the children such that the number of assigned cookies is maximized and each child gets a cookie that satisfies their greed factor. The constraints are: each child can only get one cookie, and each cookie can only be assigned to one child. The goal is to find the maximum number of children who can get a cookie that satisfies their greed factor.

## Approach
We will sort both the child's greed factors and the cookie sizes in ascending order. Then, we will use two pointers to assign cookies to the children. The intuition is to assign the smallest possible cookie to each child, so we can maximize the number of assigned cookies.

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
        // Sort the child's greed factors and the cookie sizes
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
Input: g = [1,2,3], s = [1,1]
Output: 1
Input: g = [1,2], s = [1,2,3]
Output: 2
```

## Key Takeaways
- Sort the input arrays to simplify the problem.
- Use two pointers to assign cookies to the children.
- Assign the smallest possible cookie to each child to maximize the number of assigned cookies.