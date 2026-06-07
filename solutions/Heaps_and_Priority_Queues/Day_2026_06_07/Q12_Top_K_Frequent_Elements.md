# Top K Frequent Elements

## Problem Statement
Given a non-empty array of integers, return the k most frequent elements. The output should be in any order, but the input array is guaranteed to have at least k distinct elements. For example, if the input array is [1,1,1,2,2,3] and k = 2, the output should be [1,2] because 1 appears 3 times and 2 appears 2 times. If there are multiple possible outputs, any of them is acceptable.

## Approach
The algorithm uses an unordered_map to store the frequency of each element, then a priority_queue to store the top k frequent elements. The priority_queue is implemented as a max heap where the largest frequency element is at the top. We iterate through the map and push the elements into the priority_queue, then pop the top k elements.

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
        // Create a map to store the frequency of each element
        unordered_map<int, int> freq;
        for (int num : nums) {
            freq[num]++;
        }

        // Create a priority_queue to store the top k frequent elements
        priority_queue<pair<int, int>> pq;
        for (auto& it : freq) {
            pq.push({it.second, it.first});
        }

        // Create a result vector to store the top k frequent elements
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
- Use an unordered_map to store the frequency of each element for efficient lookup.
- Use a priority_queue to store the top k frequent elements and ensure the largest frequency element is at the top.
- The time complexity is O(N log k) due to the use of the priority_queue, where N is the number of elements in the input array.