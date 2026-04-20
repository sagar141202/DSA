# Remove K Digits

## Problem Statement
Given a non-negative integer num represented as a string, remove k digits from the number so that the resulting number is the smallest possible. The constraints are: 1 <= k <= num.length <= 10000, and num does not contain any leading zeros except for the number 0 itself. For example, if num = "1432219" and k = 3, the output should be "1219".

## Approach
The approach is to use a stack to store the digits of the number. We iterate through the number from left to right, and for each digit, we check if the stack is not empty and the top of the stack is greater than the current digit. If it is, we pop the stack until it's empty or the top of the stack is not greater than the current digit, or we have removed k digits.

## Complexity
- Time: O(n)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

string removeKdigits(string num, int k) {
    // Create a stack to store the digits
    string stack;
    // Iterate through the number
    for (char c : num) {
        // While the stack is not empty and the top of the stack is greater than the current digit, and we have not removed k digits
        while (k > 0 && !stack.empty() && stack.back() > c) {
            // Pop the stack
            stack.pop_back();
            // Decrement k
            k--;
        }
        // Push the current digit to the stack
        stack.push_back(c);
    }
    // If we still have not removed k digits, remove the remaining digits from the end of the stack
    if (k > 0) {
        stack.resize(stack.size() - k);
    }
    // Find the first non-zero digit in the stack
    int start = 0;
    while (start < stack.size() && stack[start] == '0') {
        start++;
    }
    // Return the resulting number
    return start == stack.size() ? "0" : stack.substr(start);
}
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
- Use a stack to store the digits of the number.
- Iterate through the number from left to right and remove digits from the stack if they are greater than the current digit.
- If we still have not removed k digits, remove the remaining digits from the end of the stack.