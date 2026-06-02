# Assign Cookies

## Problem Statement
Assign Cookies is a problem where we have a list of child's greed factors and a list of cookie sizes. We need to assign a cookie to each child such that the child's greed factor is satisfied. The goal is to find the maximum number of children that can be satisfied. The constraints are: each child can only be assigned one cookie, and each cookie can only be assigned to one child. For example, if we have two children with greed factors [1, 2] and three cookies with sizes [1, 2, 3], we can assign the first cookie to the first child and the second cookie to the second child, satisfying both children.

## Approach
The algorithm uses a greedy approach, sorting both the child's greed factors and the cookie sizes in ascending order. We then iterate over the sorted lists, assigning the smallest possible cookie to each child. This approach ensures that we maximize the number of satisfied children.

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
        // Sort the child's greed factors and the cookie sizes in ascending order
        sort(g.begin(), g.end());
        sort(s.begin(), s.end());
        
        int child = 0, cookie = 0;
        // Iterate over the sorted lists, assigning the smallest possible cookie to each child
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
Input: g = [1, 2, 3], s = [1, 1]
Output: 1
Input: g = [1, 2], s = [1, 2, 3]
Output: 2
```

## Key Takeaways
- Sort the input lists to simplify the problem and apply the greedy approach.
- Use two pointers to iterate over the sorted lists and assign cookies to children.
- The time complexity is dominated by the sorting operation, making the algorithm efficient for large inputs.