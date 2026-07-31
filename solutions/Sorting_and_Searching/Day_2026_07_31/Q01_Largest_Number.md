# Largest Number

## Problem Statement
Given a list of non-negative integers, arrange them such that they form the largest possible number. The integers can be concatenated in any order, and each integer can only be used once. For example, given the list [3, 30, 34, 5, 9], the largest possible number that can be formed is 9534330. The list can contain up to 100 integers, and each integer can have up to 10 digits. If the list is empty, return an empty string.

## Approach
The problem can be solved by using a custom comparator to sort the list of integers. The comparator compares two integers based on their concatenated values. If the concatenated value of the first integer with the second integer is greater than the concatenated value of the second integer with the first integer, then the first integer should come before the second integer in the sorted list.

## Complexity
- Time: O(N log N)
- Space: O(N)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    string largestNumber(vector<int>& nums) {
        // Convert integers to strings
        vector<string> strNums;
        for (int num : nums) {
            strNums.push_back(to_string(num));
        }

        // Sort the list using a custom comparator
        sort(strNums.begin(), strNums.end(), [](string a, string b) {
            return a + b > b + a;
        });

        // Concatenate the sorted list
        string result;
        for (string str : strNums) {
            result += str;
        }

        // Remove leading zeros
        while (result.size() > 1 && result[0] == '0') {
            result.erase(0, 1);
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
Input: [0, 0, 0]
Output: "0"
```

## Key Takeaways
- The problem requires a custom comparator to sort the list of integers based on their concatenated values.
- The solution involves sorting the list and then concatenating the sorted list to form the largest possible number.
- The solution also involves removing leading zeros from the result to handle cases where the list contains only zeros.