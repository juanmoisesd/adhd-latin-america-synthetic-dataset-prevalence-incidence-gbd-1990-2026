"""
Figure Generator (v13)
Generate bifurcation figures for the Gini tipping model.
"""
import matplotlib.pyplot as plt
import numpy as np

def bifurcation_fig(save_path="results/figures/bifurcation_fig.png"):
    """
    Generate and save a bifurcation diagram.
    Shows low/high attractors and the transition threshold.
    """
    x = np.linspace(0.2, 0.7, 100)
    # Just a conceptual visualization
    y = (x - 0.3) * (x - 0.45) * (x - 0.6)

    plt.figure(figsize=(10, 6))
    plt.plot(x, y, label="Flow Rate")
    plt.axhline(0, color='black', lw=0.5)
    plt.axvline(0.45, color='red', ls='--', label="Tipping Point (SS_c)")
    plt.plot([0.3, 0.6], [0, 0], 'bo', label="Attractors")

    plt.title("Bifurcation Diagram (Conceptual)", fontsize=14)
    plt.xlabel("Gini Index")
    plt.ylabel("dGini/dt")
    plt.legend()
    plt.grid(True, alpha=0.3)

    plt.savefig(save_path)
    plt.close()
    return save_path

if __name__ == "__main__":
    bifurcation_fig()
