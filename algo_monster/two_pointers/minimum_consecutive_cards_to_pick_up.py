"""
You are given an integer array cards where cards[i] represents the value of the ith card. A pair of cards are matching if the cards have the same value.

Return the minimum number of consecutive cards you have to pick up to have a pair of matching cards among the picked cards. If it is impossible to have matching cards, return -1.


Example 1:

Input: cards = [3,4,2,3,4,7]
Output: 4
Explanation: We can pick up the cards [3,4,2,3] which contain a matching pair of cards with value 3. Note that picking up the cards [4,2,3,4] is also optimal.
Example 2:

Input: cards = [1,0,5,3]
Output: -1
Explanation: There is no way to pick up a set of consecutive cards that contain a pair of matching cards.
 

Constraints:

1 <= cards.length <= 105
0 <= cards[i] <= 

https://leetcode.com/problems/minimum-consecutive-cards-to-pick-up/description/
"""

class Solution:
    def minimum_card_pick_up(self, cards: list[int]) -> int:

        
        unique_chars = set([])
        min_len = len(cards) + 1
        l = 0

        for r, val in enumerate(cards):

            while val in unique_chars:
                current_len = r - l + 1
                min_len = min(min_len, current_len)
                unique_chars.remove(cards[l])
                l += 1

            unique_chars.add(val)

        return -1 if min_len == len(cards) + 1 else min_len
    
    def minimum_card_pick_up_dict(self, cards: list[int]) -> int:

        cards_seen = {}
        min_len = len(cards) + 1
        l = 0

        for r, val in enumerate(cards):

            if val in cards_seen:
                current_len = r - l + 1
                min_len = min(min_len, current_len)
                l = cards_seen[val] + 1
            
            cards_seen[val] = r
        
        return -1 if min_len == len(cards) + 1 else min_len
    


if __name__ == "__main__":
    cards = [3,4,2,3,4,7]
    sol = Solution().minimum_card_pick_up(cards)
    print(sol)

    cards = [1,0,5,3]
    sol = Solution().minimum_card_pick_up(cards)
    print(sol)

    print("Cards seen with dict approach")

    cards = [3,4,2,3,4,7]
    sol = Solution().minimum_card_pick_up_dict(cards)
    print(sol)

    cards = [1,0,5,3]
    sol = Solution().minimum_card_pick_up_dict(cards)
    print(sol)
