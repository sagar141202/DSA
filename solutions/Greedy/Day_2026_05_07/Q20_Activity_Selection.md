# Activity Selection

## Problem Statement
Given a set of activities with their start and finish times, select the maximum number of activities that can be performed by a single person, assuming that a person can only work on a single activity at a time. The activities are given as pairs of start and finish times, and the goal is to maximize the number of activities that can be completed without any conflicts. For example, if we have activities [(1, 4), (3, 5), (0, 6), (5, 7), (3, 8), (5, 9), (6, 10), (8, 11), (8, 12), (2, 13), (12, 14)], the maximum number of activities that can be selected is 4, which are [(1, 4), (5, 7), (8, 11), (12, 14)]. The constraint is that the finish time of the previous activity must be less than or equal to the start time of the next activity.

## Approach
The algorithm sorts the activities by their finish times and then iterates through the sorted list, selecting activities that do not conflict with the previously selected activity. This approach ensures that the maximum number of activities can be selected. The key insight is that selecting the activity with the earliest finish time maximizes the chance of selecting the next activity.

## Complexity
- Time: O(n log n)
- Space: O(1)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

// Function to select the maximum number of activities
int activitySelection(vector<pair<int, int>>& activities) {
    // Sort the activities by their finish times
    sort(activities.begin(), activities.end(), [](const pair<int, int>& a, const pair<int, int>& b) {
        return a.second < b.second;
    });

    // Initialize the count of selected activities
    int count = 0;

    // Initialize the finish time of the last selected activity
    int lastFinishTime = -1;

    // Iterate through the sorted activities
    for (const auto& activity : activities) {
        // Check if the current activity does not conflict with the last selected activity
        if (activity.first >= lastFinishTime) {
            // Increment the count of selected activities
            count++;

            // Update the finish time of the last selected activity
            lastFinishTime = activity.second;
        }
    }

    // Return the maximum number of activities that can be selected
    return count;
}

int main() {
    // Example usage
    vector<pair<int, int>> activities = {{1, 4}, {3, 5}, {0, 6}, {5, 7}, {3, 8}, {5, 9}, {6, 10}, {8, 11}, {8, 12}, {2, 13}, {12, 14}};
    int maxActivities = activitySelection(activities);
    cout << "Maximum number of activities that can be selected: " << maxActivities << endl;
    return 0;
}
```

## Test Cases
```
Input: [(1, 4), (3, 5), (0, 6), (5, 7), (3, 8), (5, 9), (6, 10), (8, 11), (8, 12), (2, 13), (12, 14)]
Output: 4
```

## Key Takeaways
- The activity selection problem can be solved using a greedy approach by sorting the activities by their finish times and selecting the activities that do not conflict with the previously selected activity.
- The time complexity of the algorithm is O(n log n) due to the sorting step, and the space complexity is O(1) since no additional space is used.
- The algorithm has a wide range of applications in scheduling and resource allocation problems.