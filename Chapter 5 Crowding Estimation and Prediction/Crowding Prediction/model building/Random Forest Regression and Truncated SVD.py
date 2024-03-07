#!/usr/bin/env python
# coding: utf-8

# In[28]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score
from sklearn.metrics import mean_squared_error


# In[29]:


df_train = pd.read_csv('used training data.csv')
df_test = pd.read_csv('used testing data.csv')


# In[30]:


df_train.head()


# In[31]:


df_train.columns


# In[32]:


trainY = df_train['Td']
trainX = df_train[['T1', 'T2', 'T3', 'T4', 'T5', 'T6', 'T7', 'B1', 'B2', 'B3', 'B4',
       'B5', 'B6', 'B7', 'B8', 'B9', 'B10', 'B11', 'B12', 'B13', 'B14', 'B15',
       'B16', 'B17', 'B18', 'B19', 'B20', 'B21', 'B22', 'B23', 'B24', 'B25',
       'B26', 'B27', 'B28', 'B29', 'A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7',
       'A8', 'A9', 'A10', 'A11', 'A12', 'A13', 'A14', 'A15', 'A16', 'A17',
       'A18', 'A19', 'A20', 'A21', 'A22', 'A23', 'A24', 'A25', 'A26', 'A27',
       'A28', 'A29', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday',
       'Saturday', 'Sunday']]
testY = df_test['Td']
testX = df_test[['T1', 'T2', 'T3', 'T4', 'T5', 'T6', 'T7', 'B1', 'B2', 'B3', 'B4',
       'B5', 'B6', 'B7', 'B8', 'B9', 'B10', 'B11', 'B12', 'B13', 'B14', 'B15',
       'B16', 'B17', 'B18', 'B19', 'B20', 'B21', 'B22', 'B23', 'B24', 'B25',
       'B26', 'B27', 'B28', 'B29', 'A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7',
       'A8', 'A9', 'A10', 'A11', 'A12', 'A13', 'A14', 'A15', 'A16', 'A17',
       'A18', 'A19', 'A20', 'A21', 'A22', 'A23', 'A24', 'A25', 'A26', 'A27',
       'A28', 'A29', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday',
       'Saturday', 'Sunday']]


# In[33]:


from sklearn.decomposition import PCA
pca = PCA()
data_onehot = pca.fit_transform(trainX)


# In[34]:


plt.plot(range(0,trainX.shape[1]),np.cumsum(pca.explained_variance_ratio_),label = 'Cumulative variance explained')
plt.plot(range(0,trainX.shape[1]),0.9*np.ones(trainX.shape[1]),'--r',label = '90 percent variance line')
plt.title('Explained variance vs number of features')
plt.xlabel('Explained variance')
plt.ylabel('Number of features')
plt.legend()
plt.plot()


# In[35]:


from sklearn.decomposition import PCA
pca = PCA(n_components=10)
trainX = pca.fit_transform(trainX)
testX = pca.transform(testX)


# In[36]:


print(pca.explained_variance_ratio_.shape)


# In[37]:


from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
model = LinearDiscriminantAnalysis()
model.fit(trainX,trainY)
print (mean_squared_error(trainY,model.predict(trainX)))
print(mean_squared_error(trainY,model.predict(trainX)))
print(r2_score(testY,model.predict(testX)))
print(r2_score(testY,model.predict(testX)))
plt.plot(range(0,trainY.shape[0]),model.predict(trainX))
plt.plot(range(0,trainY.shape[0]),trainY)
plt.show()
plt.plot(range(0,testY.shape[0]),model.predict(testX))
plt.plot(range(0,testY.shape[0]),testY)
plt.show()


# In[38]:


from sklearn.ensemble import RandomForestRegressor
model = RandomForestRegressor(n_estimators=33,min_samples_split=97,max_depth = 5)
model.fit(trainX,trainY)
print (mean_squared_error(trainY,model.predict(trainX)))
print(mean_squared_error(testY,model.predict(testX)))
print(r2_score(trainY,model.predict(trainX)))
print(r2_score(testY,model.predict(testX)))
print('Training data plot')
plt.plot(range(0,trainY.shape[0]),model.predict(trainX))
plt.show()
plt.plot(range(0,trainY.shape[0]),trainY)
plt.show()
print('Testing data plot')
plt.plot(range(0,testY.shape[0]),model.predict(testX))
plt.show()
plt.plot(range(0,testY.shape[0]),testY)
plt.show()


# In[39]:


sum(trainX==testX)


# In[40]:


