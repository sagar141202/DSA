# Simplify Path

## Problem Statement
Given an absolute path to a file, simplify the path by removing any redundant directories (i.e., directories that are followed by ".." which represents the parent directory) and return the simplified path. The path starts with a slash ("/") and only contains letters, digits, and slashes. The path does not end with a slash. For example, "/home/" is equivalent to "/home", and "/../" is equivalent to "/". Also, "/home//foo/" is equivalent to "/home/foo". The path is guaranteed to be a valid Unix path.

## Approach
The approach involves using a stack to store the directories in the path. When a ".." directory is encountered, the top directory is popped from the stack if it's not empty. When a "." directory is encountered, it's simply ignored. Finally, the simplified path is constructed by joining the directories in the stack with a slash.

## Complexity
- Time: O(n)
- Space: O(n)

## C++ Solution
```cpp
#include <iostream>
#include <vector>
#include <string>
#include <sstream>

class Solution {
public:
    string simplifyPath(string path) {
        vector<string> stack;
        string token;
        stringstream ss(path);
        while (getline(ss, token, '/')) {
            if (token == "" || token == ".") {
                continue;
            } else if (token == "..") {
                if (!stack.empty()) {
                    stack.pop_back();
                }
            } else {
                stack.push_back(token);
            }
        }
        string simplifiedPath = "/";
        for (const auto& dir : stack) {
            simplifiedPath += dir + "/";
        }
        if (simplifiedPath != "/") {
            simplifiedPath.pop_back(); // remove the trailing slash
        }
        return simplifiedPath;
    }
};

int main() {
    Solution solution;
    string path = "/home//foo/";
    cout << "Simplified path: " << solution.simplifyPath(path) << endl;
    return 0;
}
```

## Test Cases
```
Input: "/home/"
Output: "/home"
Input: "/../"
Output: "/"
Input: "/home//foo/"
Output: "/home/foo"
```

## Key Takeaways
- Use a stack to store the directories in the path.
- Handle ".." and "." directories separately to simplify the path.
- Construct the simplified path by joining the directories in the stack with a slash.