# Largest Number

## Problem Statement
Given a list of non-negative integers, arrange them such that they form the largest possible number. The integers can be concatenated in any order, but each integer can only be used once. For example, given the integers [3, 30, 34, 5, 9], the largest possible number that can be formed is 9534330. The input list will contain at most 100 integers, and each integer will be between 0 and 10^9.

## Approach
The approach to solve this problem is to use a custom sorting comparator that compares two numbers based on their concatenated values. This way, the numbers that produce the largest concatenated values will come first in the sorted list. The sorted list can then be concatenated to form the largest possible number.

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
        
        // Concatenate sorted strings
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

int main() {
    Solution solution;
    vector<int> nums = {3, 30, 34, 5, 9};
    cout << solution.largestNumber(nums) << endl;
    return 0;
}
```

## Test Cases
```
Input: [3, 30, 34, 5, 9]
Output: 9534330
Input: [10, 7, 76, 415]
Output: 77641510
```

## Key Takeaways
- Custom sorting comparator can be used to sort numbers based on their concatenated values.
- The sorted list can be concatenated to form the largest possible number.
- Leading zeros should be removed from the result if any.