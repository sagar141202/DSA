# Sliding Window Median

## Problem Statement
The Sliding Window Median problem involves finding the median of all numbers in a sliding window of size `k` within an array of integers. The array is given as `nums`, and the size of the sliding window is `k`. The median is the middle value in an ordered integer list. If the size of the list is even, the median is the mean of the two middle values. For example, given `nums = [1, 3, -1, -3, 5, 3, 6, 7]` and `k = 3`, the output should be `[1, -1, -1, 3, 5, 6]`, which are the medians of the sliding windows of size `3`.

## Approach
We use two heaps, a max heap to store the smaller half of the numbers and a min heap to store the larger half. We maintain the property that the max heap always has one more element than the min heap if the total number of elements is odd. The median is then the top element of the max heap.

## Complexity
- Time: O(n log k)
- Space: O(k)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class MedianFinder {
public:
    // max heap to store the smaller half
    priority_queue<int> maxHeap;
    // min heap to store the larger half
    priority_queue<int, vector<int>, greater<int>> minHeap;

    void addNum(int num) {
        // add the number to the correct heap
        if (maxHeap.empty() || num <= maxHeap.top()) {
            maxHeap.push(num);
        } else {
            minHeap.push(num);
        }
        
        // balance the heaps
        if (maxHeap.size() > minHeap.size() + 1) {
            minHeap.push(maxHeap.top());
            maxHeap.pop();
        } else if (minHeap.size() > maxHeap.size()) {
            maxHeap.push(minHeap.top());
            minHeap.pop();
        }
    }

    double findMedian() {
        // calculate the median
        if (maxHeap.size() == minHeap.size()) {
            return (maxHeap.top() + minHeap.top()) / 2.0;
        } else {
            return (double)maxHeap.top();
        }
    }

    vector<double> medianSlidingWindow(vector<int>& nums, int k) {
        vector<double> medians;
        for (int i = 0; i < nums.size(); i++) {
            addNum(nums[i]);
            if (i >= k) {
                // remove the number that is out of the window
                if (nums[i - k] <= maxHeap.top()) {
                    // remove from max heap
                    maxHeap.pop();
                } else {
                    // remove from min heap
                    minHeap.pop();
                }
            }
            if (i >= k - 1) {
                medians.push_back(findMedian());
            }
        }
        return medians;
    }
};

int main() {
    MedianFinder mf;
    vector<int> nums = {1, 3, -1, -3, 5, 3, 6, 7};
    int k = 3;
    vector<double> medians = mf.medianSlidingWindow(nums, k);
    for (double m : medians) {
        cout << m << " ";
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
- Using two heaps to maintain the sliding window median is efficient and scalable.
- The max heap stores the smaller half of the numbers, and the min heap stores the larger half.
- The median is calculated based on the sizes of the two heaps.