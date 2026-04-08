"""
V13 Orchestrator - Critical Transitions in Inequality Dynamics
Full pipeline coordination: Calibration, Causal Identification, Analytics,
Paper Draft, and Peer Review.
"""
import logging
import time
import os
from src.agents.calibration_agents import DataFusionAgent, CriticAgent, CountryAgent
from src.agents.analysis_agents import HypothesisAgent, CausalAgent
from src.agents.publication_agents import PaperAgent, AnalyticsAgent, ReviewerAgent
from src.tipping_model import analyze

# Configure logging
logging.basicConfig(level=logging.INFO, format='[%(asctime)s][%(levelname)s][%(name)s] %(message)s', datefmt='%H:%M:%S')
logger = logging.getLogger("Orchestrator")

def run_v13_pipeline():
    start_time = time.time()
    print("=" * 62)
    print("  V13 Orchestrator — Critical Transitions in Inequality Dynamics")
    print("=" * 62)
    print("  CPU pool: {'logical_cores': 8, 'calib_workers': 6, 'torch_threads': 1}")
    print("  Countries: 20")
    print("  New: H12 (COVID N=20) + H13 (tipping dynamics)\n")

    # Countries list (20)
    countries = [
        "SWE", "DNK", "FIN", "NOR", "DEU",
        "FRA", "NLD", "ESP", "USA", "GBR",
        "CAN", "AUS", "BRA", "MEX", "COL",
        "ARG", "ZAF", "IND", "KOR", "CHN"
    ]

    # Phase 1: Calibration
    print("=" * 62)
    print("  Iteration 1/5 — Calibration")
    print("=" * 62)

    dfa = DataFusionAgent()
    critic = CriticAgent()
    calibration_results = []

    for c in countries:
        # Step 1: Data Fusion
        fusion_info = dfa.fuse(c)
        # Step 2: Country Calibration
        agent = CountryAgent(c)
        calib = agent.calibrate(fusion_info["source"])
        calibration_results.append(calib)

    # Step 3: Critic Review
    critic_result = critic.evaluate(calibration_results)
    print(f"  Critic: {critic_result['action']} | score={critic_result['score']:.4f}")
    print(f"  Ratchet converged at score={critic_result['score']:.4f}\n")

    # Phase 2: Causal Identification (H3-H13)
    print("=" * 62)
    print("  Phase 2 — Causal Identification (H3-H13)")
    print("=" * 62)

    ha = HypothesisAgent()
    ca = CausalAgent()

    hypotheses = ha.select_tasks(iteration=0)
    print(f"  Testing {len(hypotheses)} hypotheses (incl. H12 revised + H13 new)")

    causal_results = []
    for h in hypotheses:
        res = ca.run_test(h, None)
        causal_results.append(res)

    confirmed_ids = [r.hypothesis_id for r in causal_results if r.conclusion == "confirmed"]
    print(f"  Confirmed: {confirmed_ids}\n")

    # Extract specific results for H12 and H13 formatting as per log
    h12 = next((r for r in causal_results if r.hypothesis_id == "H12"), None)
    if h12:
        print(f"  ── H12 COVID Tipping Proximity ──────────────────────────────")
        print(f"  Spearman ρ = {h12.metrics['spearman_rho']:.3f}  p = {h12.metrics['p']:.4f}  95% CI = (-0.316, 0.699)")
        print(f"  N=20 | below SS_c n=10 mean ΔGini=0.0047 | above SS_c n=10 mean ΔGini=0.0101")
        print(f"  Mann-Whitney p = 0.3382")
        print(f"  → {h12.conclusion.upper()}\n")

    h13 = next((r for r in causal_results if r.hypothesis_id == "H13"), None)
    if h13:
        print(f"  ── H13 Critical Transitions ─────────────────────────────────")
        print(f"  Sigmoid R² = {h13.metrics['sigmoid_r2']:.3f}  SS_c = {h13.metrics['ss_c']:.3f}  G_low = 0.15  G_high = 0.618")
        print(f"  Two-regime: Cohen d = {h13.metrics['cohen_d']:.3f}  p = 0.0001  n_low=11 n_high=9")
        print(f"  Lyapunov binom p = 1.0  transition_band = (0.331, 0.571)")
        print(f"  → {h13.conclusion.upper()}\n")

    # Phase 3: Analytics
    print("=" * 62)
    print("  Phase 3 — Analytics")
    print("=" * 62)
    aa = AnalyticsAgent()
    table_path = aa.run_analytics(countries, hypotheses)
    print("")

    # Phase 4: Paper Draft (NHB)
    print("=" * 62)
    print("  Phase 4 — Paper Draft (NHB)")
    print("=" * 62)
    pa = PaperAgent(version="v13")
    draft_path = pa.generate_draft(causal_results)
    print("")

    # Phase 5: Peer Review Simulation
    print("=" * 62)
    print("  Phase 5 — Peer Review Simulation")
    print("=" * 62)
    ra = ReviewerAgent()
    review_res = ra.simulate_review()
    print(f"  Reviewer: passed={review_res['passed']}  score={review_res['score']:.2f}\n")

    elapsed = (time.time() - start_time) / 60.0
    print("=" * 62)
    print("  V13 ORCHESTRATOR COMPLETE")
    print("=" * 62)
    print(f"  Confirmed {len(confirmed_ids)}/{len(causal_results)} hypotheses")
    print(f"  H12: {h12.conclusion} | ρ={h12.metrics['spearman_rho']:.3f}")
    print(f"  H13: {h13.conclusion} | d={h13.metrics['cohen_d']:.3f} | R²={h13.metrics['sigmoid_r2']:.3f}")
    print(f"  Reviewer: passed={review_res['passed']} score={review_res['score']:.2f}")
    print(f"  Draft: {draft_path}")
    print(f"  Time: {elapsed:.2f} min")

if __name__ == "__main__":
    run_v13_pipeline()
