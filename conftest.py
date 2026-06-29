#!/usr/bin/env python
"""
This script runs the data checks (tests) against the provided CSV file.
"""
import argparse
import logging
import pandas as pd
import wandb
import pytest
import os


logging.basicConfig(level=logging.INFO, format="%(asctime)-15s %(message)s")
logger = logging.getLogger()


def go(args):

    run = wandb.init(job_type="data_checks")
    run.config.update(args)

    logger.info("Downloading csv artifact")
    local_path = run.use_artifact(args.csv).file()

    logger.info("Downloading ref artifact")
    ref_path = run.use_artifact(args.ref).file()

    # NOTE: we use pytest to run the tests. This way we can leverage the
    # pytest infrastructure to run the tests and produce a report.
    # We pass the parameters to pytest using environment variables.
    # This is because pytest does not allow to pass parameters to the test
    # functions from the command line.
    os.environ["CSV"] = local_path
    os.environ["REF"] = ref_path
    os.environ["KL_THRESHOLD"] = str(args.kl_threshold)
    os.environ["MIN_PRICE"] = str(args.min_price)
    os.environ["MAX_PRICE"] = str(args.max_price)

    # Run the tests
    logger.info("Running data tests")
    r = pytest.main(["-vv", os.path.dirname(os.path.abspath(__file__)), "--tb=short"])

    # Fail the job if the tests fail
    if r != 0:
        raise RuntimeError("Some data tests failed (see above)")


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Run data quality checks")

    parser.add_argument(
        "--csv",
        type=str,
        help="Fully-qualified name for the input artifact (the dataset to be tested)",
        required=True
    )

    parser.add_argument(
        "--ref",
        type=str,
        help="Fully-qualified name for the reference artifact",
        required=True
    )

    parser.add_argument(
        "--kl_threshold",
        type=float,
        help="Threshold on the KL divergence to detect data drift",
        required=True
    )

    parser.add_argument(
        "--min_price",
        type=float,
        help="Minimum allowed price",
        required=True
    )

    parser.add_argument(
        "--max_price",
        type=float,
        help="Maximum allowed price",
        required=True
    )

    args = parser.parse_args()

    go(args)
