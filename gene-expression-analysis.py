import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Ensure interactive plotting works in VS Code
plt.ion()

# Generate synthetic gene expression data
np.random.seed(42)
num_samples = 100
cell_types = ["Neuron", "Astrocyte", "Microglia", "Oligodendrocyte", "Endothelial"]
data = {cell: np.random.uniform(0, 10, num_samples) for cell in cell_types}
df = pd.DataFrame(data)

# Save data for Power BI analysis
df.to_csv("gene_expression_data.csv", index=False)

# Display summary statistics
print("\n📊 Summary statistics:\n", df.describe())

# 🔥 1️⃣ Heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(df.corr(), annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Gene Expression Heatmap")
plt.savefig("gene_expression_heatmap.png", dpi=300, bbox_inches="tight")
plt.show()  

# 📦 2️⃣ Boxplot
plt.figure(figsize=(8, 6))
sns.boxplot(data=df)
plt.title("Gene Expression Boxplot")
plt.savefig("gene_expression_boxplot.png", dpi=300, bbox_inches="tight")
plt.show()

# 🎯 3️⃣ Scatterplot (Neuron vs Astrocyte)
plt.figure(figsize=(8, 6))
sns.scatterplot(x=df["Neuron"], y=df["Astrocyte"])
plt.xlabel("Neuron Expression")
plt.ylabel("Astrocyte Expression")
plt.title("Neuron vs Astrocyte Expression")
plt.savefig("gene_expression_scatterplot.png", dpi=300, bbox_inches="tight")
plt.show()

print("\n✅ Data generation and visualization complete.")
print("\n📁 Files generated:")
print("1️⃣ gene_expression_heatmap.png")
print("2️⃣ gene_expression_boxplot.png")
print("3️⃣ gene_expression_scatterplot.png")
print("4️⃣ gene_expression_data.csv (for Power BI)")
