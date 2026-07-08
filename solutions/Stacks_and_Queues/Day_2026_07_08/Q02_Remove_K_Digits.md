# Remove K Digits

## Problem Statement
Given a non-negative integer num represented as a string, remove k digits from the number so that the remaining digits form the smallest possible number. The number may have leading zeros after removing the digits. You must remove exactly k digits. Note that the input number may have up to 100,000 digits. For example, if num = "1432219" and k = 3, the output should be "1219". If num = "10200" and k = 1, the output should be "2000" but since we want the smallest number, "0200" is not allowed, the correct answer is "2000" after removing the leading zeros.

## Approach
The algorithm uses a stack to keep track of the digits. It iterates over the string, pushing digits onto the stack if the stack is empty or the top of the stack is less than or equal to the current digit. If the stack is not empty and the top of the stack is greater than the current digit, it pops the stack until it is empty or the top of the stack is less than or equal to the current digit, or until it has removed k digits. This process ensures that the remaining digits form the smallest possible number.

## Complexity
- Time: O(n)
- Space: O(n)

## C++ Solution
```cpp
class Solution {
public:
    string removeKdigits(string num, int k) {
        // Initialize an empty stack
        string stack;
        
        // Iterate over each character in the string
        for (char c : num) {
            // While the stack is not empty, the top of the stack is greater than the current character, and k is greater than 0
            while (k > 0 && !stack.empty() && stack.back() > c) {
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
            stack.resize(stack.size() - k);
        }
        
        // Find the first non-zero character in the stack
        int start = 0;
        while (start < stack.size() && stack[start] == '0') {
            start++;
        }
        
        // Return the stack as a string, starting from the first non-zero character
        return start == stack.size() ? "0" : stack.substr(start);
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
- Use a stack to keep track of the digits and remove k digits to form the smallest possible number.
- Iterate over the string and push digits onto the stack if the stack is empty or the top of the stack is less than or equal to the current digit.
- Remove the last k characters from the stack if k is still greater than 0 after iterating over the string.