### **First Steps for the Iris Dataset Clustering Project**

#### **1. Organize Project Directory**
Given your current file structure, you should store the Iris dataset in the `datasets/mod_3_unsupervised_learning_data` folder and save your Jupyter Notebook in `deliverables/mod_3_unsupervised_learning`.

---

#### **2. Automate Dataset Download in Jupyter Notebook**
Before running clustering models, the dataset must be downloaded and checked for existence. Your notebook should:
- Check if the dataset already exists in `datasets/mod_3_unsupervised_learning_data`.
- If not, download it from the UCI Repository.
- Save it as `iris_dataset.csv`.

#### **Python Code for Downloading the Dataset**
Place this in the first cell of your Jupyter Notebook:

```python
import os
import pandas as pd
import urllib.request

# Define dataset path
dataset_dir = "datasets/mod_3_unsupervised_learning_data"
dataset_path = os.path.join(dataset_dir, "iris_dataset.csv")
iris_url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"

# Ensure dataset directory exists
os.makedirs(dataset_dir, exist_ok=True)

# Download dataset if not present
if not os.path.exists(dataset_path):
    print("Dataset not found. Downloading...")
    urllib.request.urlretrieve(iris_url, dataset_path)
    print("Download complete!")
else:
    print("Dataset already exists. Skipping download.")

# Load dataset
column_names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class']
df = pd.read_csv(dataset_path, names=column_names)

# Display first few rows
df.head()
```

---

#### **3. Data Preprocessing**
Preprocess the dataset by:
- Checking for missing values.
- Normalizing the numerical features.
- Removing the `class` column since it's unsupervised learning.

Add this in a new cell:

```python
from sklearn.preprocessing import StandardScaler

# Check for missing values
print("Missing values:\n", df.isnull().sum())

# Remove the class column (unsupervised learning)
df_features = df.drop(columns=['class'])

# Normalize the features
scaler = StandardScaler()
df_scaled = pd.DataFrame(scaler.fit_transform(df_features), columns=df_features.columns)

df_scaled.head()
```

---

#### **4. Implement Clustering**
Implement both **K-Means** and **Hierarchical Clustering**.

##### **K-Means Clustering**
- Use the **Elbow Method** to determine the optimal number of clusters.
- Fit K-Means to the dataset.

```python
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# Determine the optimal number of clusters using the Elbow Method
inertia = []
k_values = range(1, 11)

for k in k_values:
    kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
    kmeans.fit(df_scaled)
    inertia.append(kmeans.inertia_)

# Plot the Elbow Curve
plt.figure(figsize=(8,5))
plt.plot(k_values, inertia, marker='o', linestyle='-')
plt.xlabel('Number of Clusters')
plt.ylabel('Inertia')
plt.title('Elbow Method for Optimal K')
plt.show()
```

---

##### **Hierarchical Clustering**
- Generate a **dendrogram** to visualize how clusters merge.

```python
import scipy.cluster.hierarchy as sch

# Create dendrogram
plt.figure(figsize=(10, 5))
dendrogram = sch.dendrogram(sch.linkage(df_scaled, method='ward'))
plt.title('Hierarchical Clustering Dendrogram')
plt.xlabel('Data Points')
plt.ylabel('Euclidean Distance')
plt.show()
```

---

#### **5. Evaluate Clustering Quality**
Use **Silhouette Score** to evaluate clustering quality.

```python
from sklearn.metrics import silhouette_score

# Fit K-Means with the chosen number of clusters (e.g., 3 based on elbow method)
kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
df_scaled['cluster'] = kmeans.fit_predict(df_scaled)

# Compute silhouette score
sil_score = silhouette_score(df_scaled.drop(columns=['cluster']), df_scaled['cluster'])
print(f"Silhouette Score: {sil_score:.4f}")
```

---

#### **6. Visualize Clusters**
Since the dataset has 4 dimensions, reduce it to 2D using **PCA** and visualize.

```python
from sklearn.decomposition import PCA

# Reduce dimensions to 2D for visualization
pca = PCA(n_components=2)
df_pca = pd.DataFrame(pca.fit_transform(df_scaled.drop(columns=['cluster'])), columns=['PC1', 'PC2'])
df_pca['cluster'] = df_scaled['cluster']

# Plot clusters
plt.figure(figsize=(8,5))
plt.scatter(df_pca['PC1'], df_pca['PC2'], c=df_pca['cluster'], cmap='viridis', alpha=0.7)
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.title('Clustering Visualization using PCA')
plt.colorbar(label='Cluster')
plt.show()
```

---

### **Final Steps**
✅ **Ensure dataset is downloaded and loaded correctly**  
✅ **Preprocess data (normalize, remove class labels)**  
✅ **Implement clustering (K-Means and Hierarchical)**  
✅ **Evaluate clustering results using silhouette scores**  
✅ **Visualize results with PCA**

---

### **Where to Save the Work**
- **Dataset:**  
  Save `iris_dataset.csv` in `datasets/mod_3_unsupervised_learning_data/`
- **Jupyter Notebook:**  
  Save `Clustering_the_Iris_Dataset.ipynb` in `deliverables/mod_3_unsupervised_learning/`

---

Would you like additional enhancements, such as automated reporting or more visualizations? 🚀