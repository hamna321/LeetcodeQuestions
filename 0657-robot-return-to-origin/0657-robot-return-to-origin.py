class Solution:
    def judgeCircle(self, moves: str) -> bool:
        if len(moves)%2==0:
            if moves.count("U")==moves.count("D") and moves.count("L")==moves.count("R"):
                return True
            return False