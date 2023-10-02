class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        alice=0
        bob=0

        for i in range(1,len(colors)-1):
            cur_color=colors[i]
            prev_color=colors[i-1]
            next_color=colors[i+1]

            if cur_color=='A' and prev_color=='A' and next_color=='A':
                alice+=1
            
            elif cur_color=='B' and prev_color=='B' and next_color=='B':
                bob+=1

        return alice>bob
