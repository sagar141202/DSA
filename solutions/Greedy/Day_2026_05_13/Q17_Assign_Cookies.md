# Assign Cookies

## Problem Statement
Assign Cookies is a problem where we have a list of children with their greed factors and a list of cookies with their sizes. We want to assign cookies to children such that the maximum number of children are satisfied. A child is satisfied if the size of the cookie assigned to them is greater than or equal to their greed factor. The goal is to find the maximum number of children that can be satisfied. The constraints are: 1 <= g.length <= 3 * 10^4, 1 <= s.length <= 3 * 10^4, 1 <= g[i], s[j] <= 2^31 - 1.

## Approach
The algorithm uses a greedy approach by sorting both the children's greed factors and the cookie sizes in ascending order. Then it iterates through the sorted lists, assigning the smallest possible cookie to each child. This ensures that the maximum number of children are satisfied.

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
        // Sort the children's greed factors and the cookie sizes in ascending order
        sort(g.begin(), g.end());
        sort(s.begin(), s.end());
        
        int child = 0; // Index of the current child
        int cookie = 0; // Index of the current cookie
        
        // Iterate through the sorted lists
        while (child < g.size() && cookie < s.size()) {
            // If the current cookie can satisfy the current child, move to the next child
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
- The greedy approach is used to solve this problem by assigning the smallest possible cookie to each child.
- Sorting the lists in ascending order allows us to efficiently find the maximum number of children that can be satisfied.
- The time complexity is dominated by the sorting operation, which has a time complexity of O(n log n + m log m).