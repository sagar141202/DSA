# Largest Number

## Problem Statement
Given a list of non-negative integers, arrange them such that they form the largest possible number. The integers can be concatenated in any order, but each integer can only be used once. For example, given the integers [3, 6, 9], the largest possible number is 963. If the input is [10, 7, 76, 415], the largest possible number is 77641510. The input list will contain at least one integer and at most 100 integers, each of which is at most 10^9.

## Approach
The problem can be solved by using a custom comparator to sort the list of integers. The comparator compares two integers based on their concatenated values. The integers are sorted in descending order based on this comparator. The sorted list is then concatenated to form the largest possible number.

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
        
        sort(strNums.begin(), strNums.end(), [](const string& a, const string& b) {
            return a + b > b + a;
        });
        
        string result;
        for (const string& str : strNums) {
            result += str;
        }
        
        // Remove leading zeros if any
        while (result.length() > 1 && result[0] == '0') {
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
Input: [0, 0, 0]
Output: "0"
```

## Key Takeaways
- Custom comparator can be used to solve this problem.
- Sorting the list of integers based on their concatenated values gives the desired result.
- Leading zeros need to be removed from the final result if any.