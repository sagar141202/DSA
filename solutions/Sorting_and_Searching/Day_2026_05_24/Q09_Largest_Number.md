# Largest Number

## Problem Statement
Given a list of non-negative integers, arrange them such that they form the largest possible number. The integers can be concatenated in any order, and each integer can be used only once. For example, if the input is [3, 6, 9], the largest possible number that can be formed is 963. If the input is [10, 7, 76, 415], the largest possible number that can be formed is 77641510. The input list will contain at least one integer and at most 100 integers, each of which is at most 100 digits long.

## Approach
The approach is to sort the numbers as strings in descending order, but with a custom comparison function that compares the concatenation of two numbers in both orders. This ensures that the numbers are ordered based on which concatenation results in a larger number. The sorted numbers can then be concatenated to form the largest possible number.

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
        sort(strNums.begin(), strNums.end(), [](string a, string b) {
            return a + b > b + a;
        });
        
        // If the largest number is 0, return "0"
        if (strNums[0] == "0") {
            return "0";
        }
        
        string result;
        for (string str : strNums) {
            result += str;
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
- The custom comparison function is used to sort the numbers based on their concatenation.
- The result is the concatenation of the sorted numbers.
- If the largest number is 0, the function returns "0" to avoid leading zeros.