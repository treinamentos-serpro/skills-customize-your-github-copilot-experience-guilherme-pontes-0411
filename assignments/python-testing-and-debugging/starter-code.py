def calculate_average(scores: list[float]) -> float:
    if not scores:
        raise ValueError("scores must not be empty")
    return sum(scores) / len(scores)


def is_passing(score: int) -> bool:
    return score > 60