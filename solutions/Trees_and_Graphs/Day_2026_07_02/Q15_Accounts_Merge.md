# Accounts Merge

## Problem Statement
Given a list of accounts where each account is a list of emails, merge all the accounts that have the same email. The goal is to group all the emails that belong to the same person. Each email should only appear once in the output, and the emails in each account should be sorted. The input is a list of lists of strings, where each inner list represents an account and each string is an email. The output should be a list of lists of strings, where each inner list represents a merged account.

## Approach
We can solve this problem by using a union-find data structure to group the accounts that have the same email. Then, we can iterate over the accounts and merge the ones that belong to the same group. We use a map to store the parent of each email and a set to store the emails in each group.

## Complexity
- Time: O(N * M * log(M))
- Space: O(N * M)

## C++ Solution
```cpp
#include <iostream>
#include <vector>
#include <string>
#include <unordered_map>
#include <set>
#include <algorithm>

class UnionFind {
public:
    std::unordered_map<std::string, std::string> parent;
    std::unordered_map<std::string, std::set<std::string>> emails;

    std::string find(const std::string& email) {
        if (parent[email] != email) {
            parent[email] = find(parent[email]);
        }
        return parent[email];
    }

    void unionEmails(const std::string& email1, const std::string& email2) {
        std::string parent1 = find(email1);
        std::string parent2 = find(email2);
        if (parent1 != parent2) {
            parent[parent1] = parent2;
            emails[parent2].insert(emails[parent1].begin(), emails[parent1].end());
            emails.erase(parent1);
        }
    }

    void addEmail(const std::string& email) {
        if (parent.find(email) == parent.end()) {
            parent[email] = email;
            emails[email] = {email};
        }
    }
};

std::vector<std::vector<std::string>> accountsMerge(std::vector<std::vector<std::string>>& accounts) {
    UnionFind uf;
    for (const auto& account : accounts) {
        for (const auto& email : account) {
            uf.addEmail(email);
        }
    }

    for (const auto& account : accounts) {
        for (int i = 1; i < account.size(); i++) {
            uf.unionEmails(account[0], account[i]);
        }
    }

    std::vector<std::vector<std::string>> result;
    for (const auto& group : uf.emails) {
        std::vector<std::string> emails(group.second.begin(), group.second.end());
        std::sort(emails.begin(), emails.end());
        result.push_back(emails);
    }
    return result;
}

int main() {
    std::vector<std::vector<std::string>> accounts = {
        {"johnsmith@email.com", "john00@email.com", "john_newyork@email.com"},
        {"johnsmith@email.com", "johnnybravo@email.com"}
    };

    std::vector<std::vector<std::string>> result = accountsMerge(accounts);
    for (const auto& account : result) {
        for (const auto& email : account) {
            std::cout << email << " ";
        }
        std::cout << std::endl;
    }

    return 0;
}
```

## Test Cases
```
Input: [["johnsmith@email.com","john00@email.com","john_newyork@email.com"],["johnsmith@email.com","johnnybravo@email.com"]]
Output: [["john00@email.com","john_newyork@email.com","johnsmith@email.com"],["johnnybravo@email.com"]]
```

## Key Takeaways
- Use a union-find data structure to group the accounts that have the same email.
- Iterate over the accounts and merge the ones that belong to the same group.
- Use a map to store the parent of each email and a set to store the emails in each group.