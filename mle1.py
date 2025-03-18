import numpy as np
from scipy import special
from scipy import optimize

# Cuckoo egg data
data = np.array([22.0, 23.9, 20.9, 23.8, 25.0, 24.0, 21.7, 23.8, 22.8, 23.1, 23.1, 23.5, 23.0, 23.0])

# Calculate sample mean
x_bar = np.mean(data)
n = len(data)
sum_log_x = np.sum(np.log(data))

# Define the negative log-likelihood function for alpha (we negate because optimization functions minimize by default)
def neg_log_likelihood(alpha):
    beta = x_bar / alpha
    # Log-likelihood formula from part (a) substituting beta = x_bar / alpha
    log_lik = -n * alpha * np.log(x_bar) + n * alpha * np.log(alpha) - n * alpha + (alpha - 1) * sum_log_x - n * special.gammaln(alpha)
    return -log_lik  # Negate because we want to maximize, not minimize

# Define the derivative of the negative log-likelihood w.r.t. alpha (for faster convergence)
def neg_log_likelihood_derivative(alpha):
    # Derivative of the log-likelihood
    deriv = -n * np.log(x_bar) + n * np.log(alpha) + n + sum_log_x - n * special.digamma(alpha)
    return -deriv  # Negate because we want to maximize, not minimize

# Initial guess for alpha (can use method of moments as a starting point)
sample_var = np.var(data, ddof=1)  # Sample variance
alpha_init = (x_bar**2) / sample_var

# Optimize to find the MLE of alpha
result = optimize.minimize(neg_log_likelihood, alpha_init, jac=neg_log_likelihood_derivative, method='BFGS')

# Extract the MLE for alpha
alpha_mle = result.x[0]

# Calculate the corresponding MLE for beta
beta_mle = x_bar / alpha_mle

print(f"Sample mean: {x_bar:.5f}")
print(f"Sample variance: {sample_var:.5f}")
print(f"Initial guess (method of moments) - alpha: {alpha_init:.5f}")
print(f"MLE of alpha: {alpha_mle:.5f}")
print(f"MLE of beta: {beta_mle:.5f}")
print(f"Convergence status: {result.success}")
#result = optimize.minimize_scalar(neg_log_likelihood, bracket=[1, alpha_init, 1000])
#alpha_mle = result.x
