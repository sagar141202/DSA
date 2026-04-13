# Single Number

## Problem Statement
Given a non-empty array of integers, every element appears twice except for one. Find that single one. The input array will have at least one element and a maximum of 1000 elements, with values ranging from 0 to 10^4. For example, if the input array is [2,2,1], the function should return 1, because 1 appears only once in the array.

## Approach
We can use the XOR operation to find the single number, as XOR of a number with itself is 0, and XOR of a number with 0 is the number itself. This property allows us to eliminate the numbers that appear twice in the array.

## Complexity
- Time: O(n)
- Space: O(1)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int singleNumber(vector<int>& nums) {
        int result = 0;
        // Iterate over each number in the array and XOR it with the result
        for (int num : nums) {
            result ^= num;
        }
        return result;
    }
};
```

## Test Cases
```
Input: [2,2,1]
Output: 1
Input: [4,1,2,1,2]
Output: 4
```

## Key Takeaways
- The XOR operation can be used to find the single number in an array where every element appears twice except for one.
- The XOR operation has a time complexity of O(n) and a space complexity of O(1), making it an efficient solution for this problem.
- The XOR operation can also be used to solve other problems that involve finding a single element in an array, such as finding the single number in an array where every element appears three times except for one.