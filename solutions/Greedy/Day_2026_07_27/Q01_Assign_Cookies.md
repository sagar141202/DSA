# Assign Cookies

## Problem Statement
Assign Cookies is a problem where we have a list of children with different levels of greed factor and a list of cookies with different sizes. We need to assign one cookie to each child such that the child's greed factor is satisfied (i.e., the size of the cookie is greater than or equal to the child's greed factor). The goal is to find the maximum number of children that can be satisfied. The constraints are: 1 <= g.length <= 3 * 10^4, 1 <= s.length <= 3 * 10^4, 1 <= g[i], s[j] <= 2^31 - 1.

## Approach
The algorithm uses a greedy approach, sorting both the children's greed factors and the cookies' sizes in ascending order. Then, it iterates through the sorted lists, assigning the smallest possible cookie to each child.

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
        // Sort the children's greed factors and the cookies' sizes in ascending order
        sort(g.begin(), g.end());
        sort(s.begin(), s.end());
        
        int child = 0; // Index for the children
        int cookie = 0; // Index for the cookies
        
        // Iterate through the sorted lists
        while (child < g.size() && cookie < s.size()) {
            // If the current cookie can satisfy the current child, assign it
            if (s[cookie] >= g[child]) {
                child++;
            }
            // Move to the next cookie
            cookie++;
        }
        
        // The number of satisfied children is the index of the last satisfied child
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
- Sort the input lists to apply the greedy approach.
- Use two pointers to iterate through the sorted lists and assign cookies to children.
- The number of satisfied children is the index of the last satisfied child.