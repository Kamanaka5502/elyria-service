def legitimacy_score(
    coherence: float,
    conflict_rate: float,
    override_rate: float,
    policy_distance: float
) -> float:
    penalties = (
        conflict_rate * 0.4 +
        override_rate * 0.3 +
        policy_distance * 0.3
    )
    score = 1.0 - penalties
    return max(0.0, min(1.0, score))
