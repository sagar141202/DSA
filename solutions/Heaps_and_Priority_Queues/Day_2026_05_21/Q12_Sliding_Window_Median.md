# Sliding Window Median

## Problem Statement
Given an array of integers `nums` and an integer `k`, find the median of each `k`-sized subarray. The median is the middle value in the sorted subarray. If the subarray has an even number of elements, the median is the average of the two middle values.

## Approach
We will use a multiset to maintain the elements in the current window. We will divide the multiset into two parts: the lower half and the upper half. The lower half will store the smaller half of the elements, and the upper half will store the larger half of the elements.

## Complexity
- Time: O(n log k)
- Space: O(k)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class MedianFinder {
public:
    multiset<int> lower;
    multiset<int> upper;

    void addNum(int num) {
        // Add the number to the correct half
        if (lower.empty() || num <= *lower.rbegin()) {
            lower.insert(num);
        } else {
            upper.insert(num);
        }

        // Balance the halves
        if (lower.size() > upper.size() + 1) {
            upper.insert(*lower.rbegin());
            lower.erase(prev(lower.end()));
        } else if (upper.size() > lower.size()) {
            lower.insert(*upper.begin());
            upper.erase(upper.begin());
        }
    }

    double findMedian() {
        // Calculate the median
        if (lower.size() == upper.size()) {
            return (*lower.rbegin() + *upper.begin()) / 2.0;
        } else {
            return *lower.rbegin();
        }
    }
};

vector<double> medianSlidingWindow(vector<int>& nums, int k) {
    MedianFinder mf;
    vector<double> medians;

    for (int i = 0; i < nums.size(); i++) {
        mf.addNum(nums[i]);
        if (i >= k) {
            mf.lower.erase(mf.lower.find(nums[i - k]));
            if (mf.lower.empty() || nums[i - k] <= *mf.lower.rbegin()) {
                if (mf.upper.find(nums[i - k]) != mf.upper.end()) {
                    mf.upper.erase(mf.upper.find(nums[i - k]));
                }
            } else {
                mf.upper.erase(mf.upper.find(nums[i - k]));
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
    cout << endl;
    return 0;
}
```

## Test Cases
```
Input: nums = [1, 3, -1, -3, 5, 3, 6, 7], k = 3
Output: [1.0, -1.0, -1.0, 3.0, 5.0, 6.0]
```

## Key Takeaways
- We use a multiset to maintain the elements in the current window.
- We divide the multiset into two parts: the lower half and the upper half.
- We balance the halves to ensure that the lower half has at most one more element than the upper half.