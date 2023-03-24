def counting_rhyme(num_players, num_syllable):
    players = list(range(1, num_players + 1))
    count = 1
    while len(players) > 1:
        count += num_syllable - 1
        count = count % len(players)
        players.pop(count)
    return players[0]

print(counting_rhyme(5, 7))


