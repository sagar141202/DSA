# Meeting Rooms II

## Problem Statement
Given an array of meeting time intervals consisting of start and end times, determine if a person could attend all meetings. The meetings are non-overlapping if a person can attend all of them. The start time will always be less than or equal to the end time. Example: Input: [[0,30],[5,10],[15,20]], Output: 2. The minimum number of rooms required to hold all meetings is 2.

## Approach
We can use a priority queue to store the end times of the meetings. We iterate through the meetings and for each meeting, we check if the start time is greater than or equal to the smallest end time in the queue. If it is, we remove the smallest end time from the queue and add the end time of the current meeting. If not, we add the end time of the current meeting to the queue. The size of the queue at any time represents the minimum number of rooms required.

## Complexity
- Time: O(N log N)
- Space: O(N)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int minMeetingRooms(vector<vector<int>>& intervals) {
        if (intervals.empty()) {
            return 0;
        }
        
        // Sort the intervals by start time
        sort(intervals.begin(), intervals.end(), [](const vector<int>& a, const vector<int>& b) {
            return a[0] < b[0];
        });
        
        // Priority queue to store the end times
        priority_queue<int, vector<int>, greater<int>> endTimes;
        
        // Add the end time of the first meeting to the queue
        endTimes.push(intervals[0][1]);
        
        // Iterate through the rest of the meetings
        for (int i = 1; i < intervals.size(); i++) {
            // If the start time is greater than or equal to the smallest end time, remove it from the queue
            if (intervals[i][0] >= endTimes.top()) {
                endTimes.pop();
            }
            // Add the end time of the current meeting to the queue
            endTimes.push(intervals[i][1]);
        }
        
        // The size of the queue represents the minimum number of rooms required
        return endTimes.size();
    }
};
```

## Test Cases
```
Input: [[0,30],[5,10],[15,20]]
Output: 2
Input: [[7,10],[2,4]]
Output: 1
```

## Key Takeaways
- Use a priority queue to efficiently manage the end times of the meetings.
- Sort the meetings by start time to ensure that we process them in the correct order.
- The size of the priority queue at any time represents the minimum number of rooms required to hold all meetings.