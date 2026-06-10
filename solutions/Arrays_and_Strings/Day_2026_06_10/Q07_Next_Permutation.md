# Next Permutation

## Problem Statement
Given an array of integers, find the next permutation of the array in lexicographic order. If the array is the last permutation, return the first permutation. For example, given the array [1, 2, 3], the next permutation is [1, 3, 2]. The array is 1-indexed, and the elements are distinct. The length of the array is between 1 and 100.

## Approach
The algorithm starts from the end of the array and finds the first pair of elements that are in decreasing order. Then, it swaps the first element with the smallest element greater than it. Finally, it reverses the elements after the first element.

## Complexity
- Time: O(n)
- Space: O(1)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

void nextPermutation(vector<int>& nums) {
    // find the first pair of elements in decreasing order from the end
    int i = nums.size() - 2;
    while (i >= 0 && nums[i] >= nums[i + 1]) {
        i--;
    }

    // if the array is the last permutation, return the first permutation
    if (i >= 0) {
        int j = nums.size() - 1;
        while (nums[j] <= nums[i]) {
            j--;
        }
        // swap the first element with the smallest element greater than it
        swap(nums[i], nums[j]);
    }

    // reverse the elements after the first element
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
Input: [1, 1, 5]
Output: [1, 5, 1]
```

## Key Takeaways
- The next permutation of an array can be found by swapping the first element that is smaller than the next element with the smallest element greater than it.
- If the array is the last permutation, the function returns the first permutation by reversing the array.
- The time complexity of the algorithm is O(n), where n is the length of the array.