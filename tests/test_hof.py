from click.testing import CliRunner
from hof.cmd import init, add, remove, destroy
import numpy as np
import os
import pytest as pt
import pandas as pd
import shutil

PWD = os.path.dirname(__file__)


def __load_hof():
    return pd.read_csv(f"{PWD}/../data/hof.csv")


def __init_data():
    shutil.copy(f"{PWD}/data/hof.csv", f"{PWD}/../data/hof.csv")


@pt.fixture()
def runner():
    return CliRunner(mix_stderr=False)


@pt.fixture()
def hof_ans_data():
    return pd.read_csv(f"{PWD}/data/hof.csv")


def test_init(runner, hof_ans_data):
    runner.invoke(init)
    assert np.array_equal(__load_hof().values, hof_ans_data.values)


def test_remove(runner):
    name = "Ty Cobb"
    __init_data()
    runner.invoke(remove, ["--name", name])
    assert name not in __load_hof()["NAME"].values


def test_add(runner):
    name = "Barry Bonds"
    __init_data()
    runner.invoke(add, ["--name", name])
    assert name in __load_hof()["NAME"].values


def test_destroy(runner):
    __init_data()
    runner.invoke(destroy)
    assert __load_hof().empty
