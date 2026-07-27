# Remove K Digits

## Problem Statement
Given a non-negative integer num represented as a string, remove k digits from the number so that the resulting number is the smallest possible. The constraints are 1 <= k <= num.length <= 10000, and num does not contain any leading zero. For example, if num = "1432219" and k = 3, the output should be "1219". If num = "10200" and k = 1, the output should be "2000" which is then reduced to "200" by removing the leading zeros, and then further reduced to "20" and finally to "2" if k was larger.

## Approach
The algorithm uses a stack to keep track of the digits. It iterates over the string, pushing digits onto the stack if the stack is empty or the top of the stack is less than or equal to the current digit. If the top of the stack is greater than the current digit, it pops the stack until it is empty or the top of the stack is less than or equal to the current digit, or until k becomes 0. This ensures that the resulting number is the smallest possible.

## Complexity
- Time: O(n)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

string removeKdigits(string num, int k) {
    // Create an empty stack
    string stack;
    
    // Iterate over each character in the string
    for (char c : num) {
        // While the stack is not empty, the top of the stack is greater than the current character, and k is greater than 0
        while (!stack.empty() && stack.back() > c && k > 0) {
            // Pop the stack
            stack.pop_back();
            // Decrement k
            k--;
        }
        // Push the current character onto the stack
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
- Use a stack to keep track of the digits in the number.
- Remove digits from the stack that are greater than the current digit to minimize the resulting number.
- Handle the case where the resulting number is zero.