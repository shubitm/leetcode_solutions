class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        radiant = deque()  # Queue for Radiant senators
        dire = deque()     # Queue for Dire senators

        # Populate the initial queues with the indices of senators from both parties
        for i, s in enumerate(senate):
            if s == 'R':
                radiant.append(i)
            else:
                dire.append(i)

        while radiant and dire:
            r_idx = radiant.popleft()  # Radiant senator
            d_idx = dire.popleft()     # Dire senator
            
            # The senator with the smaller index can ban the opponent
            if r_idx < d_idx:
                radiant.append(r_idx + len(senate))  # Radiant senator gets to act in the next round
            else:
                dire.append(d_idx + len(senate))     # Dire senator gets to act in the next round

        # If any Radiant senators remain, Radiant wins; otherwise, Dire wins
        return "Radiant" if radiant else "Dire"