from sklearn.neural_network import MLPRegressor
model  = MLPRegressor(hidden_layer_sizes=(3,5,2),random_state=1234,solver='adam',activation='relu',max_iter=2000)
model.fit(trainX,trainY)
print (mean_squared_error(trainY,model.predict(trainX)))
print(mean_squared_error(testY,model.predict(testX)))
print(r2_score(trainY,model.predict(trainX)))
print(r2_score(testY,model.predict(testX)))
print('Training data plot')
plt.plot(range(0,trainY.shape[0]),model.predict(trainX))
plt.show()
plt.plot(range(0,trainY.shape[0]),trainY)
plt.show()
print('Testing data plot')
plt.plot(range(0,testY.shape[0]),model.predict(testX))
plt.show()
plt.plot(range(0,testY.shape[0]),testY)
plt.show()


# In[41]:


from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(trainX,trainY)
print (mean_squared_error(trainY,model.predict(trainX)))
print(mean_squared_error(testY,model.predict(testX)))
print(r2_score(trainY,model.predict(trainX)))
print(r2_score(testY,model.predict(testX)))
print('Training data plot')
plt.plot(range(0,trainY.shape[0]),model.predict(trainX))
plt.show()
plt.plot(range(0,trainY.shape[0]),trainY)
plt.show()
print('Testing data plot')
plt.plot(range(0,testY.shape[0]),model.predict(testX))
plt.show()
plt.plot(range(0,testY.shape[0]),testY)
plt.show()


# In[42]:


from sklearn.decomposition import PCA

a = []
model = RandomForestRegressor(n_estimators=33,min_samples_split=97,max_depth = 5)
for i in range(1,70):
    trainY = df_train['Td']
    trainX = df_train[['T1', 'T2', 'T3', 'T4', 'T5', 'T6', 'T7', 'B1', 'B2', 'B3', 'B4',
           'B5', 'B6', 'B7', 'B8', 'B9', 'B10', 'B11', 'B12', 'B13', 'B14', 'B15',
           'B16', 'B17', 'B18', 'B19', 'B20', 'B21', 'B22', 'B23', 'B24', 'B25',
           'B26', 'B27', 'B28', 'B29', 'A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7',
           'A8', 'A9', 'A10', 'A11', 'A12', 'A13', 'A14', 'A15', 'A16', 'A17',
           'A18', 'A19', 'A20', 'A21', 'A22', 'A23', 'A24', 'A25', 'A26', 'A27',
           'A28', 'A29', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday',
           'Saturday', 'Sunday']]
    testY = df_test['Td']
    testX = df_test[['T1', 'T2', 'T3', 'T4', 'T5', 'T6', 'T7', 'B1', 'B2', 'B3', 'B4',
           'B5', 'B6', 'B7', 'B8', 'B9', 'B10', 'B11', 'B12', 'B13', 'B14', 'B15',
           'B16', 'B17', 'B18', 'B19', 'B20', 'B21', 'B22', 'B23', 'B24', 'B25',
           'B26', 'B27', 'B28', 'B29', 'A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7',
           'A8', 'A9', 'A10', 'A11', 'A12', 'A13', 'A14', 'A15', 'A16', 'A17',
           'A18', 'A19', 'A20', 'A21', 'A22', 'A23', 'A24', 'A25', 'A26', 'A27',
           'A28', 'A29', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday',
           'Saturday', 'Sunday']]
    pca = PCA(n_components=i)
    trainX = pca.fit_transform(trainX)
    testX = pca.transform(testX)
    model.fit(trainX,trainY)
    print('no. of features = ',i)
    print (mean_squared_error(trainY,model.predict(trainX)))
    print(mean_squared_error(testY,model.predict(testX)))
    print(r2_score(trainY,model.predict(trainX)))
    print(r2_score(testY,model.predict(testX)))
    print('**********************************')
    a.append([mean_squared_error(trainY,model.predict(trainX)),mean_squared_error(testY,model.predict(testX)),
             r2_score(trainY,model.predict(trainX)),r2_score(testY,model.predict(testX))])
a = np.array(a)


# In[43]:


plt.plot(range(69),a[:,0],label = 'mse for train')
plt.plot(range(69),a[:,1],label = 'mse for test')
plt.legend()
plt.show()
plt.plot(range(69),a[:,2],label = 'r2_score for train')
plt.plot(range(69),a[:,3],label = 'r2_score for test')
plt.legend()
plt.show()


# In[44]:


### best model
print('no of features = ',np.argmin(a[:,1])+1)
print('mse for train = ',a[np.argmin(a[:,1])][0])
print('mse for test = ',a[np.argmin(a[:,1])][1])
print('r2_score for train = ',a[np.argmin(a[:,1])][2])
print('r2_score for test = ',a[np.argmin(a[:,1])][3])


# In[45]:


from sklearn.decomposition import PCA

