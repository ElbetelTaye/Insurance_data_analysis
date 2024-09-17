import pandas as pd
import numpy as np
from scipy.stats import chi2_contingency, ttest_ind
import os

# Analyze and Report
def analyze_and_report(p_value, hypothesis_name):
    if p_value < 0.05:
        result = "Reject the null hypothesis: Evidence suggests a significant effect."
    else:
        result = "Fail to reject the null hypothesis: No significant effect detected."
    return f"{hypothesis_name}: {result} (p-value: {p_value:.4f})"
