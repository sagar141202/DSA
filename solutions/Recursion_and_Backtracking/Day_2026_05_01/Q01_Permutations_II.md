# Permutations II

## Problem Statement
Given a collection of numbers that might contain duplicates, return all possible unique permutations. The input collection is given as an array of integers, and the output should be a list of lists, where each sublist is a unique permutation of the input array. For example, given the input [1, 1, 2], the output should be [[1, 1, 2], [1, 2, 1], [2, 1, 1]]. The length of the input array will not exceed 10, and the elements will be between 1 and 10.

## Approach
The approach to solve this problem involves using recursion and backtracking to generate all permutations of the input array, while avoiding duplicates by sorting the array and skipping over duplicate elements. This ensures that each permutation is unique, even if the input array contains duplicate elements. The algorithm will explore all possible permutations and store the unique ones.

## Complexity
- Time: O(N! / (k1! * k2! * ... * km!)) where N is the length of the input array, and k1, k2, ..., km are the frequencies of each distinct element in the array.
- Space: O(N) for the recursion stack.

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

void backtrack(vector<int>& nums, int start, vector<vector<int>>& result) {
    if (start == nums.size()) {
        result.push_back(nums);
        return;
    }
    for (int i = start; i < nums.size(); i++) {
        if (i > start && nums[i] == nums[start]) continue;
        swap(nums[start], nums[i]);
        backtrack(nums, start + 1, result);
        swap(nums[start], nums[i]);
    }
}

vector<vector<int>> permuteUnique(vector<int>& nums) {
    vector<vector<int>> result;
    sort(nums.begin(), nums.end());
    backtrack(nums, 0, result);
    return result;
}

int main() {
    vector<int> nums = {1, 1, 2};
    vector<vector<int>> result = permuteUnique(nums);
    for (auto& perm : result) {
        for (int num : perm) {
            cout << num << " ";
        }
        cout << endl;
    }
    return 0;
}
```

## Test Cases
```
Input: [1, 1, 2]
Output: [[1, 1, 2], [1, 2, 1], [2, 1, 1]]
Input: [2, 1, 1]
Output: [[1, 1, 2], [1, 2, 1], [2, 1, 1]]
```

## Key Takeaways
- Use recursion and backtracking to generate all permutations of the input array.
- Sort the input array to group duplicate elements together, and skip over duplicates to avoid generating duplicate permutations.
- Use a swap operation to permute the elements of the input array, and restore the original array after each recursive call to backtrack and explore other permutations.