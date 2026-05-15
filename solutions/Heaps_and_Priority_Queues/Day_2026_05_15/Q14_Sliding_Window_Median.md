# Sliding Window Median

## Problem Statement
The Sliding Window Median problem involves finding the median of all numbers in a sliding window of size `k` within an array of integers. The array is given as `nums`, and the window size `k` is also provided. The task is to calculate the median for each window position, where the window can slide one element at a time from left to right. The median of a window is the middle value in the sorted window. If the window has an even number of elements, the median is the average of the two middle values. The goal is to return a list of medians for all window positions.

## Approach
To solve this problem, we utilize two heaps: a max heap to store the smaller half of the window and a min heap to store the larger half. We maintain the balance between the two heaps, ensuring the max heap has at most one more element than the min heap. This allows for efficient calculation of the median.

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
        // Max heap to store the smaller half of the window
        priority_queue<int> maxHeap;
        // Min heap to store the larger half of the window
        priority_queue<int, vector<int>, greater<int>> minHeap;
        
        // Initialize the window
        for (int i = 0; i < k; i++) {
            // Add elements to the heaps
            addNum(maxHeap, minHeap, nums[i]);
        }
        
        // Calculate the median for the first window
        medians.push_back(getMedian(maxHeap, minHeap));
        
        // Slide the window
        for (int i = k; i < nums.size(); i++) {
            // Remove the leftmost element from the window
            removeNum(maxHeap, minHeap, nums[i - k]);
            // Add the new element to the window
            addNum(maxHeap, minHeap, nums[i]);
            // Calculate the median for the current window
            medians.push_back(getMedian(maxHeap, minHeap));
        }
        
        return medians;
    }
    
    // Helper function to add a number to the heaps
    void addNum(priority_queue<int>& maxHeap, priority_queue<int, vector<int>, greater<int>>& minHeap, int num) {
        if (maxHeap.empty() || num <= maxHeap.top()) {
            maxHeap.push(num);
        } else {
            minHeap.push(num);
        }
        
        // Balance the heaps
        if (maxHeap.size() > minHeap.size() + 1) {
            minHeap.push(maxHeap.top());
            maxHeap.pop();
        } else if (minHeap.size() > maxHeap.size()) {
            maxHeap.push(minHeap.top());
            minHeap.pop();
        }
    }
    
    // Helper function to remove a number from the heaps
    void removeNum(priority_queue<int>& maxHeap, priority_queue<int, vector<int>, greater<int>>& minHeap, int num) {
        if (num <= maxHeap.top()) {
            // Remove from max heap
            priority_queue<int> newMaxHeap;
            while (!maxHeap.empty() && maxHeap.top() != num) {
                newMaxHeap.push(maxHeap.top());
                maxHeap.pop();
            }
            if (!maxHeap.empty()) {
                maxHeap.pop();
            }
            maxHeap = newMaxHeap;
        } else {
            // Remove from min heap
            priority_queue<int, vector<int>, greater<int>> newMinHeap;
            while (!minHeap.empty() && minHeap.top() != num) {
                newMinHeap.push(minHeap.top());
                minHeap.pop();
            }
            if (!minHeap.empty()) {
                minHeap.pop();
            }
            minHeap = newMinHeap;
        }
        
        // Balance the heaps
        if (maxHeap.size() > minHeap.size() + 1) {
            minHeap.push(maxHeap.top());
            maxHeap.pop();
        } else if (minHeap.size() > maxHeap.size()) {
            maxHeap.push(minHeap.top());
            minHeap.pop();
        }
    }
    
    // Helper function to get the median
    double getMedian(priority_queue<int>& maxHeap, priority_queue<int, vector<int>, greater<int>>& minHeap) {
        if (maxHeap.size() == minHeap.size()) {
            return (double)(maxHeap.top() + minHeap.top()) / 2;
        } else {
            return (double)maxHeap.top();
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
- The use of two heaps (max heap and min heap) allows for efficient maintenance of the window's median.
- The balance between the two heaps is crucial for correctly calculating the median.
- The time complexity of O(n log k) is due to the heap operations, where n is the size of the input array and k is the window size.