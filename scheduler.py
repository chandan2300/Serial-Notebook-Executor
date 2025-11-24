
import os
import sys
import time
import logging
import nbformat
from nbconvert.preprocessors import ExecutePreprocessor, CellExecutionError

# Ensure logs directory exists
LOG_DIR = "logs"
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

class LoggingExecutePreprocessor(ExecutePreprocessor):
    def preprocess_cell(self, cell, resources, index):
        logging.info(f"Executing cell {index + 1}...")
        return super().preprocess_cell(cell, resources, index)

def setup_logger(notebook_name):
    """
    Sets up a logger that writes to both console and a file.
    """
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    
    # Clear existing handlers to avoid duplicate logs
    if logger.hasHandlers():
        logger.handlers.clear()

    # Console Handler
    c_handler = logging.StreamHandler(sys.stdout)
    c_handler.setFormatter(logging.Formatter('[%(asctime)s] %(message)s', datefmt='%H:%M:%S'))
    logger.addHandler(c_handler)

    # File Handler
    timestamp = time.strftime("%Y%m%d_%H%M%S")
    log_file = os.path.join(LOG_DIR, f"{notebook_name}_{timestamp}.log")
    f_handler = logging.FileHandler(log_file)
    f_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
    logger.addHandler(f_handler)
    
    return log_file

def run_notebook(notebook_path):
    """
    Runs a Jupyter notebook using nbconvert Python API with cell-level logging.
    """
    notebook_name = os.path.splitext(os.path.basename(notebook_path))[0]
    log_file = setup_logger(notebook_name)
    
    logging.info(f"Starting execution of {notebook_path}...")
    logging.info(f"Logs are being saved to {log_file}")
    
    # Check if file exists
    if not os.path.exists(notebook_path):
        logging.error(f"Notebook not found at {notebook_path}")
        return False

    nb = None
    execution_failed = False

    try:
        # Read the notebook
        with open(notebook_path) as f:
            nb = nbformat.read(f, as_version=4)

        # Configure the preprocessor
        # timeout=-1 means no timeout
        ep = LoggingExecutePreprocessor(timeout=-1, kernel_name='python3')

        # Execute the notebook
        # resources={'metadata': {'path': 'notebooks/'}} helps find relative paths if needed
        ep.preprocess(nb, {'metadata': {'path': os.path.dirname(notebook_path)}})
        
        logging.info(f"Successfully finished {notebook_path}")

    except CellExecutionError as e:
        logging.error(f"Error executing cell in {notebook_path}:")
        logging.error(str(e))
        execution_failed = True
    except Exception as e:
        logging.error(f"An error occurred while running {notebook_path}:")
        logging.error(str(e))
        execution_failed = True
    
    # Save the notebook regardless of success or failure (if it was read)
    if nb:
        try:
            with open(notebook_path, 'w', encoding='utf-8') as f:
                nbformat.write(nb, f)
            logging.info(f"Notebook saved to {notebook_path}")
        except Exception as e:
            logging.error(f"Failed to save notebook {notebook_path}: {e}")
            return False

    return not execution_failed

import argparse

def main():
    parser = argparse.ArgumentParser(description="Schedule sequential execution of Jupyter Notebooks.")
    parser.add_argument("notebooks", nargs="*", help="List of notebook paths to execute.")
    args = parser.parse_args()

    if args.notebooks:
        notebooks = args.notebooks
    else:
        # Default list if no arguments provided
        notebooks = [
            "notebooks/test_nb_1.ipynb",
            # "notebooks/fail_nb.ipynb",
            "notebooks/test_nb_2.ipynb"
        ]
    
    print("Starting sequential notebook scheduler...")
    print("----------------------------------------")

    for nb in notebooks:
        success = run_notebook(nb)
        if not success:
            print("Stopping execution due to failure.")
            sys.exit(1)
        
        # Optional: explicit garbage collection or wait if needed
        logging.info("Kernel cleared and resources released.\n")

    print("----------------------------------------")
    print("All notebooks executed successfully.")

if __name__ == "__main__":
    main()

