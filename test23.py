def rankTeams(votes):
    """
    :type votes: List[str]
    :rtype: str
    """
    vote_size = len(votes)
    team_size = len(votes[0])
    if vote_size==1 or team_size==1:
        return votes[0]

    team_counts = [0 for i in range(team_size+1)]

    oneteam_counts =dict()
    for team in votes[0]:
        oneteam_counts[team]=team_counts[:]
        oneteam_counts[team][-1]=ord(team)-ord('A')

    for vote in votes:
        for i in range(len(vote)):
            oneteam_counts[vote[i]][i]+=1

    bucket = [[] for i in range(27)]

