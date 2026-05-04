# Largest Number

## Problem Statement
Given a list of non-negative integers, arrange them such that they form the largest possible number. The integers can be concatenated in any order, and the result should be the maximum possible number that can be formed. For example, if the input is [3, 30, 34, 5, 9], the output should be "9534330". The numbers can be concatenated in any order, but the resulting number should be the largest possible.

## Approach
The approach is to sort the numbers based on a custom comparator that compares two numbers based on their concatenated values. The sorting is done in descending order, and the resulting sorted list is then concatenated to form the largest possible number.

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
        
        // Custom comparator for sorting
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
Output: "9534330"
Input: [10, 7, 76, 415]
Output: "77641510"
```

## Key Takeaways
- Custom comparator is used for sorting the numbers based on their concatenated values.
- The sorting is done in descending order to get the largest possible number.
- Leading zeros are removed from the result if any.