# Top K Frequent Elements

## Problem Statement
Given an integer array `nums` and an integer `k`, return the top `k` frequent elements in the array. The output should be sorted in descending order of frequency, and if two elements have the same frequency, they should be sorted in ascending order. For example, given `nums = [1,1,1,2,2,3]` and `k = 2`, the output should be `[1,2]`. The array `nums` can contain duplicate elements and the range of `k` is `1 <= k <= nums.size()`.

## Approach
The algorithm uses an unordered map to count the frequency of each element, then a priority queue to store the top k frequent elements. The priority queue is sorted based on the frequency of elements and their values.

## Complexity
- Time: O(N log k)
- Space: O(N)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        // Count the frequency of each element
        unordered_map<int, int> freq;
        for (int num : nums) {
            freq[num]++;
        }

        // Use a priority queue to store the top k frequent elements
        priority_queue<pair<int, int>> pq;
        for (auto& it : freq) {
            pq.push({it.second, it.first});
        }

        // Get the top k frequent elements
        vector<int> result;
        while (k-- > 0) {
            result.push_back(pq.top().second);
            pq.pop();
        }

        return result;
    }
};
```

## Test Cases
```
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Input: nums = [1], k = 1
Output: [1]
```

## Key Takeaways
- Use an unordered map to efficiently count the frequency of each element.
- Utilize a priority queue to store the top k frequent elements, sorted by frequency and value.
- The time complexity is dominated by the priority queue operations, resulting in O(N log k) time complexity.