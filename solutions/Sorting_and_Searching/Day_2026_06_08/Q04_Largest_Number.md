# Largest Number

## Problem Statement
Given a list of non-negative integers, arrange them such that they form the largest possible number. The integers can be concatenated in any order, and each integer can be used only once. For example, if the input is [3, 30, 34, 5, 9], the largest possible number that can be formed is 9534330. The input list will contain at most 100 integers, and each integer will be between 0 and 10^9.

## Approach
The problem can be solved by using a custom sorting comparator to sort the integers based on their concatenated values. The idea is to compare two integers a and b by concatenating them in both orders (ab and ba) and comparing the results. The integer that produces the larger concatenated value should come first in the sorted order.

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
        // Convert integers to strings
        vector<string> str_nums;
        for (int num : nums) {
            str_nums.push_back(to_string(num));
        }
        
        // Custom sorting comparator
        sort(str_nums.begin(), str_nums.end(), [](string a, string b) {
            return a + b > b + a;
        });
        
        // Handle the case where the largest number is 0
        if (str_nums[0] == "0") {
            return "0";
        }
        
        // Concatenate the sorted strings
        string result;
        for (string str : str_nums) {
            result += str;
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
- The problem requires careful handling of edge cases, such as when the largest number is 0.
- The time complexity of the solution is O(n log n) due to the sorting operation.