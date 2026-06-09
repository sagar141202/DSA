# Assign Cookies

## Problem Statement
Assign Cookies is a problem where we have a list of kid sizes and a list of cookie sizes. We need to assign a cookie to each kid such that the kid's size is less than or equal to the cookie size. The goal is to find the maximum number of kids that can be assigned a cookie. The problem has the following constraints: 1 <= g.length <= 3 * 10^4, 1 <= s.length <= 3 * 10^4, 1 <= g[i] <= 2 * 10^4, 1 <= s[j] <= 2 * 10^4. For example, if we have kid sizes [1,2,3] and cookie sizes [1,1], we can assign a cookie to the first kid, resulting in a total of 1 kid being assigned a cookie.

## Approach
The algorithm uses a greedy approach, sorting both the kid sizes and cookie sizes in ascending order. It then iterates over the sorted lists, assigning a cookie to each kid if the kid's size is less than or equal to the cookie size. This approach ensures that the maximum number of kids can be assigned a cookie.

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
        // Sort kid sizes and cookie sizes in ascending order
        sort(g.begin(), g.end());
        sort(s.begin(), s.end());

        int kidIndex = 0;
        int cookieIndex = 0;

        // Assign cookies to kids
        while (kidIndex < g.size() && cookieIndex < s.size()) {
            if (g[kidIndex] <= s[cookieIndex]) {
                // Assign a cookie to the kid
                kidIndex++;
            }
            // Move to the next cookie
            cookieIndex++;
        }

        // Return the number of kids assigned a cookie
        return kidIndex;
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
- Sort both kid sizes and cookie sizes in ascending order to ensure the maximum number of kids can be assigned a cookie.
- Use a greedy approach to assign cookies to kids, moving to the next cookie after each assignment.
- The time complexity is O(n log n + m log m) due to the sorting, and the space complexity is O(1) as no additional space is used.