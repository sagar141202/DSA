# Remove K Digits

## Problem Statement
Given a non-negative integer num represented as a string, remove k digits from the number so that the resulting number is the smallest possible. The constraints are: 1 <= k <= num.length <= 10000, and num does not contain any leading zeros except for the number zero itself. For example, if num = "1432219" and k = 3, the output should be "1219". If num = "10200" and k = 1, the output should be "2000" but since we want to keep the number as small as possible and remove leading zeros, the output will be "2000" -> "2" is not the answer because the number is not the smallest, the answer is "2000" after removing '1' and then '0' is removed as it is a leading zero, so "200" -> "20" -> "2" is the process but we write "2000" and then remove '1' to get "2000" and it is already the smallest after removing '1', so the output will be "2000" after removing '1', not "2" because the leading zeros are removed after the removal process, not during. The goal is to find the smallest number possible after removing k digits.

## Approach
We use a stack data structure to keep track of the digits. We iterate through the number and push each digit to the stack. If the stack is not empty and the current digit is smaller than the top of the stack, we pop the stack until it is empty or the top of the stack is smaller than the current digit, or we have removed k digits. This ensures that the resulting number is the smallest possible.

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
    
    // Iterate through each character in the string
    for (char c : num) {
        // While the stack is not empty, the top of the stack is greater than the current character, and k is greater than 0
        while (k > 0 && !stack.empty() && stack.back() > c) {
            // Pop the top of the stack
            stack.pop_back();
            // Decrement k
            k--;
        }
        // Push the current character to the stack
        stack.push_back(c);
    }
    
    // If k is still greater than 0, remove the last k characters from the stack
    if (k > 0) {
        stack.erase(stack.size() - k);
    }
    
    // Find the first non-zero character in the stack
    int start = 0;
    while (start < stack.size() && stack[start] == '0') {
        start++;
    }
    
    // Return the result
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
- Use a stack to keep track of the digits and remove the larger digits first.
- Remove leading zeros after the removal process.
- Handle edge cases where the result is zero or the input number is already the smallest possible.