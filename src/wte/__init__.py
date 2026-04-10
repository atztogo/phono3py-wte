"""Wigner transport equation plugin for phono3py conductivity.

This package registers the ``"WTE"`` variant with phono3py's conductivity
factory.  Registration is performed lazily via the :func:`register` function,
which is invoked by phono3py through the ``phono3py.conductivity`` entry point
declared in ``pyproject.toml``.  After installation via ``pip install
phono3py-wte``, ``conductivity_calculator("WTE-rta", ...)`` (and the LBTE
counterpart) becomes available without any explicit import.

"""

from __future__ import annotations

from phono3py.conductivity.build_components import VariantContext

from wte.kappa_solvers import WignerLBTEKappaSolver, WignerRTAKappaSolver
from wte.velocity_solvers import VelocityOperatorSolver


def _make_velocity_solver(ctx: VariantContext) -> VelocityOperatorSolver:
    return VelocityOperatorSolver(
        ctx.interaction,
        is_kappa_star=ctx.kappa_settings.is_kappa_star,
        gv_delta_q=ctx.kappa_settings.gv_delta_q,
        log_level=ctx.log_level,
    )


def _make_rta_kappa_solver(ctx: VariantContext) -> WignerRTAKappaSolver:
    frequencies, _, _ = ctx.interaction.get_phonons()
    return WignerRTAKappaSolver(
        kappa_settings=ctx.kappa_settings,
        frequencies=frequencies,
        volume=ctx.interaction.primitive.volume,
        log_level=ctx.log_level,
    )


def _make_lbte_kappa_solver(ctx: VariantContext) -> WignerLBTEKappaSolver:
    frequencies, _, _ = ctx.interaction.get_phonons()
    return WignerLBTEKappaSolver(
        solver=ctx.collision_matrix_kernel,
        kappa_settings=ctx.kappa_settings,
        frequencies=frequencies,
        volume=ctx.interaction.primitive.volume,
        is_reducible_collision_matrix=(
            ctx.kappa_settings.is_reducible_collision_matrix
        ),
        log_level=ctx.log_level,
    )


def register() -> None:
    """Register the WTE (Wigner transport equation) variant with phono3py.

    This function is the target of the ``phono3py.conductivity`` entry point
    declared in ``pyproject.toml`` and is invoked by phono3py's factory
    discovery loop.  It registers both the RTA and LBTE kappa solvers in a
    single call via :func:`phono3py.conductivity.factory.register_variant`.

    """
    from phono3py.conductivity.factory import register_variant

    register_variant(
        "WTE",
        make_velocity_solver=_make_velocity_solver,
        make_rta_kappa_solver=_make_rta_kappa_solver,
        make_lbte_kappa_solver=_make_lbte_kappa_solver,
    )
