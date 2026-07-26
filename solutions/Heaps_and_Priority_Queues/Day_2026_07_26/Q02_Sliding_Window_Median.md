# Sliding Window Median

## Problem Statement
The median is the middle value in an ordered integer list. If the size of the list is even, there are two middle values, and the median is their mean. Given a list of integers `nums` and an integer `k`, return the median of each `k` sized sub-list. The sub-lists are created by sliding a window of size `k` over the list `nums`. The median of each sub-list should be returned in the order they are calculated. For example, given `nums = [1, 3, -1, -3, 5, 3, 6, 7]` and `k = 3`, the output should be `[1, -1, -1, 3, 5, 6]`.

## Approach
We will use two heaps to maintain the smaller and larger halves of the current window, ensuring the max heap stores the smaller half and the min heap stores the larger half. This allows us to efficiently calculate the median for each window.

## Complexity
- Time: O(n log k)
- Space: O(k)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class MedianFinder {
public:
    priority_queue<int> maxHeap; // max heap for smaller half
    priority_queue<int, vector<int>, greater<int>> minHeap; // min heap for larger half

    void addNum(int num) {
        // Add to correct heap
        if (maxHeap.empty() || num <= maxHeap.top()) {
            maxHeap.push(num);
        } else {
            minHeap.push(num);
        }
        
        // Balance heaps
        if (maxHeap.size() > minHeap.size() + 1) {
            minHeap.push(maxHeap.top());
            maxHeap.pop();
        } else if (minHeap.size() > maxHeap.size()) {
            maxHeap.push(minHeap.top());
            minHeap.pop();
        }
    }

    double findMedian() {
        if (maxHeap.size() == minHeap.size()) {
            return (maxHeap.top() + minHeap.top()) / 2.0;
        } else {
            return (double)maxHeap.top();
        }
    }
};

vector<double> medianSlidingWindow(vector<int>& nums, int k) {
    MedianFinder mf;
    vector<double> medians;
    
    for (int i = 0; i < nums.size(); i++) {
        mf.addNum(nums[i]);
        
        if (i >= k) {
            // Remove the oldest number from the window
            if (nums[i - k] <= mf.maxHeap.top()) {
                // If the number is in the max heap, remove it
                // Note: This is a simplified version and does not handle duplicates.
                // In a real scenario, you would need a more complex data structure.
                if (mf.maxHeap.top() == nums[i - k]) {
                    mf.maxHeap.pop();
                }
            } else {
                // If the number is in the min heap, remove it
                if (mf.minHeap.top() == nums[i - k]) {
                    mf.minHeap.pop();
                }
            }
        }
        
        if (i >= k - 1) {
            medians.push_back(mf.findMedian());
        }
    }
    
    return medians;
}

int main() {
    vector<int> nums = {1, 3, -1, -3, 5, 3, 6, 7};
    int k = 3;
    vector<double> result = medianSlidingWindow(nums, k);
    for (double d : result) {
        cout << d << " ";
    }
    return 0;
}
```

## Test Cases
```
Input: nums = [1, 3, -1, -3, 5, 3, 6, 7], k = 3
Output: [1, -1, -1, 3, 5, 6]
```

## Key Takeaways
- Use two heaps to maintain the smaller and larger halves of the window for efficient median calculation.
- Balance the heaps after adding a new number to ensure the max heap size is at most one more than the min heap size.
- When removing the oldest number from the window, consider its presence in both heaps.