# Missing Number
## Problem Statement
Given an array of integers from 0 to n, where n is the length of the array, find the missing number in the array. The array contains all integers from 0 to n except one. For example, given the array [0, 1, 3], the missing number is 2. The array can contain duplicate elements and the missing number can be any integer from 0 to n.

## Approach
The approach to solve this problem is to use bitwise XOR operation to find the missing number. We XOR all the numbers in the array with all the numbers from 0 to n. The XOR of all numbers from 0 to n will give us the missing number.

## Complexity
- Time: O(n)
- Space: O(1)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int missingNumber(vector<int>& nums) {
        int n = nums.size();
        int result = n;
        for (int i = 0; i < n; i++) {
            // XOR all numbers in the array with all numbers from 0 to n
            result = result ^ i ^ nums[i];
        }
        return result;
    }
};

int main() {
    Solution solution;
    vector<int> nums = {0, 1, 3};
    cout << solution.missingNumber(nums) << endl;  // Output: 2
    return 0;
}
```

## Test Cases
```
Input: [0, 1, 3]
Output: 2
Input: [4, 0, 3, 1]
Output: 2
```

## Key Takeaways
- The XOR operation has the property that a ^ a = 0 and a ^ 0 = a, which makes it useful for finding the missing number.
- The XOR operation is associative and commutative, which means that the order of the operations does not matter.
- This solution has a time complexity of O(n) and a space complexity of O(1), making it efficient for large inputs.