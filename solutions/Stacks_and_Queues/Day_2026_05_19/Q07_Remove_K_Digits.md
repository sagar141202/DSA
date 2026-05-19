# Remove K Digits

## Problem Statement
Given a non-negative integer `num` represented as a string, remove `k` digits from `num` such that the resulting string is the smallest possible integer. You can assume that `num` does not contain any leading zeros. The integer does not contain leading zeros and `k` is within the range [0, num.length - 1]. For example, if `num = "1432219"` and `k = 3`, the output should be `"1219"`.

## Approach
We will use a stack-based approach to solve this problem, iterating through the string and pushing characters to the stack if they are smaller than the top of the stack or if the stack is empty. If the stack is not empty and the top of the stack is greater than the current character, we will pop from the stack until it is empty or the top of the stack is smaller than the current character.

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
    
    // Iterate through the string
    for (char c : num) {
        // While the stack is not empty and the top of the stack is greater than the current character
        // and k is greater than 0, pop from the stack and decrement k
        while (k > 0 && !stack.empty() && stack.back() > c) {
            stack.pop_back();
            k--;
        }
        // Push the current character to the stack
        stack.push_back(c);
    }
    
    // If k is still greater than 0, remove the last k characters from the stack
    if (k > 0) {
        stack.erase(stack.size() - k);
    }
    
    // Remove leading zeros from the stack
    while (stack.size() > 1 && stack[0] == '0') {
        stack.erase(stack.begin());
    }
    
    // Return the resulting string
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
- Use a stack-based approach to remove k digits from a string to get the smallest possible integer.
- Iterate through the string and push characters to the stack if they are smaller than the top of the stack or if the stack is empty.
- Remove leading zeros from the resulting string to get the final answer.