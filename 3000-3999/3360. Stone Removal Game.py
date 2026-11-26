class Solution:
    def canAliceWin(self, n: int) -> bool:
        remove = 10
        alice_turn = True

        while n >= remove:
            n -= remove
            remove -= 1
            alice_turn = not alice_turn

        # If it's Alice's turn and she can't move, she loses (return False).
        # If it's Bob's turn and he can't move, Alice wins (return True).
        return not alice_turn