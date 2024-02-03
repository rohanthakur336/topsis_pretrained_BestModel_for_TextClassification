import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Import result
data = pd.read_csv("topsis_result.csv")


# Display the table
print("Model Ranking Table:")
print(
    data[["MODELS", "Precision", "Recall", "F1-Score", "AUC-Score","Rank"]].sort_values(
        by="Rank"
    )
)

# Bar chart
labels = data["MODELS"]
num_models = len(labels)

# Parameters for bar chart
precision = data["Precision"]
recall = data["Recall"]
f1_score = data["F1-Score"]
auc_score = data["AUC-Score"]
rank = data["Rank"]

# Normalize ranks to a scale of 0 to 1 for better comparison
normalized_ranks = rank / np.max(rank)

# Plot the bar chart
fig, ax = plt.subplots(figsize=(10, 6))

bar_width = 0.2
index = range(num_models)

ax.bar(index,precision,width=bar_width,label="Precision")
ax.bar(index,recall,width=bar_width,label="Recall",bottom=precision,)
ax.bar(index, f1_score, width=bar_width, label="F1-Score",bottom=precision + recall,)
ax.bar(index,auc_score,width=bar_width,label="AUC-Score",bottom=precision + recall + f1_score,)
ax.bar(
    index,
    normalized_ranks,
    width=bar_width,
    label="Normalized Rank",
    color="black",
    alpha=0.5,
)

ax.set_xticks(index)
ax.set_xticklabels(labels)
ax.set_ylabel("Metrics")
ax.set_title("Text Classification Model Comparison Through Topsis")

ax.legend()
plt.savefig("BarChart.png")
plt.show()

