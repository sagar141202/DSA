# Largest Number

## Problem Statement
Given a list of non-negative integers, arrange them such that they form the largest possible number and return it as a string. The integers can be concatenated in any order, but each integer can only be used once. If the largest possible number is 0, return "0". For example, given the list [3, 30, 34, 5, 9], the largest possible number is "9534330". The list of integers is non-empty and contains at most 100 integers, each of which is at most 100 digits long.

## Approach
The approach is to sort the list of integers based on a custom comparison function that compares two integers a and b by concatenating them in both orders (ab and ba) and checking which one is larger. This ensures that the integers are arranged in the order that forms the largest possible number. The sorted list is then concatenated to form the largest possible number.

## Complexity
- Time: O(n log n)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    string largestNumber(vector<int>& nums) {
        vector<string> strNums;
        for (int num : nums) {
            strNums.push_back(to_string(num));
        }
        
        // Custom comparison function to sort the integers
        sort(strNums.begin(), strNums.end(), [](string a, string b) {
            return a + b > b + a;
        });
        
        // Concatenate the sorted integers to form the largest possible number
        string largestNum;
        for (string str : strNums) {
            largestNum += str;
        }
        
        // If the largest possible number is 0, return "0"
        if (largestNum[0] == '0') {
            return "0";
        }
        
        return largestNum;
    }
};
```

## Test Cases
```
Input: [3, 30, 34, 5, 9]
Output: "9534330"
Input: [10, 7, 76, 415]
Output: "77641510"
Input: [0, 0, 0]
Output: "0"
```

## Key Takeaways
- Custom comparison functions can be used to sort objects based on specific criteria.
- The `sort` function in C++ can be used with custom comparison functions to sort lists of objects.
- When working with strings and numbers, it's essential to consider the concatenation of numbers as strings to achieve the desired result.