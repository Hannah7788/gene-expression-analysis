import pandas as pd

# Sample gene expression dataset
data = {
    "Gene": ["BRCA1", "TP53", "EGFR", "MYC", "PTEN"],
    "Expression": [5.2, 3.8, 6.1, 4.5, 2.9]
}

df = pd.DataFrame(data)

# Display dataset
print("Gene Expression Data:")
print(df)

# Basic analysis
mean_expression = df["Expression"].mean()
max_expression = df["Expression"].max()

print("\nAverage Expression:", mean_expression)
print("Highest Expression:", max_expression)
