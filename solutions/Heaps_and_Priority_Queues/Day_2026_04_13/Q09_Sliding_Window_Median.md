# Sliding Window Median

## Problem Statement
The Sliding Window Median problem involves finding the median of all numbers in a sliding window of size k, where the window moves over a given array of integers. The array can contain duplicates, and the window size k is fixed. The goal is to calculate the median for each position of the window. For example, given the array [1, 3, -1, -3, 5, 3, 6, 7] and a window size of 3, the medians for each window position would be [1, 1, -1, -1, 3, 5].

## Approach
The algorithm uses two heaps, a max heap to store the smaller half of the window and a min heap to store the larger half. The max heap stores the k/2 smaller elements, and the min heap stores the k/2 larger elements. The median is then calculated based on the sizes of the heaps.

## Complexity
- Time: O(n log k)
- Space: O(k)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class MedianFinder {
public:
    // max heap to store the smaller half of the window
    priority_queue<int> maxHeap;
    // min heap to store the larger half of the window
    priority_queue<int, vector<int>, greater<int>> minHeap;

    void addNum(int num) {
        // add num to the correct heap
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
};

vector<double> medianSlidingWindow(vector<int>& nums, int k) {
    MedianFinder mf;
    vector<double> medians;
    for (int i = 0; i < nums.size(); i++) {
        mf.addNum(nums[i]);
        if (i >= k) {
            // remove the num that is out of the window
            if (nums[i - k] <= mf.maxHeap.top()) {
                mf.maxHeap.pop();
                // add back the removed num to maintain the balance
                mf.addNum(nums[i - k]);
                mf.maxHeap.pop();
            } else {
                mf.minHeap.pop();
                // add back the removed num to maintain the balance
                mf.addNum(nums[i - k]);
                mf.minHeap.pop();
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
Output: [1, 1, -1, -1, 3, 5]
```

## Key Takeaways
- Use two heaps to maintain the balance of the window.
- The max heap stores the smaller half of the window, and the min heap stores the larger half.
- The median is calculated based on the sizes of the heaps.