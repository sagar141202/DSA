# Remove K Digits

## Problem Statement
Given a non-negative integer num represented as a string, remove k digits from the number so that the resulting number is the smallest possible. The constraints are: 1 <= k <= num.length <= 10000, and num does not contain any leading zero. For example, if num = "1432219" and k = 3, the output should be "1219". If num = "10200" and k = 1, the output should be "2000", and if num = "10" and k = 2, the output should be "0".

## Approach
The approach is to use a stack to keep track of the digits. We iterate through the string and push each digit to the stack. If the stack is not empty and the top of the stack is greater than the current digit, we pop the stack until it is empty or the top of the stack is less than or equal to the current digit, or we have removed k digits. This ensures that the resulting number is the smallest possible.

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
        // Create a stack to store the digits
        string stack;
        // Iterate through each digit in the number
        for (char c : num) {
            // While the stack is not empty, the top of the stack is greater than the current digit, and we have not removed k digits
            while (k > 0 && !stack.empty() && stack.back() > c) {
                // Remove the top of the stack
                stack.pop_back();
                // Decrement k
                k--;
            }
            // Push the current digit to the stack
            stack.push_back(c);
        }
        // If we have not removed k digits, remove the remaining digits from the end of the stack
        if (k > 0) {
            stack.erase(stack.size() - k);
        }
        // Remove leading zeros from the stack
        while (!stack.empty() && stack[0] == '0') {
            stack.erase(stack.begin());
        }
        // If the stack is empty, return "0"
        if (stack.empty()) {
            return "0";
        }
        // Return the resulting number
        return stack;
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
- Use a stack to keep track of the digits and remove digits from the stack when a smaller digit is encountered.
- Remove leading zeros from the resulting number.
- Handle edge cases where the resulting number is empty or has only one digit.