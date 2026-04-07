# Remove K Digits

## Problem Statement
Given a non-negative integer num represented as a string, remove k digits from the number so that the resulting number is the smallest possible. The constraints are: 1 <= k <= num.length <= 10000, and num does not contain any leading zero. For example, if num = "1432219" and k = 3, the output should be "1219" because we can remove the digits 4, 3, and 2 to get the smallest possible number.

## Approach
We can use a stack-based approach to solve this problem, where we iterate through the number from left to right and pop the stack whenever we encounter a digit that is smaller than the current digit. This ensures that the resulting number is the smallest possible. We also keep track of the number of digits removed.

## Complexity
- Time: O(n)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

string removeKdigits(string num, int k) {
    // Initialize an empty stack
    string stack;
    
    // Iterate through the number
    for (char c : num) {
        // While the stack is not empty and the top of the stack is greater than the current digit
        while (k > 0 && !stack.empty() && stack.back() > c) {
            // Pop the stack
            stack.pop_back();
            // Decrement k
            k--;
        }
        // Push the current digit to the stack
        stack.push_back(c);
    }
    
    // If k is still greater than 0, remove the remaining digits from the end
    if (k > 0) {
        stack.erase(stack.size() - k);
    }
    
    // Remove leading zeros
    while (!stack.empty() && stack[0] == '0') {
        stack.erase(stack.begin());
    }
    
    // Return the resulting number
    return stack.empty() ? "0" : stack;
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
- Use a stack-based approach to remove k digits from a number to get the smallest possible number.
- Iterate through the number from left to right and pop the stack whenever we encounter a digit that is smaller than the current digit.
- Keep track of the number of digits removed and remove the remaining digits from the end if necessary.