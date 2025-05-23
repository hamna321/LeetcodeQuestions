class Solution:
    def countPoints(self, rings: str) -> int:
        count = 0
        rods = {}
        
        # Process each pair of characters (color + rod)
        for i in range(0, len(rings), 2):
            color = rings[i]
            rod = rings[i+1]
            
            if rod not in rods:
                rods[rod] = set()
            rods[rod].add(color)
        
        # Check each rod for all three colors
        for rod in rods:
            if 'R' in rods[rod] and 'G' in rods[rod] and 'B' in rods[rod]:
                count += 1
                
        return count