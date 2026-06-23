# Sliding Window Median

## Problem Statement
The Sliding Window Median problem involves finding the median of all numbers in a sliding window of size `k` within an array of integers. The array is given as `nums`, and the window size is given as `k`. The task is to return an array of medians for each possible sliding window. The median of a window is the middle value in the sorted window. If the window has an even number of elements, the median is the average of the two middle values. For example, given `nums = [1, 3, -1, -3, 5, 3, 6, 7]` and `k = 3`, the output should be `[1, -1, -1, 3, 5, 6]`.

## Approach
The algorithm uses two heaps: a max-heap to store the smaller half of the window and a min-heap to store the larger half. It maintains the balance between the two heaps to efficiently calculate the median. The max-heap stores the smaller half of the window, and the min-heap stores the larger half.

## Complexity
- Time: O(n log k)
- Space: O(k)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class MedianFinder {
public:
    priority_queue<int> maxHeap; // max-heap for smaller half
    priority_queue<int, vector<int>, greater<int>> minHeap; // min-heap for larger half

    void addNum(int num) {
        // Add the number to the correct heap
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

    double findMedian() {
        // Calculate the median
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
            // Remove the number that is out of the window
            if (nums[i - k] <= mf.maxHeap.top()) {
                // Remove from max-heap
                priority_queue<int> newMaxHeap;
                while (!mf.maxHeap.empty()) {
                    if (mf.maxHeap.top() != nums[i - k]) {
                        newMaxHeap.push(mf.maxHeap.top());
                    }
                    mf.maxHeap.pop();
                }
                mf.maxHeap = newMaxHeap;
                if (mf.maxHeap.empty() || mf.minHeap.top() < mf.maxHeap.top()) {
                    mf.maxHeap.push(mf.minHeap.top());
                    mf.minHeap.pop();
                }
            } else {
                // Remove from min-heap
                priority_queue<int, vector<int>, greater<int>> newMinHeap;
                while (!mf.minHeap.empty()) {
                    if (mf.minHeap.top() != nums[i - k]) {
                        newMinHeap.push(mf.minHeap.top());
                    }
                    mf.minHeap.pop();
                }
                mf.minHeap = newMinHeap;
                if (mf.minHeap.empty() || mf.maxHeap.top() > mf.minHeap.top()) {
                    mf.minHeap.push(mf.maxHeap.top());
                    mf.maxHeap.pop();
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
    vector<double> medians = medianSlidingWindow(nums, k);
    for (double median : medians) {
        cout << median << " ";
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
- The use of two heaps (max-heap and min-heap) allows for efficient calculation of the median in a sliding window.
- Maintaining the balance between the two heaps is crucial for ensuring the correctness of the algorithm.
- The time complexity of O(n log k) is achieved due to the use of heaps, where n is the size of the input array and k is the window size.