# PatchPilot Demo Target

Small Python repository for demonstrating PatchPilot against a safe,
reproducible target project.

## Intentional demo bug

`src/calculator.py::divide` multiplies instead of dividing. The issue is
recorded in [issues/001-fix-divide.md](issues/001-fix-divide.md).

Expected repair:

```python
return a / b
```

PatchPilot should retrieve `src/calculator.py`, propose one Python-file
modification, validate the original content, generate a deterministic diff,
run the tests in its separate sandbox, and wait for explicit approval before
publishing a pull request.

## Run locally

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -e ".[test]"
python -m pytest -q
```

Python 3.12 is the documented target runtime. The project uses no network
services and contains no secrets.

## Safe-failure demonstration

See [issues/002-unsafe-request.md](issues/002-unsafe-request.md). That issue
intentionally requests a traversal path and test-file modification. PatchPilot
must reject it, report an unsafe-path or protected-path validation error, and
create no pull request.

## GitHub demonstration

Create a new public repository named `patchpilot-demo-target`, push this
directory to its `main` branch, and open the two issue files as GitHub issues.
Use the clear bug issue for the success path and the unsafe issue for the
rejection path. Do not add credentials or private source data.
