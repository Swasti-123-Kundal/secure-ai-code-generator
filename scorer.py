def calculate_score(syntax_ok, security_result):
    score = 100

    if not syntax_ok:
        score -= 40

    if "Unsafe" in security_result:
        score -= 30

    return max(score, 0)