a = []
model = LinearRegression()
for i in range(1,70):
    trainY = df_train['Td']
    trainX = df_train[['T1', 'T2', 'T3', 'T4', 'T5', 'T6', 'T7', 'B1', 'B2', 'B3', 'B4',
           'B5', 'B6', 'B7', 'B8', 'B9', 'B10', 'B11', 'B12', 'B13', 'B14', 'B15',
           'B16', 'B17', 'B18', 'B19', 'B20', 'B21', 'B22', 'B23', 'B24', 'B25',
           'B26', 'B27', 'B28', 'B29', 'A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7',
           'A8', 'A9', 'A10', 'A11', 'A12', 'A13', 'A14', 'A15', 'A16', 'A17',
           'A18', 'A19', 'A20', 'A21', 'A22', 'A23', 'A24', 'A25', 'A26', 'A27',
           'A28', 'A29', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday',
           'Saturday', 'Sunday']]
    testY = df_test['Td']
    testX = df_test[['T1', 'T2', 'T3', 'T4', 'T5', 'T6', 'T7', 'B1', 'B2', 'B3', 'B4',
           'B5', 'B6', 'B7', 'B8', 'B9', 'B10', 'B11', 'B12', 'B13', 'B14', 'B15',
           'B16', 'B17', 'B18', 'B19', 'B20', 'B21', 'B22', 'B23', 'B24', 'B25',
           'B26', 'B27', 'B28', 'B29', 'A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7',
           'A8', 'A9', 'A10', 'A11', 'A12', 'A13', 'A14', 'A15', 'A16', 'A17',
           'A18', 'A19', 'A20', 'A21', 'A22', 'A23', 'A24', 'A25', 'A26', 'A27',
           'A28', 'A29', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday',
           'Saturday', 'Sunday']]
    pca = PCA(n_components=i)
    trainX = pca.fit_transform(trainX)
    testX = pca.transform(testX)
    model.fit(trainX,trainY)
    print('no. of features = ',i)
    print (mean_squared_error(trainY,model.predict(trainX)))
    print(mean_squared_error(testY,model.predict(testX)))
    print(r2_score(trainY,model.predict(trainX)))
    print(r2_score(testY,model.predict(testX)))
    print('**********************************')
    a.append([mean_squared_error(trainY,model.predict(trainX)),mean_squared_error(testY,model.predict(testX)),
             r2_score(trainY,model.predict(trainX)),r2_score(testY,model.predict(testX))])
a = np.array(a)


# In[46]:


plt.plot(range(69),a[:,0],label = 'mse for train')
plt.plot(range(69),a[:,1],label = 'mse for test')
plt.legend()
plt.show()
plt.plot(range(69),a[:,2],label = 'r2_score for train')
plt.plot(range(69),a[:,3],label = 'r2_score for test')
plt.legend()
plt.show()


# In[47]:


### best model
print('no of features = ',np.argmin(a[:,1])+1)
print('mse for train = ',a[np.argmin(a[:,1])][0])
print('mse for test = ',a[np.argmin(a[:,1])][1])
print('r2_score for train = ',a[np.argmin(a[:,1])][2])
print('r2_score for test = ',a[np.argmin(a[:,1])][3])


# In[48]:


from sklearn.decomposition import TruncatedSVD

a = []
model = LinearRegression()
for i in range(1,70):
    trainY = df_train['Td']
    trainX = df_train[['T1', 'T2', 'T3', 'T4', 'T5', 'T6', 'T7', 'B1', 'B2', 'B3', 'B4',
           'B5', 'B6', 'B7', 'B8', 'B9', 'B10', 'B11', 'B12', 'B13', 'B14', 'B15',
           'B16', 'B17', 'B18', 'B19', 'B20', 'B21', 'B22', 'B23', 'B24', 'B25',
           'B26', 'B27', 'B28', 'B29', 'A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7',
           'A8', 'A9', 'A10', 'A11', 'A12', 'A13', 'A14', 'A15', 'A16', 'A17',
           'A18', 'A19', 'A20', 'A21', 'A22', 'A23', 'A24', 'A25', 'A26', 'A27',
           'A28', 'A29', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday',
           'Saturday', 'Sunday']]
    testY = df_test['Td']
    testX = df_test[['T1', 'T2', 'T3', 'T4', 'T5', 'T6', 'T7', 'B1', 'B2', 'B3', 'B4',
           'B5', 'B6', 'B7', 'B8', 'B9', 'B10', 'B11', 'B12', 'B13', 'B14', 'B15',
           'B16', 'B17', 'B18', 'B19', 'B20', 'B21', 'B22', 'B23', 'B24', 'B25',
           'B26', 'B27', 'B28', 'B29', 'A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7',
           'A8', 'A9', 'A10', 'A11', 'A12', 'A13', 'A14', 'A15', 'A16', 'A17',
           'A18', 'A19', 'A20', 'A21', 'A22', 'A23', 'A24', 'A25', 'A26', 'A27',
           'A28', 'A29', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday',
           'Saturday', 'Sunday']]
    pca = TruncatedSVD(n_components=i)
    trainX = pca.fit_transform(trainX)
    testX = pca.transform(testX)
    model.fit(trainX,trainY)
    print('no. of features = ',i)
    print (mean_squared_error(trainY,model.predict(trainX)))
    print(mean_squared_error(testY,model.predict(testX)))
    print(r2_score(trainY,model.predict(trainX)))
    print(r2_score(testY,model.predict(testX)))
    print('**********************************')
    a.append([mean_squared_error(trainY,model.predict(trainX)),mean_squared_error(testY,model.predict(testX)),
             r2_score(trainY,model.predict(trainX)),r2_score(testY,model.predict(testX))])
