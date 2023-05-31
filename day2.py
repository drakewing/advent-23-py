from typing import Dict, List


def d2p1(path: str) -> int:
    score = 0
    results = {
        "win": ["A Y", "B Z", "C X"],
        "tie": ["A X", "B Y", "C Z"],
        "loss": ["A Z", "B X", "C Y"],
    }

    with open(path) as f:
        for line in f:
            score += calc_score(line.strip(), results)

    return score

def calc_score(game: str, results: Dict[str, List[str]]) -> int:
    choice_score = ord(game[2]) - 87
    
    if game in results['win']:
        return choice_score + 6

    if game in results['tie']:
        return choice_score + 3

    return choice_score

