# Next Permutation

## Problem Statement
Given a list of integers, find the next lexicographically greater permutation of the list. If no greater permutation exists, the function should return the first permutation (i.e., the sorted list). For example, if the input is [1, 2, 3], the next permutation would be [1, 3, 2]. If the input is [3, 2, 1], the function should return [1, 2, 3] as it is the first permutation.

## Approach
The algorithm finds the largest index k such that the current element is less than the next one, then finds the largest index l > k such that the current element at index k is less than the element at index l, and swaps them. Finally, it reverses the sequence from index k + 1 to the end.

## Complexity
- Time: O(n)
- Space: O(1)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

void nextPermutation(vector<int>& nums) {
    int i = nums.size() - 2;
    // Find the largest index k such that the current element is less than the next one
    while (i >= 0 && nums[i] >= nums[i + 1]) {
        i--;
    }
    
    if (i >= 0) {
        int j = nums.size() - 1;
        // Find the largest index l > k such that the current element at index k is less than the element at index l
        while (nums[j] <= nums[i]) {
            j--;
        }
        // Swap the elements at indices i and j
        swap(nums[i], nums[j]);
    }
    // Reverse the sequence from index i + 1 to the end
    reverse(nums.begin() + i + 1, nums.end());
}

int main() {
    vector<int> nums = {1, 2, 3};
    nextPermutation(nums);
    for (int num : nums) {
        cout << num << " ";
    }
    return 0;
}
```

## Test Cases
```
Input: [1, 2, 3]
Output: [1, 3, 2]
Input: [3, 2, 1]
Output: [1, 2, 3]
Input: [1, 1, 5]
Output: [1, 5, 1]
```

## Key Takeaways
- Find the largest index k such that the current element is less than the next one.
- Find the largest index l > k such that the current element at index k is less than the element at index l.
- Reverse the sequence from index k + 1 to the end to get the smallest permutation that is greater than the current one.