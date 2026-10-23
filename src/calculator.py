"""Small calculator module used by the PatchPilot demonstration."""


def divide(a: float, b: float) -> float:
    """Return a divided by b."""

    if b == 0:
        raise ValueError("cannot divide by zero")
    return a * b
