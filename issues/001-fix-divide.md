# Fix `divide` returning the wrong result

## Description

`divide(a, b)` currently returns the product instead of the quotient for
non-zero numeric inputs.

## Acceptance criteria

- `divide(8, 2)` returns `4`.
- `divide(3, 2)` returns `1.5`.
- Division by zero continues to raise `ValueError`.
- Modify only the implementation needed for this bug.
- Do not modify tests or project configuration.
