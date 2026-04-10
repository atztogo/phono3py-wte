"""Pytest fixtures for the phono3py-wte test suite.

The fixtures here mirror a subset of phono3py's ``test/conftest.py`` — only
the entries actually consumed by tests under ``tests/`` are kept.  All input
files live under ``tests/data/`` so the test suite is self-contained.

"""

from __future__ import annotations

from pathlib import Path

import phonopy
import pytest
from phonopy import Phonopy

import phono3py
from phono3py import Phono3py

_DATA = Path(__file__).parent / "data"


@pytest.fixture(scope="session")
def si_pbesol() -> Phono3py:
    """Return Phono3py instance of Si 2x2x2 (with symmetry, full fc)."""
    return phono3py.load(
        _DATA / "phono3py_si_pbesol.yaml",
        forces_fc3_filename=_DATA / "FORCES_FC3_si_pbesol",
        make_r0_average=True,
        log_level=1,
    )


@pytest.fixture(scope="session")
def si_pbesol_nosym() -> Phono3py:
    """Return Phono3py instance of Si 2x2x2 (without symmetry, no fc)."""
    return phono3py.load(
        _DATA / "phono3py_si_pbesol.yaml",
        forces_fc3_filename=_DATA / "FORCES_FC3_si_pbesol",
        is_symmetry=False,
        produce_fc=False,
        make_r0_average=True,
        log_level=1,
    )


@pytest.fixture(scope="session")
def si_pbesol_nomeshsym() -> Phono3py:
    """Return Phono3py instance of Si 2x2x2 (without mesh-symmetry, no fc)."""
    return phono3py.load(
        _DATA / "phono3py_si_pbesol.yaml",
        forces_fc3_filename=_DATA / "FORCES_FC3_si_pbesol",
        is_mesh_symmetry=False,
        produce_fc=False,
        make_r0_average=True,
        log_level=1,
    )


@pytest.fixture(scope="session")
def si_pbesol_compact_fc() -> Phono3py:
    """Return Phono3py instance of Si 2x2x2 (with symmetry, compact fc)."""
    return phono3py.load(
        _DATA / "phono3py_si_pbesol.yaml",
        forces_fc3_filename=_DATA / "FORCES_FC3_si_pbesol",
        is_compact_fc=True,
        make_r0_average=True,
        log_level=1,
    )


@pytest.fixture(scope="session")
def nacl_pbe() -> Phono3py:
    """Return Phono3py instance of NaCl 2x2x2 (with symmetry, full fc)."""
    return phono3py.load(
        _DATA / "phono3py_params_NaCl222.yaml.xz",
        make_r0_average=True,
        log_level=1,
    )


@pytest.fixture(scope="session")
def aln_lda() -> Phono3py:
    """Return Phono3py instance of AlN 3x3x2 (with symmetry, full fc)."""
    return phono3py.load(
        _DATA / "phono3py_params_AlN332.yaml.xz",
        make_r0_average=True,
        log_level=1,
    )


@pytest.fixture(scope="session")
def ph_nacl() -> Phonopy:
    """Return Phonopy instance of NaCl 2x2x2."""
    return phonopy.load(
        _DATA / "phonopy_disp_NaCl.yaml",
        force_sets_filename=_DATA / "FORCE_SETS_NaCl",
        born_filename=_DATA / "BORN_NaCl",
        is_compact_fc=False,
        log_level=1,
        produce_fc=True,
    )


@pytest.fixture(scope="session")
def ph_si() -> Phonopy:
    """Return Phonopy instance of Si-prim 2x2x2."""
    return phonopy.load(
        _DATA / "phonopy_params_Si.yaml",
        is_compact_fc=False,
        log_level=1,
        produce_fc=True,
    )
