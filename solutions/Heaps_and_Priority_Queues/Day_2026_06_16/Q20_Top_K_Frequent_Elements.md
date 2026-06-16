# Top K Frequent Elements

## Problem Statement
Given a non-empty array of integers, return the k most frequent elements. The input array will have at least 1 element, but no more than 10^5 elements, with each element in the range [1, 10^5]. The value of k will be in the range [1, number of unique elements in the array]. It is guaranteed that the answer is unique. For example, if the input array is [1,1,1,2,2,3] and k = 2, the output should be [1,2] because 1 appears three times and 2 appears twice.

## Approach
We can use a hash map to store the frequency of each element, then use a priority queue to get the top k frequent elements. The priority queue will store pairs of elements and their frequencies, ordered by frequency. We will then extract the top k elements from the priority queue.

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
        // Create a hash map to store the frequency of each element
        unordered_map<int, int> count;
        for (int num : nums) {
            count[num]++;
        }
        
        // Create a priority queue to store the top k frequent elements
        priority_queue<pair<int, int>> queue;
        for (auto& it : count) {
            queue.push({it.second, it.first});
        }
        
        // Extract the top k elements from the priority queue
        vector<int> result;
        while (k-- > 0) {
            result.push_back(queue.top().second);
            queue.pop();
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
- Use a hash map to store the frequency of each element for efficient lookup and counting.
- Use a priority queue to efficiently extract the top k frequent elements.
- The time complexity is O(N log k) due to the use of the priority queue, where N is the number of unique elements in the input array.