# Largest Number

## Problem Statement
Given a list of non-negative integers, arrange them such that they form the largest possible number. The integers can be concatenated to form a new number. For example, given the list [3, 6, 9], the largest possible number that can be formed is 963. The list can contain duplicate integers and can be empty. The integers are non-negative and can be single-digit or multi-digit.

## Approach
The approach to solve this problem is to use a custom comparator to sort the list of integers. The comparator compares two integers by concatenating them in both orders and checking which one is larger. This ensures that the integers are arranged in the order that forms the largest possible number.

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
        
        // Sort the strings using a custom comparator
        sort(strNums.begin(), strNums.end(), [](const string& a, const string& b) {
            return a + b > b + a;
        });
        
        // Join the sorted strings to form the largest number
        string largestNum;
        for (const string& str : strNums) {
            largestNum += str;
        }
        
        // Remove leading zeros if any
        while (largestNum.size() > 1 && largestNum[0] == '0') {
            largestNum.erase(0, 1);
        }
        
        return largestNum;
    }
};

int main() {
    Solution solution;
    vector<int> nums = {3, 6, 9};
    cout << solution.largestNumber(nums) << endl;
    return 0;
}
```

## Test Cases
```
Input: [3, 6, 9]
Output: 963
Input: [10, 7, 76, 415]
Output: 77641510
Input: [0, 0, 0]
Output: 0
```

## Key Takeaways
- Use a custom comparator to sort the list of integers based on their concatenated values.
- Remove leading zeros from the resulting largest number if any.
- The time complexity of the solution is O(n log n) due to the sorting operation.