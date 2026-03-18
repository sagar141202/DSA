# Meeting Rooms II

## Problem Statement
Given an array of meeting time intervals consisting of start and end times, determine the minimum number of rooms required to accommodate all meetings. Each meeting is represented as an interval [start, end], and the start and end times are in minutes. For example, if we have the following meeting intervals: [[0, 30],[5, 10],[15, 20]], we need at least 2 rooms to accommodate all meetings. The constraints are: 1 <= intervals.length <= 10^4, 0 <= start_i < end_i <= 10^6.

## Approach
We will use a priority queue to store the end times of the meetings. The intuition is to always try to reuse a room if possible, which is the room that ends earliest. We will sort the start times and end times separately, then iterate over the start times and update the priority queue accordingly.

## Complexity
- Time: O(n log n)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

struct Interval {
    int start;
    int end;
};

int minMeetingRooms(vector<Interval>& intervals) {
    if (intervals.empty()) return 0;

    vector<int> starts;
    vector<int> ends;

    for (auto& interval : intervals) {
        starts.push_back(interval.start);
        ends.push_back(interval.end);
    }

    sort(starts.begin(), starts.end());
    sort(ends.begin(), ends.end());

    int i = 0; // index for starts
    int j = 0; // index for ends
    int rooms = 0; // minimum number of rooms required
    int currRooms = 0; // current number of rooms in use
    priority_queue<int, vector<int>, greater<int>> pq; // priority queue to store end times

    while (i < starts.size()) {
        if (starts[i] < ends[j]) {
            // If a new meeting starts before the earliest end time, add a new room
            pq.push(ends[j]);
            currRooms++;
            i++;
        } else {
            // If a meeting ends before a new one starts, reuse the room
            pq.pop();
            currRooms--;
            j++;
        }

        rooms = max(rooms, currRooms);
    }

    return rooms;
}
```

## Test Cases
```
Input: [[0, 30],[5, 10],[15, 20]]
Output: 2
Input: [[7, 10],[2, 4]]
Output: 1
```

## Key Takeaways
- We need to use a priority queue to efficiently store and retrieve the end times of the meetings.
- Sorting the start and end times separately allows us to iterate over the start times and update the priority queue accordingly.
- The minimum number of rooms required is the maximum number of rooms in use at any point in time.