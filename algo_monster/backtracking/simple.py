"""
Given a non-negative integer n, find all n-letter words composed by 'a' and 'b', return them in a list of strings in lexicographical order.

Input: 2
Output: ["aa", "ab", "ba", "bb"]

Input: 4
Output: ["aaaa", "aaab", "aaba", "aabb", "abaa", "abab", "abba", "abbb", "baaa", "baab", "baba", "babb", "bbaa", "bbab", "bbba", "bbbb"]
"""

def letter_combination(n: int) -> list[str]:

    res: list[str] = []

    def dfs(start_index: int, path: list[str]):

        if start_index == n:
            res.append("".join(path))
            return

        for letter in "ab":
            path.append(letter)
            dfs(start_index + 1, path)
            path.pop()

    dfs(0, [])
    return res


if __name__ == "__main__":
    n = 3
    res = letter_combination(n)
    for line in sorted(res):
        print(line)

