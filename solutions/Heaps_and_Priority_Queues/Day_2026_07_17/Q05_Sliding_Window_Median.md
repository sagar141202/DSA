# Sliding Window Median

## Problem Statement
The Sliding Window Median problem involves finding the median of all numbers in a sliding window of size `k` in an array of integers. The array is given as `nums`, and the window size is given as `k`. The median is the middle value in the sorted array. If the window size is even, the median is the average of the two middle values. The goal is to find the median for each window position and return a vector of these medians.

## Approach
The algorithm uses two heaps, a max heap to store the smaller half of the window and a min heap to store the larger half. It maintains the balance between the two heaps by ensuring the max heap always has one more element than the min heap when the window size is odd.

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
        
        // Initialize the window with the first k elements
        for (int i = 0; i < k; i++) {
            window.insert(nums[i]);
        }
        
        // Calculate the median for the first window
        medians.push_back(getMedian(window, k));
        
        // Slide the window and calculate the median for each position
        for (int i = k; i < nums.size(); i++) {
            window.erase(window.find(nums[i - k]));
            window.insert(nums[i]);
            medians.push_back(getMedian(window, k));
        }
        
        return medians;
    }
    
    double getMedian(multiset<int>& window, int k) {
        if (k % 2 == 0) {
            // If the window size is even, return the average of the two middle values
            auto mid1 = next(window.begin(), k / 2 - 1);
            auto mid2 = next(window.begin(), k / 2);
            return (*mid1 + *mid2) / 2.0;
        } else {
            // If the window size is odd, return the middle value
            auto mid = next(window.begin(), k / 2);
            return *mid;
        }
    }
};

```

## Test Cases
```
Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [1.0,-1.0,-1.0,3.0,5.0,6.0]
```

## Key Takeaways
- Use a balanced binary search tree (like multiset in C++) or two heaps to maintain the window elements in sorted order.
- Calculate the median based on whether the window size is even or odd.
- Slide the window by removing the oldest element and adding the newest element, then recalculate the median.