# Meeting Rooms II

## Problem Statement
Given an array of meeting time intervals consisting of start and end times, determine if a person could attend all meetings. The meetings are non-overlapping if the start time of one meeting is greater than the end time of the previous meeting. However, in this problem, we are given an array of meeting time intervals, and we need to find the minimum number of conference rooms required to accommodate all the meetings. For example, if we have the following meetings: [[0, 30],[5, 10],[15, 20]], we need at least 2 rooms because the meetings [0, 30] and [5, 10] overlap, and the meetings [5, 10] and [15, 20] also overlap.

## Approach
We can solve this problem using a priority queue to store the end times of the meetings. We first sort the meetings based on their start times, and then we iterate over the sorted meetings. For each meeting, we check if the earliest end time (which is the top of the priority queue) is earlier than the start time of the current meeting. If it is, we remove the earliest end time from the priority queue and add the end time of the current meeting to the priority queue.

## Complexity
- Time: O(n log n)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int minMeetingRooms(vector<vector<int>>& intervals) {
        // If there are no meetings, we don't need any rooms.
        if (intervals.empty()) {
            return 0;
        }

        // Sort the meetings based on their start times.
        sort(intervals.begin(), intervals.end(), [](const vector<int>& a, const vector<int>& b) {
            return a[0] < b[0];
        });

        // Initialize a priority queue to store the end times of the meetings.
        priority_queue<int, vector<int>, greater<int>> endTimes;

        // Add the end time of the first meeting to the priority queue.
        endTimes.push(intervals[0][1]);

        // Iterate over the rest of the meetings.
        for (int i = 1; i < intervals.size(); i++) {
            // If the earliest end time is earlier than the start time of the current meeting,
            // we can reuse the room, so we remove the earliest end time from the priority queue.
            if (endTimes.top() <= intervals[i][0]) {
                endTimes.pop();
            }

            // Add the end time of the current meeting to the priority queue.
            endTimes.push(intervals[i][1]);
        }

        // The size of the priority queue is the minimum number of rooms required.
        return endTimes.size();
    }
};
```

## Test Cases
```
Input: [[0, 30],[5, 10],[15, 20]]
Output: 2
Input: [[7, 10],[2, 4]]
Output: 1
```

## Key Takeaways
- We can use a priority queue to efficiently manage the end times of the meetings.
- We need to sort the meetings based on their start times to ensure that we are considering the meetings in the correct order.
- The size of the priority queue at the end of the algorithm is the minimum number of rooms required to accommodate all the meetings.