# Largest Number

## Problem Statement
Given a list of non-negative integers, arrange them such that they form the largest possible number. The integers can be concatenated to form a new number. For example, given the list [3, 6, 9], the largest possible number is 963. The list can contain duplicate numbers and the numbers can be zero. The goal is to find the largest possible number that can be formed by concatenating the numbers in the list.

## Approach
The approach is to sort the list of numbers based on a custom comparator that compares two numbers based on their concatenated values. This ensures that the numbers are arranged in a way that forms the largest possible number. The sorted list is then concatenated to form the largest possible number.

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
        // Convert the numbers to strings for easy concatenation
        vector<string> strNums;
        for (int num : nums) {
            strNums.push_back(to_string(num));
        }

        // Sort the numbers based on a custom comparator
        sort(strNums.begin(), strNums.end(), [](const string& a, const string& b) {
            return a + b > b + a;
        });

        // Concatenate the sorted numbers to form the largest possible number
        string result;
        for (const string& str : strNums) {
            result += str;
        }

        // Remove leading zeros if any
        while (result.size() > 1 && result[0] == '0') {
            result.erase(0, 1);
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
```

## Key Takeaways
- The custom comparator is used to compare two numbers based on their concatenated values.
- The numbers are sorted in descending order based on the custom comparator.
- The sorted numbers are concatenated to form the largest possible number.