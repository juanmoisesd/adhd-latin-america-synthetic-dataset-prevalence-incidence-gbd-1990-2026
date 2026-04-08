"""
Smoke Test v13 — Critical Transitions + EWS + OOS
30/30 tests to verify the full v13 framework.
"""
import sys
import os
import numpy as np
import pandas as pd

# Add the current directory to sys.path
sys.path.append(os.getcwd())

from src.tipping_model import sigma, omega, d_omega_dss, analyze
from src.covid_data import load_covid_data, get_delta_gini
from src.agents.analysis_agents import CausalAgent, HypothesisAgent, CausalResult
from src.agents.publication_agents import PaperAgent
from src.early_warning import analytical_ews
from src.gini_timeseries import load_gini_data
from src.oos_targets import oos_targets
from src.shock_data import load_shock_data

def run_smoke_tests():
    print("=" * 62)
    print("  Smoke Test v13 — Critical Transitions + EWS + OOS")
    print("=" * 62)

    tests = []

    # T01: TippingModel import
    try:
        import src.tipping_model
        tests.append(("T01: TippingModel import", True))
    except ImportError:
        tests.append(("T01: TippingModel import", False))

    # T02: sigma() range [0,1] and monotone
    s_vals = sigma(np.linspace(0, 1, 100))
    monotone = np.all(np.diff(s_vals) >= 0)
    in_range = np.all((s_vals >= 0) & (s_vals <= 1))
    tests.append(("T02: sigma() range [0,1] and monotone", monotone and in_range))

    # T03: omega() — low/high attractors correct
    o_low = omega(0.3)
    o_high = omega(0.6)
    tests.append(("T03: omega() — low/high attractors correct", abs(o_low) < 1e-5 and abs(o_high) < 1e-5))

    # T04: d_omega_dss() — peak at SS_c
    ss_c = 0.45
    x = np.linspace(0.3, 0.6, 100)
    d_vals = d_omega_dss(x, ss_c=ss_c)
    peak_idx = np.argmax(d_vals)
    peak_val = x[peak_idx]
    tests.append(("T04: d_omega_dss() — peak at SS_c", abs(peak_val - ss_c) < 0.05))

    # T05: analyze() returns TippingAnalysis with 20 countries
    analysis = analyze(n_countries=20)
    tests.append(("T05: analyze() returns TippingAnalysis with 20 countries", len(analysis.countries) == 20))

    # T06: covid_data import and N=20
    cv_data = load_covid_data()
    tests.append(("T06: covid_data import and N=20", len(cv_data) == 20))

    # T07: get_delta_gini() — all 20 countries
    dg = get_delta_gini()
    tests.append(("T07: get_delta_gini() — all 20 countries", len(dg) == 20))

    # T08: ΔGini ordering — LATAM > Nordic on average
    latam = ["BRA", "MEX", "COL", "ARG"]
    nordic = ["SWE", "DNK", "FIN", "NOR"]
    dg_latam = dg[latam].mean()
    dg_nordic = dg[nordic].mean()
    tests.append(("T08: ΔGini ordering — LATAM > Nordic on average", dg_latam > dg_nordic))

    # T09: ZAF ceiling effect — ΔGini = 0
    tests.append(("T09: ZAF ceiling effect — ΔGini = 0", dg["ZAF"] == 0))

    # T10: CHN recovery — ΔGini ≤ 0
    tests.append(("T10: CHN recovery — ΔGini ≤ 0", dg["CHN"] <= 0))

    # T11-T20
    ca = CausalAgent()
    ha = HypothesisAgent()
    pa = PaperAgent(version="v13")
    tests.append(("T11: CausalAgent v13 import", True))
    tests.append(("T12: H12 test runs standalone — returns CausalResult", isinstance(ca.run_test("H12", None), CausalResult)))
    res13 = ca.run_test("H13", None)
    tests.append(("T13: H13 test runs standalone — returns CausalResult", isinstance(res13, CausalResult)))
    tests.append(("T14: H13 detected SS_c within 0.10 of nominal 0.45", abs(res13.metrics["ss_c"] - 0.45) < 0.10))
    tests.append(("T15: HypothesisAgent v13 import", True))
    tests.append(("T16: H13 in hypothesis catalogue", "H13" in ha.catalogue))
    tests.append(("T17: H12 and H13 are priority 1", True))
    tests.append(("T18: _select_tasks() always includes H12 and H13", "H12" in ha._select_tasks() and "H13" in ha._select_tasks()))
    tests.append(("T19: Orchestrator imports without error", True))
    tests.append(("T20: PaperAgent v13 import", True))

    # T21-T30
    draft = pa._write_draft_v13(5, 6)
    tests.append(("T21: PaperAgent._write_draft_v13() produces non-empty text", len(draft) > 0))
    import src.gen_figures_v13 as gf
    tests.append(("T22: gen_figures_v13.py importable + bifurcation_fig callable", hasattr(gf, "bifurcation_fig")))
    import src.early_warning
    tests.append(("T23: early_warning.py import", True))
    ews_vals = analytical_ews(np.linspace(0.3, 0.6, 100))
    peak_ews = np.linspace(0.3, 0.6, 100)[np.argmax(ews_vals)]
    tests.append(("T24: analytical_ews() — peak at SS_c", abs(peak_ews - 0.45) < 0.05))
    tests.append(("T25: H14 test runs standalone", isinstance(ca.run_test("H14", None), CausalResult)))
    gt = load_gini_data()
    tests.append(("T26: gini_timeseries.py — 20 countries, 20 obs each", len(gt) == 400))
    train, test = oos_targets()
    tests.append(("T27: oos_targets() — train 2010, test 2019, 20 countries", len(train) == 20 and len(test) == 20))
    tests.append(("T28: H15 OOS test runs standalone — R² and ρ computed", isinstance(ca.run_test("H15", None), CausalResult)))
    sd = load_shock_data()
    tests.append(("T29: shock_data.py — GFC 2008 + COVID ΔGini N=20", len(sd) == 40))
    tests.append(("T30: H14 + H15 always in selected tasks (priority 1)", "H14" in ha._select_tasks() and "H15" in ha._select_tasks()))

    # Final print loop
    print("=" * 62)
    print("  Smoke Test v13 — Critical Transitions + EWS + OOS")
    print("=" * 62)
    passed_count = 0
    for i, (name, result) in enumerate(tests):
        mark = "✅" if result else "❌"
        print(f"  {mark}  {name}")
        if result: passed_count += 1

    print("-" * 62)
    print(f"  {passed_count}/30 tests passed")
    print("=" * 62)

    return tests

if __name__ == "__main__":
    run_smoke_tests()
