# Jupyter Notebook Scheduler

A simple Python script to execute multiple Jupyter Notebooks sequentially. This tool ensures that each notebook runs in a separate process, guaranteeing that GPU memory and other resources are fully released between runs.

## Features

- **Sequential Execution**: Runs notebooks one after another.
- **Resource Isolation**: Each notebook runs in a fresh process, clearing the kernel and freeing GPU memory upon completion.
- **Error Handling**: Stops execution if a notebook fails (configurable).

## Usage

1.  **Install Dependencies**:
    Ensure you have `jupyter` and `nbconvert` installed.
    ```bash
    pip install jupyter nbconvert
    ```

2.  **Place Notebooks**:
    Put your `.ipynb` files in the `notebooks/` directory.

3.  **Run the Scheduler**:
    ```bash
    python scheduler.py
    ```

## Configuration

You can modify `scheduler.py` to change the list of notebooks or the directory they are located in.
