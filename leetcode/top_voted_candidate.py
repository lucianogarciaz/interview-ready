class TopVotedCandidate:
    """

    
      times: 0 5 10 15 20 25 30
      pers:  0 1 1  0  0  1  0
      res:   0 1 1  0  0  1
        res: 0, 1, 1, 0
        counter = [0:2,1:2]
        q: 3-> 0
        q:12-> 1
        q25:-> 1
        q:15-> 0
        q:24-> 0
        q:8 -> 1
    first try:
        init: 
            counter[p] = counter.get(p, 0)+1
            person_winner = res[t-1]
            if counter[person_winner] <= counter[p]:
                res[t] = p
            else:
                res[t] = person_winner
            
            
            counter = {0:0, 1:0}

        q: o(len(times))
            loop: t >= times[i]: res[i]
    second try:
        q: (log n)
            i = bisect.bisect_right
            return res[i]
    """  
    
    def __init__(self, persons: List[int], times: List[int]):
        self.persons = persons
        self.times = times
        self.res = []
        counter = {}
        for i in range(len(self.persons)):
            winner = self.persons[i]
            if i == 0:
                counter[winner] = 1
                self.res.append(winner)
                continue
            prev_winner = self.res[i-1]
            amount_prev = counter[prev_winner]
            counter[winner] = counter.get(winner,0) + 1
            if counter[winner] >= amount_prev:
                self.res.append(winner)
            else:
                self.res.append(prev_winner)

    def q(self, t: int) -> int:
        i = bisect.bisect_left(self.times,t)
        if len(self.times) == i:
            i = i-1
        elif self.times[i]!=t:
            i = i-1
        return self.res[i]


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)