# Remove K Digits

## Problem Statement
Given a non-negative integer num represented as a string, remove k digits from num such that the resulting integer is the smallest possible. The constraints are: 1 <= k <= num.size() - 1, and num will not contain any leading zeros except for the zero itself. For example, if num = "1432219" and k = 3, the output should be "1219".

## Approach
The approach is to use a stack to store the digits of the number. We iterate over the number from left to right, and for each digit, we check if the stack is not empty and the top of the stack is greater than the current digit. If it is, we pop the stack until it is empty or the top of the stack is not greater than the current digit, or we have removed k digits. We then push the current digit to the stack.

## Complexity
- Time: O(n)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

string removeKdigits(string num, int k) {
    // Initialize an empty stack to store the digits
    string stack;
    
    // Iterate over the number
    for (char c : num) {
        // While the stack is not empty and the top of the stack is greater than the current digit
        // and we have not removed k digits yet, pop the stack
        while (k > 0 && !stack.empty() && stack.back() > c) {
            stack.pop_back();
            k--;
        }
        // Push the current digit to the stack
        stack.push_back(c);
    }
    
    // If we have not removed k digits yet, remove the remaining digits from the end of the stack
    if (k > 0) {
        stack.erase(stack.size() - k);
    }
    
    // Remove leading zeros
    while (!stack.empty() && stack[0] == '0') {
        stack.erase(stack.begin());
    }
    
    // If the stack is empty, return "0"
    if (stack.empty()) {
        return "0";
    }
    
    // Return the resulting string
    return stack;
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
- Iterate over the number from left to right and remove digits from the stack if they are greater than the current digit.
- Remove leading zeros from the resulting string.
- Handle the case where the stack is empty after removing digits.