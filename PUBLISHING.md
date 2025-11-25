# Publishing to PyPI

You can publish this package to the Python Package Index (PyPI) so anyone can install it with `pip install jupyter-serial-scheduler`.

## Prerequisites

1.  **Create a PyPI Account**:
    - Go to [pypi.org](https://pypi.org/) and register.
    - (Optional but recommended) Go to [test.pypi.org](https://test.pypi.org/) and register for a test account.

2.  **Install Build Tools**:
    You need `build` and `twine` installed.
    ```bash
    pip install build twine
    ```

## Steps to Publish

1.  **Build the Package**:
    Run this command from the project root to create the distribution files (`dist/`).
    ```bash
    python -m build
    ```

2.  **Check the Artifacts**:
    Verify that the files in `dist/` look correct.
    ```bash
    twine check dist/*
    ```

3.  **Upload to TestPyPI** (Recommended first):
    ```bash
    twine upload --repository testpypi dist/*
    ```
    You will be prompted for your TestPyPI username and password (or API token).

4.  **Upload to PyPI** (Production):
    Once you verified it works on TestPyPI, upload to the real PyPI.
    ```bash
    twine upload dist/*
    ```

## Installing from PyPI

After uploading, you (and anyone else) can install it:

```bash
pip install jupyter-serial-scheduler
```
