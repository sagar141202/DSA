# Permutations II

## Problem Statement
Given a collection of numbers that might contain duplicates, return all possible unique permutations. The input collection is given as an array of integers. For example, given the array [1,1,2], the function should return [[1,1,2], [1,2,1], [2,1,1]].

## Approach
The approach involves using backtracking to generate all permutations and sorting the input array to handle duplicates. We will use a helper function to recursively generate the permutations and skip duplicates.

## Complexity
- Time: O(N! / (k1! * k2! * ... * km!)) where N is the length of the input array and k1, k2, ..., km are the frequencies of each distinct number
- Space: O(N) for the recursion stack

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
        // skip duplicates
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
    for (auto& vec : result) {
        for (auto& num : vec) {
            cout << num << " ";
        }
        cout << endl;
    }
    return 0;
}
```

## Test Cases
```
Input: [1,1,2]
Output: [[1,1,2], [1,2,1], [2,1,1]]
```

## Key Takeaways
- Use backtracking to generate all permutations of the input array
- Sort the input array to handle duplicates
- Skip duplicates by checking if the current number is the same as the previous one and if the current index is greater than the start index.