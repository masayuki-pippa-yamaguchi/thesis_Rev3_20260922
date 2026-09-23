import numpy as np
import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt

np.random.seed(123)

# ---------------------------------------------------------
# Step1：真の世界のデータ生成（CSV 不要）
# ---------------------------------------------------------

N = 5000

mu_true = np.random.normal(loc=0.02, scale=0.03, size=N)
sigma_true = np.random.normal(loc=0.20, scale=0.05, size=N)
S_true = np.random.choice([0,1,2,3], size=N, p=[0.25]*4)
D_true = np.random.lognormal(mean=-1.0, sigma=0.4, size=N)

a, b, c, d = 1.0, 1.0, 0.8, 1.2

Z_true = a*mu_true - b*sigma_true + c*S_true - d*D_true
p_true = 1 / (1 + np.exp(-Z_true))
default = np.random.binomial(n=1, p=p_true, size=N)

df_true = pd.DataFrame({
    "mu_true": mu_true,
    "sigma_true": sigma_true,
    "S_true": S_true,
    "D_true": D_true,
    "default": default
})

print("Step1 完了：真の世界データ生成")
print(df_true.head())

# ---------------------------------------------------------
# Step2：代理変数（proxy）生成（CSV 不要）
# ---------------------------------------------------------

mu_proxy = mu_true + np.random.normal(0, 0.01, size=N)
sigma_proxy = sigma_true + np.random.normal(0, 0.02, size=N)
S_proxy = S_true
D_proxy = D_true * np.exp(np.random.normal(0, 0.1, size=N))

df_proxy = pd.DataFrame({
    "mu": mu_proxy,
    "sigma": sigma_proxy,
    "S": S_proxy,
    "D": D_proxy,
    "default": default
})

print("\nStep2 完了：代理変数生成")
print(df_proxy.head())

# ---------------------------------------------------------
# Step3：ロジット推定（CSV 不要）
# ---------------------------------------------------------

X = df_proxy[["mu", "sigma", "S", "D"]]
X = sm.add_constant(X)
y = df_proxy["default"]

logit_model = sm.Logit(y, X)
result = logit_model.fit(disp=False)

print("\nStep3 完了：ロジット推定結果")
print(result.summary())

# ---------------------------------------------------------
# Step4：可視化（任意）
# ---------------------------------------------------------

plt.figure(figsize=(6,4))
plt.hist(result.predict(), bins=30, alpha=0.7)
plt.title("Predicted Default Probability")
plt.xlabel("p_hat")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()
