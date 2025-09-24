# -------------------------------
# Import required libraries
# -------------------------------
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

# -------------------------------
# Task 1: Load and Explore Dataset
# -------------------------------

try:
    # Load Iris dataset (from sklearn)
    iris = load_iris(as_frame=True)
    df = iris.frame  # Convert to Pandas DataFrame

    print("✅ Dataset loaded successfully!\n")

    # Display first few rows
    print("First 5 rows of dataset:")
    print(df.head(), "\n")

    # Check structure (data types)
    print("Dataset Info:")
    print(df.info(), "\n")

    # Check for missing values
    print("Missing values per column:")
    print(df.isnull().sum(), "\n")

    # Clean dataset (Iris has no missing values, but we demonstrate)
    df = df.dropna()

except FileNotFoundError:
    print("❌ Error: Dataset not found. Please check file path.")
except Exception as e:
    print("❌ Unexpected error:", e)

# -------------------------------
# Task 2: Basic Data Analysis
# -------------------------------

# Descriptive statistics of numerical columns
print("Descriptive Statistics:")
print(df.describe(), "\n")

# Group by categorical column (species) and compute mean values
print("Mean values grouped by species (target column):")
print(df.groupby("target").mean(), "\n")

# Observations / patterns
print("Observations:")
print("- Setosa (0) has much smaller petals compared to Virginica (2).")
print("- Sepal measurements overlap more than petal measurements.\n")

# -------------------------------
# Task 3: Data Visualization
# -------------------------------

# 1. Line Chart: Petal Length across samples
plt.figure(figsize=(8,5))
plt.plot(df.index, df["petal length (cm)"], label="Petal Length", color="blue")
plt.title("Line Chart: Petal Length across Samples")
plt.xlabel("Sample Index")
plt.ylabel("Petal Length (cm)")
plt.legend()
plt.show()

# 2. Bar Chart: Average Petal Length per Species
plt.figure(figsize=(8,5))
sns.barplot(x="target", y="petal length (cm)", data=df, ci=None, palette="viridis")
plt.title("Bar Chart: Avg Petal Length per Species")
plt.xlabel("Species (0=Setosa, 1=Versicolor, 2=Virginica)")
plt.ylabel("Average Petal Length (cm)")
plt.show()

# 3. Histogram: Sepal Length Distribution
plt.figure(figsize=(8,5))
plt.hist(df["sepal length (cm)"], bins=20, color="skyblue", edgecolor="black")
plt.title("Histogram: Sepal Length Distribution")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Frequency")
plt.show()

# 4. Scatter Plot: Sepal vs Petal Length
plt.figure(figsize=(8,5))
sns.scatterplot(x="sepal length (cm)", y="petal length (cm)",
                hue="target", data=df, palette="Set1")
plt.title("Scatter Plot: Sepal vs Petal Length")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Petal Length (cm)")
plt.legend(title="Species")
plt.show()

# -------------------------------
# Final Findings
# -------------------------------
print("📌 Final Findings:")
print("1. Setosa has the smallest petals; Virginica has the largest.")
print("2. Sepal length distribution is roughly normal.")
print("3. Petal length shows clear separation between species.")
print("4. Sepal length and petal length are positively correlated.\n")

print("✅ Analysis complete.")

