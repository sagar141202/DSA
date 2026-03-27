# Activity Selection

## Problem Statement
The activity selection problem is a classic problem in greedy algorithms. We are given a set of activities, each with a start and end time. The goal is to select the maximum number of activities that can be performed by a single person, given that a person can only work on a single activity at a time. The activities are selected based on their end times, with the activity having the earliest end time being selected first. The problem has the following constraints: (1) each activity has a start and end time, (2) a person can only work on one activity at a time, and (3) the activities are non-preemptive, meaning that once an activity is started, it cannot be interrupted.

## Approach
The approach to solving this problem is to use a greedy algorithm, sorting the activities based on their end times and then selecting the activities that do not conflict with each other. The algorithm iterates through the sorted activities and selects the activities that start after the previously selected activity ends. This approach ensures that the maximum number of activities are selected.

## Complexity
- Time: O(n log n)
- Space: O(1)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

// Define a structure to represent an activity
struct Activity {
    int start;
    int end;
};

// Comparison function to sort activities based on their end times
bool compareActivities(const Activity &a, const Activity &b) {
    return a.end < b.end;
}

// Function to select the maximum number of activities
int selectActivities(Activity activities[], int n) {
    // Sort the activities based on their end times
    sort(activities, activities + n, compareActivities);

    // Initialize the count of selected activities to 1
    int count = 1;

    // Initialize the end time of the previously selected activity
    int prevEnd = activities[0].end;

    // Iterate through the sorted activities
    for (int i = 1; i < n; i++) {
        // Check if the current activity starts after the previously selected activity ends
        if (activities[i].start >= prevEnd) {
            // Increment the count of selected activities
            count++;

            // Update the end time of the previously selected activity
            prevEnd = activities[i].end;
        }
    }

    // Return the count of selected activities
    return count;
}

int main() {
    // Example usage
    Activity activities[] = {{1, 4}, {3, 5}, {0, 6}, {5, 7}, {3, 8}, {5, 9}, {6, 10}, {8, 11}, {8, 12}, {2, 13}, {12, 14}};
    int n = sizeof(activities) / sizeof(activities[0]);

    int count = selectActivities(activities, n);

    cout << "Maximum number of activities that can be selected: " << count << endl;

    return 0;
}
```

## Test Cases
```
Input: activities = [(1, 4), (3, 5), (0, 6), (5, 7), (3, 8), (5, 9), (6, 10), (8, 11), (8, 12), (2, 13), (12, 14)]
Output: Maximum number of activities that can be selected: 4
```

## Key Takeaways
- The activity selection problem can be solved using a greedy algorithm, which selects the activities based on their end times.
- The time complexity of the solution is O(n log n) due to the sorting of activities, and the space complexity is O(1) since no extra space is used.
- The solution iterates through the sorted activities and selects the activities that do not conflict with each other, ensuring the maximum number of activities are selected.