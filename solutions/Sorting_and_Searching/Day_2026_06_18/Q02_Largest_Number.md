# Largest Number

## Problem Statement
Given a list of non-negative integers, arrange them such that they form the largest possible number. The integers can be concatenated together to form a single number. For example, if the input is [3, 6, 9], the largest possible number that can be formed is 963. The input list can contain up to 100 integers, each of which can be up to 10 digits long. The goal is to write a function that takes this list as input and returns the largest possible number as a string.

## Approach
The approach is to sort the input list in descending order based on a custom comparison function. This function compares two numbers by concatenating them in both orders and checking which one is larger. The sorted list is then concatenated together to form the largest possible number.

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
        
        // Sort the strings based on a custom comparison function
        sort(strNums.begin(), strNums.end(), [](string a, string b) {
            return a + b > b + a;
        });
        
        // Concatenate the sorted strings together
        string result;
        for (string str : strNums) {
            result += str;
        }
        
        // Remove leading zeros if any
        while (result.size() > 1 && result[0] == '0') {
            result.erase(0, 1);
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
Output: "963"
Input: [10, 7, 76, 415]
Output: "77641510"
```

## Key Takeaways
- Custom sorting is necessary to arrange the numbers in the correct order.
- Concatenating the sorted numbers together forms the largest possible number.
- Leading zeros need to be removed from the result if any.