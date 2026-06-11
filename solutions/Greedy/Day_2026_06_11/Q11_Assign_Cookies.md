# Assign Cookies

## Problem Statement
Assign Cookies is a problem where we have a list of children with different levels of greed factor and a list of cookies with different sizes. We need to assign a cookie to each child such that the child's greed factor is satisfied. The goal is to find the maximum number of children that can be satisfied. The constraints are: each child can be assigned at most one cookie, and each cookie can be assigned to at most one child. For example, if we have two children with greed factors [1, 2] and three cookies with sizes [1, 2, 3], we can assign the first cookie to the first child and the second cookie to the second child, satisfying both children.

## Approach
The algorithm uses a greedy approach by sorting both the children's greed factors and the cookie sizes in ascending order. Then, we iterate through the sorted lists and assign the smallest possible cookie to each child. This approach ensures that we maximize the number of satisfied children. We use two pointers to track the current position in the sorted lists.

## Complexity
- Time: O(n log n + m log m)
- Space: O(1)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

int findContentChildren(vector<int>& g, vector<int>& s) {
    // Sort the children's greed factors and the cookie sizes in ascending order
    sort(g.begin(), g.end());
    sort(s.begin(), s.end());
    
    int child = 0;  // Pointer for the children's greed factors
    int cookie = 0;  // Pointer for the cookie sizes
    
    // Iterate through the sorted lists and assign cookies to children
    while (child < g.size() && cookie < s.size()) {
        if (s[cookie] >= g[child]) {
            child++;  // Assign the current cookie to the current child
        }
        cookie++;  // Move to the next cookie
    }
    
    return child;  // Return the number of satisfied children
}
```

## Test Cases
```
Input: g = [1, 2, 3], s = [1, 1]
Output: 1

Input: g = [1, 2], s = [1, 2, 3]
Output: 2
```

## Key Takeaways
- Use a greedy approach to solve the problem by sorting the input lists and iterating through them.
- Use two pointers to track the current position in the sorted lists.
- The time complexity is dominated by the sorting operations, which have a time complexity of O(n log n) and O(m log m) for the children's greed factors and the cookie sizes, respectively.