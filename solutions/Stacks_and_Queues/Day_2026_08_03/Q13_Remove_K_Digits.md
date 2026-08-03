# Remove K Digits
## Problem Statement
Given a non-negative integer num represented as a string, remove k digits from the number so that the resulting number is the smallest possible. The number may have leading zeros after removal. Note that the input number may be very large and may not fit in a 64-bit signed integer. For example, given num = "1432219" and k = 3, the output should be "1219". If num = "10200" and k = 1, the output should be "2000" or "0200" but since we want the smallest number, the leading zeros should be removed, so the output should be "200" or simply "2" if all digits are zeros.

## Approach
We will use a stack-based approach to solve this problem, iterating over the input number from left to right and pushing digits to the stack if they are smaller than the top of the stack or if the stack is empty. If the stack is not empty and its top is larger than the current digit, we will pop the stack until it's empty or its top is smaller than the current digit, or we have removed k digits.

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
        // Initialize an empty stack
        string stack;
        
        // Iterate over the input number
        for (char c : num) {
            // While the stack is not empty, its top is larger than the current digit, and we can still remove digits
            while (k > 0 && !stack.empty() && stack.back() > c) {
                // Remove the top of the stack
                stack.pop_back();
                // Decrement the count of digits to remove
                k--;
            }
            // Push the current digit to the stack
            stack.push_back(c);
        }
        
        // If we still have digits to remove, remove them from the end of the stack
        if (k > 0) {
            stack.resize(stack.size() - k);
        }
        
        // Find the index of the first non-zero digit in the stack
        int start = 0;
        while (start < stack.size() && stack[start] == '0') {
            start++;
        }
        
        // If the stack is empty or only contains zeros, return "0"
        if (start == stack.size()) {
            return "0";
        }
        
        // Return the result as a string
        return stack.substr(start);
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
- Use a stack to keep track of the digits in the resulting number.
- Remove digits from the stack if they are larger than the current digit and we can still remove digits.
- If we still have digits to remove after iterating over the input number, remove them from the end of the stack.
- Remove leading zeros from the result before returning it.