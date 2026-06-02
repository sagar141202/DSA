# Activity Selection

## Problem Statement
Given a set of activities with their start and finish times, select the maximum number of activities that can be performed by a single person, assuming that a person can only work on a single activity at a time. The activities are represented as pairs of integers, where the first integer is the start time and the second integer is the finish time. The goal is to find the maximum number of non-overlapping activities. For example, if we have the following activities: (1, 4), (3, 5), (0, 6), (5, 7), (3, 8), (5, 9), (6, 10), (8, 11), (8, 12), (2, 13), (12, 14), the maximum number of non-overlapping activities is 4.

## Approach
The algorithm sorts the activities based on their finish times and then iterates over the sorted activities, selecting the ones that do not overlap with the previously selected activity. This approach ensures that we select the maximum number of non-overlapping activities. The key insight is that if we select the activity with the earliest finish time, we have the maximum chance of selecting the next activity.

## Complexity
- Time: O(n log n)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

// Structure to represent an activity
struct Activity {
    int start;
    int finish;
};

// Comparison function to sort activities based on finish time
bool compareActivities(const Activity &a, const Activity &b) {
    return a.finish < b.finish;
}

// Function to select the maximum number of non-overlapping activities
int selectActivities(vector<Activity> &activities) {
    // Sort the activities based on their finish times
    sort(activities.begin(), activities.end(), compareActivities);

    // Initialize the count of selected activities
    int count = 1;

    // Initialize the finish time of the last selected activity
    int lastFinish = activities[0].finish;

    // Iterate over the sorted activities
    for (int i = 1; i < activities.size(); i++) {
        // Check if the current activity does not overlap with the last selected activity
        if (activities[i].start >= lastFinish) {
            // Increment the count of selected activities
            count++;

            // Update the finish time of the last selected activity
            lastFinish = activities[i].finish;
        }
    }

    // Return the maximum number of non-overlapping activities
    return count;
}

int main() {
    // Example usage
    vector<Activity> activities = {{1, 4}, {3, 5}, {0, 6}, {5, 7}, {3, 8}, {5, 9}, {6, 10}, {8, 11}, {8, 12}, {2, 13}, {12, 14}};
    cout << "Maximum number of non-overlapping activities: " << selectActivities(activities) << endl;
    return 0;
}
```

## Test Cases
```
Input: [(1, 4), (3, 5), (0, 6), (5, 7), (3, 8), (5, 9), (6, 10), (8, 11), (8, 12), (2, 13), (12, 14)]
Output: 4
```

## Key Takeaways
- The problem can be solved using a greedy approach by sorting the activities based on their finish times.
- The key insight is to select the activity with the earliest finish time to maximize the chance of selecting the next activity.
- The time complexity of the solution is O(n log n) due to the sorting step, and the space complexity is O(n) for storing the activities.