import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

train_df = pd.read_excel('train.xlsx')
test_df = pd.read_excel('test.xlsx')

print(train_df.head())

features = train_df.columns.drop('target')

scaler = StandardScaler()
scaled_train_data = scaler.fit_transform(train_df[features])

kmeans = KMeans(n_clusters=3, random_state=42)
kmeans.fit(scaled_train_data)

train_df['cluster'] = kmeans.labels_

print(train_df.head())

def predict_cluster(new_data_point, scaler, kmeans, feature_names):
    new_data_df = pd.DataFrame([new_data_point], columns=feature_names)
    scaled_data_point = scaler.transform(new_data_df)
    cluster = kmeans.predict(scaled_data_point)
    return cluster[0]

test_df['cluster'] = test_df[features].apply(lambda row: predict_cluster(row.values, scaler, kmeans, features), axis=1)

print(test_df.head())

def explain_cluster(new_data_point, scaler, kmeans, feature_names):
    new_data_df = pd.DataFrame([new_data_point], columns=feature_names)
    scaled_data_point = scaler.transform(new_data_df)
    cluster = kmeans.predict(scaled_data_point)
    centroid = kmeans.cluster_centers_[cluster[0]]
    return cluster[0], centroid

new_data_point = test_df.iloc[0][features].values
cluster, centroid = explain_cluster(new_data_point, scaler, kmeans, features)

print(f'The new data point belongs to cluster: {cluster}')
print(f'The centroid of the cluster is: {centroid}')
