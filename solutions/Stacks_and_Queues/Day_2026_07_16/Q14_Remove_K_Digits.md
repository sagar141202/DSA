# Remove K Digits

## Problem Statement
Given a non-negative integer num represented as a string, remove k digits from the number so that the resulting number is the smallest possible. The number may have leading zeros. You must remove exactly k digits. If the result has leading zeros, you should remove them as well. For example, if num = "1432219" and k = 3, the output should be "1219". The constraints are 1 <= num.length <= 10000, and 0 <= k <= num.length.

## Approach
We can solve this problem by using a stack to keep track of the digits. We iterate through the number from left to right and push each digit to the stack. If the stack is not empty and the top of the stack is greater than the current digit, we pop the stack until it's empty or the top of the stack is less than or equal to the current digit. We repeat this process until we have removed k digits.

## Complexity
- Time: O(n)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

string removeKdigits(string num, int k) {
    // Create an empty stack to store the digits
    string stack;
    
    // Iterate through the number from left to right
    for (char c : num) {
        // While the stack is not empty, the top of the stack is greater than the current digit, and k is greater than 0
        while (!stack.empty() && stack.back() > c && k > 0) {
            // Pop the stack
            stack.pop_back();
            // Decrement k
            k--;
        }
        // Push the current digit to the stack
        stack.push_back(c);
    }
    
    // If k is still greater than 0, remove the remaining digits from the end of the stack
    if (k > 0) {
        stack.resize(stack.size() - k);
    }
    
    // Remove leading zeros from the stack
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
- Use a stack to keep track of the digits and remove the larger digits first to get the smallest possible number.
- Remove leading zeros from the resulting number.
- Handle the case where the resulting number is empty (i.e., the input number is "0" and k is 1).