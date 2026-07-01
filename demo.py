import os,numpy as np,matplotlib;matplotlib.use("Agg")
import matplotlib.pyplot as plt
os.makedirs("figures",exist_ok=True);os.makedirs("results",exist_ok=True)
rng=np.random.default_rng(1);n=5000
A=rng.uniform(1,16,n)  # mean expression (log)
M=rng.normal(0,0.3+2/np.sqrt(A),n)  # noisier at low expression
idx=rng.choice(n,150,replace=False);M[idx]+=rng.choice([-1,1],150)*rng.uniform(1.5,4,150)
sig=np.abs(M)>1
plt.figure(figsize=(7,4))
plt.scatter(A[~sig],M[~sig],s=4,c="grey",alpha=.4)
plt.scatter(A[sig],M[sig],s=6,c="firebrick")
plt.axhline(0,c="k",lw=.7);plt.axhline(1,ls="--",c="k",lw=.5);plt.axhline(-1,ls="--",c="k",lw=.5)
plt.xlabel("A = mean log-expression");plt.ylabel("M = log fold change");plt.title("MA plot (demo data)")
plt.tight_layout();plt.savefig("figures/demo.png",dpi=150)
open("results/summary.txt","w").write(f"significant: {int(sig.sum())}\n");print("ok")