a = np.array(a)


# In[49]:


plt.plot(range(69),a[:,0],label = 'mse for train')
plt.plot(range(69),a[:,1],label = 'mse for test')
plt.legend()
plt.show()
plt.plot(range(69),a[:,2],label = 'r2_score for train')
plt.plot(range(69),a[:,3],label = 'r2_score for test')
plt.legend()
plt.show()


# In[50]:


### best model
print('no of features = ',np.argmin(a[:,1])+1)
print('mse for train = ',a[np.argmin(a[:,1])][0])
print('mse for test = ',a[np.argmin(a[:,1])][1])
print('r2_score for train = ',a[np.argmin(a[:,1])][2])
print('r2_score for test = ',a[np.argmin(a[:,1])][3])


# In[51]:


from sklearn.decomposition import PCA

a = []
model = RandomForestRegressor(n_estimators=33,min_samples_split=97,max_depth = 5)
for i in range(1,70):
    trainY = df_train['Td']
    trainX = df_train[['T1', 'T2', 'T3', 'T4', 'T5', 'T6', 'T7', 'B1', 'B2', 'B3', 'B4',
           'B5', 'B6', 'B7', 'B8', 'B9', 'B10', 'B11', 'B12', 'B13', 'B14', 'B15',
           'B16', 'B17', 'B18', 'B19', 'B20', 'B21', 'B22', 'B23', 'B24', 'B25',
           'B26', 'B27', 'B28', 'B29', 'A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7',
           'A8', 'A9', 'A10', 'A11', 'A12', 'A13', 'A14', 'A15', 'A16', 'A17',
           'A18', 'A19', 'A20', 'A21', 'A22', 'A23', 'A24', 'A25', 'A26', 'A27',
           'A28', 'A29', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday',
           'Saturday', 'Sunday']]
    testY = df_test['Td']
    testX = df_test[['T1', 'T2', 'T3', 'T4', 'T5', 'T6', 'T7', 'B1', 'B2', 'B3', 'B4',
           'B5', 'B6', 'B7', 'B8', 'B9', 'B10', 'B11', 'B12', 'B13', 'B14', 'B15',
           'B16', 'B17', 'B18', 'B19', 'B20', 'B21', 'B22', 'B23', 'B24', 'B25',
           'B26', 'B27', 'B28', 'B29', 'A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7',
           'A8', 'A9', 'A10', 'A11', 'A12', 'A13', 'A14', 'A15', 'A16', 'A17',
           'A18', 'A19', 'A20', 'A21', 'A22', 'A23', 'A24', 'A25', 'A26', 'A27',
           'A28', 'A29', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday',
           'Saturday', 'Sunday']]
    pca = PCA(n_components=i)
    trainX = pca.fit_transform(trainX)
    testX = pca.transform(testX)
    model.fit(trainX,trainY)
    print('no. of features = ',i)
    print (mean_squared_error(trainY,model.predict(trainX)))
    print(mean_squared_error(testY,model.predict(testX)))
    print(r2_score(trainY,model.predict(trainX)))
    print(r2_score(testY,model.predict(testX)))
    print('**********************************')
    a.append([mean_squared_error(trainY,model.predict(trainX)),mean_squared_error(testY,model.predict(testX)),
             r2_score(trainY,model.predict(trainX)),r2_score(testY,model.predict(testX))])
a = np.array(a)


# In[52]:


plt.plot(range(69),a[:,0],label = 'mse for train')
plt.plot(range(69),a[:,1],label = 'mse for test')
plt.legend()
plt.show()
plt.plot(range(69),a[:,2],label = 'r2_score for train')
plt.plot(range(69),a[:,3],label = 'r2_score for test')
plt.legend()
plt.show()


# In[53]:


### best model
print('no of features = ',np.argmin(a[:,1])+1)
print('mse for train = ',a[np.argmin(a[:,1])][0])
print('mse for test = ',a[np.argmin(a[:,1])][1])
print('r2_score for train = ',a[np.argmin(a[:,1])][2])
print('r2_score for test = ',a[np.argmin(a[:,1])][3])


# In[ ]:




