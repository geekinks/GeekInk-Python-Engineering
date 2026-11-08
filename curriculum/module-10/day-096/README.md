# Day 096: Unsupervised Learning

## Learning Objectives

- Understand unsupervised learning and how it differs from supervised learning.
- Use KMeans clustering to group data points without labels.
- Choose an appropriate number of clusters using the elbow method.
- Apply PCA for dimensionality reduction and visualization.
- Interpret clustering results to derive meaningful insights.

## Introduction

In supervised learning, every data point in your training set has a label: this student passed, this house costs 5 million naira. Unsupervised learning works with data that has no labels. The algorithm's job is to find structure, patterns, or groupings in the data on its own.

The most common unsupervised learning technique is clustering: dividing data points into groups where members of each group are similar to each other and different from members of other groups. Think of sorting a box of unsorted objects: you might group them by color, size, shape, or some combination. KMeans is the most widely used clustering algorithm. You tell it how many clusters you want, and it finds the best way to divide the data into that many groups.

Another important technique is dimensionality reduction. Real-world datasets often have many features. PCA (Principal Component Analysis) reduces the number of features while preserving as much information as possible. This is useful for visualization (plotting high-dimensional data in 2D) and for improving model performance by removing noise.

## Concepts

### KMeans Clustering

KMeans works by:
1. Randomly placing K cluster centers.
2. Assigning each data point to its nearest center.
3. Moving each center to the average position of its assigned points.
4. Repeating steps 2-3 until centers stop moving.

### The Elbow Method

How do you choose K (the number of clusters)? Plot the "inertia" (sum of squared distances from each point to its cluster center) for different values of K. The inertia always decreases as K increases, but at some point the improvement slows down sharply --- this "elbow" is a good choice for K.

### PCA (Principal Component Analysis)

PCA finds the directions in the data that capture the most variation. By projecting data onto the top 2 or 3 directions, you can visualize high-dimensional data in a plot.

## Practical Examples

### KMeans clustering on customer data

```python
import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Generate customer data
np.random.seed(42)

# Three natural groups of customers
group1 = np.random.normal([30, 25000, 2], [5, 5000, 1], (60, 3))   # Young, low income
group2 = np.random.normal([45, 75000, 8], [8, 15000, 2], (50, 3))  # Middle-aged, high income
group3 = np.random.normal([55, 40000, 5], [7, 10000, 2], (40, 3))  # Older, moderate income

data = np.vstack([group1, group2, group3])
df = pd.DataFrame(data, columns=["age", "income", "purchases_per_month"])

print("Dataset shape:", df.shape)
print(df.describe())

# Scale the features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(df)

# Fit KMeans with 3 clusters
kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
df["cluster"] = kmeans.fit_predict(X_scaled)

# Analyze clusters
print("\nCluster Centers (original scale):")
centers = scaler.inverse_transform(kmeans.cluster_centers_)
for i, center in enumerate(centers):
    print(f"  Cluster {i}: Age={center[0]:.0f}, "
          f"Income={center[1]:,.0f}, "
          f"Purchases={center[2]:.1f}")

print("\nCluster Sizes:")
print(df["cluster"].value_counts().sort_index())

print("\nCluster Profiles:")
for cluster_id in sorted(df["cluster"].unique()):
    subset = df[df["cluster"] == cluster_id]
    print(f"\n  Cluster {cluster_id} ({len(subset)} customers):")
    print(f"    Avg Age: {subset['age'].mean():.0f}")
    print(f"    Avg Income: {subset['income'].mean():,.0f}")
    print(f"    Avg Purchases: {subset['purchases_per_month'].mean():.1f}")
```

### The elbow method

```python
from sklearn.cluster import KMeans

inertias = []
K_range = range(1, 11)

for k in K_range:
    km = KMeans(n_clusters=k, random_state=42, n_init=10)
    km.fit(X_scaled)
    inertias.append(km.inertia_)

print("K vs Inertia:")
for k, inertia in zip(K_range, inertias):
    bar = "#" * int(inertia / max(inertias) * 40)
    print(f"  K={k:2d}  Inertia={inertia:8.1f}  {bar}")

# Look for the "elbow" --- where the decrease in inertia slows significantly
```

### PCA for visualization

