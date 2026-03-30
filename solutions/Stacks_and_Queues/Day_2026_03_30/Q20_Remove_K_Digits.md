# Remove K Digits

## Problem Statement
Given a non-negative integer num represented as a string, remove k digits from the number so that the resulting number is the smallest possible. The constraints are: 1 <= num.length() <= 20000, num consists of only digits, and 1 <= k <= num.length(). For example, if num = "1432219" and k = 3, the output should be "1219".

## Approach
To solve this problem, we can use a stack data structure to keep track of the digits. We iterate through the number from left to right, and for each digit, we check if the stack is not empty and the top of the stack is greater than the current digit. If it is, we pop the stack until it's empty or the top is not greater than the current digit, or we have removed k digits.

## Complexity
- Time: O(n)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    string removeKdigits(string num, int k) {
        string res;
        for (char c : num) {
            while (k > 0 && !res.empty() && res.back() > c) {
                res.pop_back();
                k--;
            }
            res.push_back(c);
        }
        while (k > 0 && !res.empty()) {
            res.pop_back();
            k--;
        }
        // Remove leading zeros
        while (!res.empty() && res[0] == '0') {
            res.erase(0, 1);
        }
        return res.empty() ? "0" : res;
    }
};
```

## Test Cases
```
Input: num = "1432219", k = 3
Output: "1219"
Input: num = "10200", k = 1
Output: "2000"
Input: num = "10", k = 2
Output: "0"
```

## Key Takeaways
- Use a stack to keep track of the digits and remove k digits from the number to get the smallest possible number.
- Iterate through the number from left to right and pop the stack when the top of the stack is greater than the current digit.
- Remove leading zeros from the result to get the final answer.