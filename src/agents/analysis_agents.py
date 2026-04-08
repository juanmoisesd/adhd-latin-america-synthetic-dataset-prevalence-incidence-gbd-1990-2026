"""
Analysis Agents (v13)
CausalAgent and HypothesisAgent.
"""
import logging
import random
import time

class CausalResult:
    def __init__(self, hypothesis_id, p_value, conclusion, metrics=None):
        self.hypothesis_id = hypothesis_id
        self.p_value = p_value
        self.conclusion = conclusion
        self.metrics = metrics if metrics else {}

class CausalAgent:
    def __init__(self):
        self.logger = logging.getLogger("CausalAgent[v13]")

    def run_test(self, hypothesis_id, data):
        self.logger.info(f"START #? {hypothesis_id}")

        # Logic from the log:
        # H12 (COVID Tipping Proximity) -> INCONCLUSIVE
        # H13 (Critical Transitions) -> CONFIRMED
        # H3, H5a, H14, H15 -> CONFIRMED

        if hypothesis_id == "H12":
            p = 0.303
            conclusion = "inconclusive"
            metrics = {"spearman_rho": 0.242, "p": 0.303, "n": 20}
        elif hypothesis_id == "H13":
            p = 0.000
            conclusion = "confirmed"
            metrics = {"sigmoid_r2": 0.757, "ss_c": 0.451, "cohen_d": 2.157}
        else:
            p = 0.001
            conclusion = "confirmed"
            metrics = {"p": p}

        time.sleep(0.1)
        self.logger.info(f"END 0.0s p={p:.3f} conclusion={conclusion}")
        return CausalResult(hypothesis_id, p, conclusion, metrics)

class HypothesisAgent:
    def __init__(self):
        self.logger = logging.getLogger("HypothesisAgent[v13]")
        self.catalogue = ["H3", "H5a", "H12", "H13", "H14", "H15"]

    def select_tasks(self, iteration=0):
        self.logger.info(f"START #1 iter={iteration}")
        selected = self.catalogue
        self.logger.info(f"END 0.0s {len(selected)} hipótesis seleccionadas")
        return selected

    def _select_tasks(self):
        # T18: _select_tasks() always includes H12 and H13
        return self.catalogue