```python
from sklearn.decomposition import PCA

# Reduce to 2 dimensions for visualization
pca = PCA(n_components=2)
X_2d = pca.fit_transform(X_scaled)

print(f"\nPCA explained variance: {pca.explained_variance_ratio_}")
print(f"Total variance captured: {sum(pca.explained_variance_ratio_):.2%}")

# Show the 2D coordinates with cluster labels
viz_df = pd.DataFrame({
    "PC1": X_2d[:, 0],
    "PC2": X_2d[:, 1],
    "cluster": df["cluster"],
})

print("\nFirst 10 data points in 2D PCA space:")
print(viz_df.head(10).to_string(index=False))

# Show how well-separated the clusters are in 2D
for c in sorted(viz_df["cluster"].unique()):
    subset = viz_df[viz_df["cluster"] == c]
    print(f"\nCluster {c}: PC1 mean={subset['PC1'].mean():.2f}, "
          f"PC2 mean={subset['PC2'].mean():.2f}")
```

## Guided Practice

1. Run the KMeans customer clustering example.

2. Run the elbow method. At which K value does the elbow appear?

3. Try K=2 and K=5 instead of K=3. How do the cluster profiles change?

4. Run PCA and observe:
   - How much variance do the first 2 components capture?
   - Are the clusters well-separated in 2D PCA space?

5. Try adding a fourth feature (e.g., `years_as_customer`). Does PCA still capture most variance in 2 components?

## Daily Challenge

Cluster student performance data to identify natural groupings of students.

### Step 1: Create the dataset

```python
import numpy as np
import pandas as pd

np.random.seed(42)
n = 300

# Generate 3 natural student groups
# High performers
hp = np.random.normal(
    [8, 90, 9, 85, 3.5],
    [1.5, 5, 1, 5, 0.3],
    (100, 5)
)
# Average performers
ap = np.random.normal(
    [5, 70, 6, 65, 2.5],
    [1.5, 8, 2, 8, 0.4],
    (120, 5)
)
# At-risk students
ar = np.random.normal(
    [2, 50, 3, 45, 1.8],
    [1, 10, 1.5, 10, 0.5],
    (80, 5)
)

data = np.vstack([hp, ap, ar])
np.random.shuffle(data)

df = pd.DataFrame(data, columns=[
    "study_hours", "attendance_pct", "assignments_completed",
    "test_average", "gpa"
])

# Clip values to realistic ranges
df["study_hours"] = df["study_hours"].clip(0, 15)
df["attendance_pct"] = df["attendance_pct"].clip(0, 100)
df["assignments_completed"] = df["assignments_completed"].clip(0, 10).round()
df["test_average"] = df["test_average"].clip(0, 100)
df["gpa"] = df["gpa"].clip(0, 4.0).round(2)
```

### Step 2: Cluster the students

1. Scale the features using StandardScaler.
2. Run the elbow method for K=1 through K=8. Identify the best K.
3. Run KMeans with the best K.
4. Profile each cluster: print the average of each feature per cluster.
5. Assign meaningful labels to each cluster (e.g., "High Performers", "Average", "At Risk").

### Step 3: PCA visualization

1. Reduce to 2 dimensions with PCA.
2. Report the explained variance ratio.
3. Print cluster positions in PCA space.

### Step 4: Analysis

Write answers to:
- How many natural groups exist in the data?
- What distinguishes each group?
- If you were a school administrator, how would you use these clusters to improve student outcomes?
- Which feature contributes most to separating the clusters?

## Expected Output

```
=== Elbow Method ===
K=1  Inertia=1500.0  ########################################
K=2  Inertia=900.0   ########################
K=3  Inertia=450.0   ############
K=4  Inertia=420.0   ###########
K=5  Inertia=400.0   ##########

Best K: 3

=== Cluster Profiles ===
Cluster 0 (High Performers, 98 students):
  Study Hours: 8.1, Attendance: 90.2%, GPA: 3.5

Cluster 1 (Average, 118 students):
  Study Hours: 5.0, Attendance: 70.3%, GPA: 2.5

Cluster 2 (At Risk, 84 students):
  Study Hours: 2.1, Attendance: 49.8%, GPA: 1.8

=== PCA ===
Variance captured: 75.3% (2 components)
```

## Assessment

1. What is the fundamental difference between supervised and unsupervised learning?
2. How does the elbow method help you choose the number of clusters?
3. What does PCA do, and why is it useful for high-dimensional data?

## Submission Instructions

Submit your solution to: `task/students/your-github-username/module-10/day-096/`

Include:
- `student_clustering.py`
- `analysis.txt`

## Additional Resources

- [scikit-learn Clustering](https://scikit-learn.org/stable/modules/clustering.html)
- [scikit-learn PCA](https://scikit-learn.org/stable/modules/decomposition.html#pca)

## Reflection

- Can you think of a situation in your community where clustering could reveal useful patterns in data?
- How would you explain the concept of clustering to someone who has never heard of machine learning?
