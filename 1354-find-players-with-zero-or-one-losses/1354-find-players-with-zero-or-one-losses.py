class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        result = set()
        winner = 0
        looser = 1
        
        loss_count = {}
        
        for player in matches:
            # Increment loss count for losers
            if player[looser] not in loss_count:
                loss_count[player[looser]] = 0
            loss_count[player[looser]] += 1
            
            # Add winners who haven't lost yet
            if player[winner] not in loss_count:
                loss_count[player[winner]] = 0
                result.add(player[winner])
            elif loss_count[player[winner]] == 0:
                result.add(player[winner])
        
        # Extract no_losses and one_loss players
        no_losses = sorted([player for player in loss_count if loss_count[player] == 0])
        one_loss = sorted([player for player in loss_count if loss_count[player] == 1])

        return [no_losses, one_loss]
