# Top K Frequent Elements

## Problem Statement
Given an integer array `nums` and an integer `k`, return the top `k` frequent elements in the array. The output should be in any order. The input array will contain at least `k` distinct elements. For example, if `nums = [1,1,1,2,2,3]` and `k = 2`, the output should be `[1,2]` because `1` appears three times and `2` appears two times.

## Approach
The approach is to use an unordered map to store the frequency of each element, then use a priority queue to store the top k frequent elements. We will iterate over the map and push the elements into the priority queue based on their frequencies.

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
        // Store the frequency of each element
        unordered_map<int, int> frequency;
        for (int num : nums) {
            frequency[num]++;
        }

        // Use a priority queue to store the top k frequent elements
        priority_queue<pair<int, int>> maxHeap;
        for (auto& pair : frequency) {
            maxHeap.push({pair.second, pair.first});
        }

        // Get the top k frequent elements
        vector<int> result;
        while (k-- > 0) {
            result.push_back(maxHeap.top().second);
            maxHeap.pop();
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
- Use an unordered map to efficiently store the frequency of each element.
- Utilize a priority queue to easily retrieve the top k frequent elements.
- The time complexity is dominated by the priority queue operations, resulting in O(N log k) time complexity.