def threat_score(label):

    scores = {
        "Normal":1,
        "Flooding":5,
        "Sybil":7,
        "Blackhole":9,
        "Wormhole":10
    }

    score = scores.get(label,3)

    if score <=3:
        level="LOW"
    elif score <=6:
        level="MEDIUM"
    elif score <=8:
        level="HIGH"
    else:
        level="CRITICAL"

    return score,level