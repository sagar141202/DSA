# Next Permutation

## Problem Statement
Given a collection of distinct integers, return all possible next lexicographic permutations. If no such permutation exists, return the last permutation in reverse order. The input array is guaranteed to be non-empty and contain only distinct integers. For example, given the array [1,2,3], the next permutation would be [1,3,2]. If the input array is [3,2,1], the next permutation would be [1,2,3] as it is the first permutation in lexicographic order.

## Approach
The algorithm involves finding the first decreasing element from the right, swapping it with the smallest element greater than it, and then reversing the elements to the right of the swap. This approach ensures that we generate the next lexicographic permutation.

## Complexity
- Time: O(n)
- Space: O(1)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

void nextPermutation(vector<int>& nums) {
    // Find the first decreasing element from the right
    int i = nums.size() - 2;
    while (i >= 0 && nums[i] >= nums[i + 1]) {
        i--;
    }
    
    // If no such element exists, the array is the last permutation
    if (i >= 0) {
        // Find the smallest element greater than nums[i]
        int j = nums.size() - 1;
        while (nums[j] <= nums[i]) {
            j--;
        }
        
        // Swap nums[i] and nums[j]
        swap(nums[i], nums[j]);
    }
    
    // Reverse the elements to the right of the swap
    int left = i + 1;
    int right = nums.size() - 1;
    while (left < right) {
        swap(nums[left], nums[right]);
        left++;
        right--;
    }
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
```

## Key Takeaways
- The algorithm has a time complexity of O(n) due to the potential need to traverse the entire array.
- The space complexity is O(1) as we are modifying the input array in-place.
- The approach involves finding the first decreasing element from the right, swapping it with the smallest element greater than it, and then reversing the elements to the right of the swap.