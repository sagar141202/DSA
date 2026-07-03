# Remove K Digits

## Problem Statement
Given a non-negative integer num represented as a string, remove k digits from the number so that the resulting number is the smallest possible. The number will not contain any leading zeros after removal, and the removal should be done in such a way that the resulting number is the smallest possible. For example, if num = "1432219" and k = 3, the output should be "1219". The constraints are 1 <= k <= num.length <= 10^5, and num consists of only digits.

## Approach
We can solve this problem using a stack data structure. The idea is to iterate over the string and push characters into the stack if the stack is empty or the top of the stack is less than or equal to the current character. If the top of the stack is greater than the current character and we can still remove digits, we remove the top of the stack.

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
        string stack;
        for (char c : num) {
            // remove digits from the stack if they are larger than the current digit
            while (k > 0 && !stack.empty() && stack.back() > c) {
                stack.pop_back();
                k--;
            }
            // do not push leading zeros into the stack
            if (!stack.empty() || c != '0') {
                stack.push_back(c);
            }
        }
        // if we still have digits to remove, remove them from the end of the stack
        while (k > 0 && !stack.empty()) {
            stack.pop_back();
            k--;
        }
        return stack.empty() ? "0" : stack;
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
- Using a stack to keep track of the digits in the resulting number is an efficient way to solve this problem.
- The key to this problem is to remove the larger digits from the stack when we encounter a smaller digit, which ensures the resulting number is the smallest possible.
- We need to handle the case where the resulting number is empty (i.e., all digits are removed), in which case the answer is "0".