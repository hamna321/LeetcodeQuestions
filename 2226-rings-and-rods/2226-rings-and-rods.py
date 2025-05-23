class Solution:
    def countPoints(self, rings: str) -> int:
        rod_colors = {}
        
        # Process the string in pairs (color + rod)
        for i in range(0, len(rings), 2):
            color = rings[i]
            rod = rings[i+1]
            
            if rod not in rod_colors:
                rod_colors[rod] = set()
            rod_colors[rod].add(color)
        
        # Count rods with all three colors
        count = 0
        for colors in rod_colors.values():
            if len(colors) == 3:
                count += 1
                
        return count