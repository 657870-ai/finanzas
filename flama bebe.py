from scipy import stats

# Apple Inc.

AAPL = [77.706920, 29.711906]

# Microsoft Corporation

MFST = [48, -1.454]

beta, alpha, r_value, p_value, std_err = stats.linregress(AAPL, MFST)