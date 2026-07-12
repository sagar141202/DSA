# Largest Number

## Problem Statement
Given a list of non-negative integers, arrange them such that they form the largest possible number. The integers can be concatenated together in any order. For example, given the list [3, 6, 9], the largest possible number that can be formed is 963. The list can contain duplicate integers and can be empty. If the list is empty, return "0". If the list contains only zeros, return "0".

## Approach
The algorithm involves sorting the list of integers based on a custom comparator that compares the concatenation of two numbers in both orders. This ensures that the numbers are arranged in a way that maximizes the value of the resulting number. The sorted list is then concatenated together to form the largest possible number.

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
        // Convert integers to strings for easy concatenation
        vector<string> strNums;
        for (int num : nums) {
            strNums.push_back(to_string(num));
        }
        
        // Sort the list based on a custom comparator
        sort(strNums.begin(), strNums.end(), [](const string& a, const string& b) {
            return a + b > b + a;
        });
        
        // Concatenate the sorted list to form the largest possible number
        string result;
        for (const string& str : strNums) {
            result += str;
        }
        
        // If the result starts with '0', return "0"
        if (result[0] == '0') {
            return "0";
        }
        
        return result;
    }
};
```

## Test Cases
```
Input: [3, 6, 9]
Output: "963"
Input: [10, 7, 76, 415]
Output: "77641510"
Input: [0, 0, 0]
Output: "0"
```

## Key Takeaways
- Custom comparators can be used to sort lists based on complex conditions.
- Concatenating strings in C++ can be done using the `+` operator.
- It's essential to handle edge cases, such as lists containing only zeros.