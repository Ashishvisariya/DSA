class Solution(object):
    def canAliceWin(self, n):
        remove = 10
        alice_turn = True

        while n >= remove:
            n -= remove
            remove -= 1
            alice_turn = not alice_turn

        return not alice_turn