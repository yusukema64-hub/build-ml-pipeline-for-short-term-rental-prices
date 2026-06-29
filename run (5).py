import pytest
import pandas as pd
import wandb
import os


@pytest.fixture(scope="session")
def data(request):
    return pd.read_csv(os.environ["CSV"])


@pytest.fixture(scope="session")
def ref_data(request):
    return pd.read_csv(os.environ["REF"])


@pytest.fixture(scope="session")
def kl_threshold(request):
    return float(os.environ["KL_THRESHOLD"])


@pytest.fixture(scope="session")
def min_price(request):
    return float(os.environ["MIN_PRICE"])


@pytest.fixture(scope="session")
def max_price(request):
    return float(os.environ["MAX_PRICE"])
