# Largest Number

## Problem Statement
Given a list of non-negative integers, arrange them such that they form the largest possible number. The integers can be concatenated in any order to form the largest possible number. For example, given the list [3, 30, 34, 5, 9], the largest possible number that can be formed is 9534330. The numbers can be repeated, but in this case, we are only allowed to use each number once. The goal is to write a function that takes a list of integers as input and returns the largest possible number that can be formed by concatenating the integers.

## Approach
The approach to solve this problem is to use a custom sorting comparator that compares two numbers based on their concatenated values. We sort the list of numbers in descending order using this comparator. The largest possible number is then formed by concatenating the sorted numbers.

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

        // Custom sorting comparator
        sort(strNums.begin(), strNums.end(), [](string a, string b) {
            return a + b > b + a;
        });

        // Concatenate the sorted numbers
        string result;
        for (string str : strNums) {
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
- Custom sorting comparators can be used to solve complex sorting problems.
- Concatenating strings in C++ can be done using the `+` operator.
- Leading zeros can be removed by checking if the first character of the string is '0'.