# Largest Number

## Problem Statement
Given a list of non-negative integers, arrange them such that they form the largest possible number. The integers can be concatenated in any order, and the resulting number should be the maximum possible. For example, if the input is [3, 30, 34, 5, 9], the output should be "9534330". The numbers can be concatenated in any order, but the resulting number should be the largest possible. The input list will contain at most 100 integers, each of which is at most 10 digits long.

## Approach
The approach is to sort the list of numbers based on a custom comparison function that compares two numbers based on their concatenated values. This comparison function will prioritize the number that results in a larger concatenated value. The sorted list will then be concatenated to form the largest possible number.

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
        
        // Custom comparison function for sorting
        sort(strNums.begin(), strNums.end(), [](const string& a, const string& b) {
            return a + b > b + a;
        });
        
        // Concatenate the sorted list to form the largest possible number
        string result;
        for (const string& str : strNums) {
            result += str;
        }
        
        // Remove leading zeros if any
        if (result[0] == '0') {
            return "0";
        }
        
        return result;
    }
};
```

## Test Cases
```
Input: [3, 30, 34, 5, 9]
Output: "9534330"
Input: [10, 7, 76, 415]
Output: "77641510"
```

## Key Takeaways
- Custom comparison functions can be used to sort objects based on specific criteria.
- The `sort` function in C++ can be used with a custom comparison function to sort a list of objects.
- Leading zeros should be removed from the result if the largest possible number starts with a zero.