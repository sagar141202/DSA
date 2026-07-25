# Remove K Digits

## Problem Statement
Given a non-negative integer num represented as a string, remove k digits from the number so that the resulting number is the smallest possible. The constraints are 1 <= num.length <= 10^5, 1 <= k <= num.length, and num contains only digits. For example, if num = "1432219" and k = 3, the output should be "1219".

## Approach
The algorithm uses a stack to keep track of the digits in the resulting number. It iterates through the input string, pushing digits onto the stack if they are smaller than the top of the stack or if the stack is empty. If the stack is not empty and the top of the stack is greater than the current digit, it pops the top of the stack until it finds a smaller digit or the stack is empty. This process is repeated until k digits have been removed.

## Complexity
- Time: O(n)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

string removeKdigits(string num, int k) {
    // Initialize an empty stack to store the result
    string stack;
    
    // Iterate over each character in the input string
    for (char c : num) {
        // While the stack is not empty, the top of the stack is greater than the current character, and k is greater than 0
        while (k > 0 && !stack.empty() && stack.back() > c) {
            // Remove the top of the stack
            stack.pop_back();
            // Decrement k
            k--;
        }
        // Push the current character onto the stack
        stack.push_back(c);
    }
    
    // If k is still greater than 0, remove the top k elements from the stack
    if (k > 0) {
        stack.resize(stack.size() - k);
    }
    
    // Remove leading zeros from the stack
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
- Use a stack to keep track of the digits in the resulting number.
- Remove digits from the stack that are greater than the current digit to minimize the resulting number.
- Handle edge cases such as leading zeros and an empty stack.