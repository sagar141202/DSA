# Sliding Window Median

## Problem Statement
Given an array of integers `nums` and an integer `k`, find the median of each subarray of size `k` in `nums`. The median is the middle value in an ordered integer list. If the size of the list is even, the median is the mean of the two middle values. Return a list of the medians for each subarray of size `k`. The constraints are 1 <= k <= nums.size() and nums.size() >= 1.

## Approach
We can use two heaps, a max-heap to store the smaller half of the numbers and a min-heap to store the larger half. The max-heap will store the smaller half of the numbers, and the min-heap will store the larger half. The max-heap will be used to calculate the median when the size of the window is odd, and both heaps will be used when the size of the window is even.

## Complexity
- Time: O(n log k)
- Space: O(k)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<double> medianSlidingWindow(vector<int>& nums, int k) {
        vector<double> medians;
        multiset<int> window;
        
        // Initialize the window
        for (int i = 0; i < k; i++) {
            window.insert(nums[i]);
        }
        
        // Calculate the median for the first window
        medians.push_back(getMedian(window, k));
        
        // Slide the window
        for (int i = k; i < nums.size(); i++) {
            window.erase(window.find(nums[i - k]));
            window.insert(nums[i]);
            medians.push_back(getMedian(window, k));
        }
        
        return medians;
    }
    
    double getMedian(multiset<int>& window, int k) {
        if (k % 2 == 0) {
            auto it1 = window.begin();
            auto it2 = window.begin();
            advance(it1, k / 2 - 1);
            advance(it2, k / 2);
            return (*it1 + *it2) / 2.0;
        } else {
            auto it = window.begin();
            advance(it, k / 2);
            return *it;
        }
    }
};

```

## Test Cases
```
Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [1,-1,-1,3,5,6]
```

## Key Takeaways
- Use a multiset to maintain the window of elements.
- Calculate the median for each window based on whether the window size is odd or even.
- Use iterators to access the elements in the multiset for calculating the median.