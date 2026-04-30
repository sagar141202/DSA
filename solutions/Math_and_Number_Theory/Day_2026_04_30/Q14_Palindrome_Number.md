# Palindrome Number

## Problem Statement
Given a non-negative integer, determine if it is a palindrome number. A palindrome number is a number that remains the same when its digits are reversed. For example, 121 is a palindrome number, but 123 is not. The input integer will be in the range [0, 2^31 - 1]. The function should return true if the number is a palindrome and false otherwise.

## Approach
We can solve this problem by converting the integer to a string and then comparing the string with its reverse. Alternatively, we can also solve this problem mathematically by reversing the number and comparing it with the original number.

## Complexity
- Time: O(log(n))
- Space: O(log(n))

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    bool isPalindrome(int x) {
        // if x is negative, it's not a palindrome
        if (x < 0) return false;
        
        // convert x to string
        string str = to_string(x);
        
        // initialize two pointers
        int left = 0, right = str.size() - 1;
        
        // compare characters from both ends
        while (left < right) {
            if (str[left] != str[right]) return false;
            left++, right--;
        }
        
        return true;
    }
};
```

## Test Cases
```
Input: 121
Output: true
Input: 123
Output: false
```

## Key Takeaways
- A palindrome number remains the same when its digits are reversed.
- We can solve this problem by converting the integer to a string and comparing it with its reverse, or by reversing the number mathematically.
- The time complexity of this solution is O(log(n)) because we are converting the integer to a string, and the space complexity is also O(log(n)) because we are storing the string.