# Largest Number

## Problem Statement
Given a list of non-negative integers, arrange them such that they form the largest possible number. The integers can be concatenated to form a single number. For example, if the input is [3, 6, 9], the output should be 963. The integers are between 0 and 9, and there can be duplicate integers. The goal is to find the largest possible number that can be formed by arranging these integers.

## Approach
The approach is to sort the integers based on a custom comparison function that compares two numbers as if they were concatenated. This function checks which concatenation is larger, either the first number concatenated with the second or the second concatenated with the first.

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
        
        string result = "";
        for (const string& str : strNums) {
            result += str;
        }
        
        // Handle the case where the input is [0, 0, 0]
        if (result[0] == '0') {
            return "0";
        }
        
        return result;
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
```

## Key Takeaways
- Custom sorting is used to compare numbers based on their concatenated values.
- The solution handles the case where the input contains only zeros.
- The time complexity is O(n log n) due to the sorting operation.