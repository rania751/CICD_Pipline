# -*- coding: utf-8 -*-
"""train_model.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1q5js-JNYyW9CvTds9bQNrF2BVJpQtAJl
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import *
from tensorflow.keras.callbacks import ModelCheckpoint
from tensorflow.keras.losses import MeanSquaredError
from tensorflow.keras.metrics import RootMeanSquaredError
from tensorflow.keras.optimizers import Adam

df_info = pd.read_csv('DATAPRICE.csv')

# df_info=df_info[12273:24747]

df_info.shape

# df_info.info

df_info.describe()

df_info.isnull().sum()

## Correlation
df_info.corr()

# sns.jointplot(x='current_datetime',y='gas_price_Gwei',kind='scatter',data=df_info)

df_info.dtypes

df_info.columns

# plt.figure(figsize=(16, 13), dpi=100)
# features = ['gas_price_Gwei',
#        'safe_gas_price', 'ProposeGasPrice', 'fast_gas_price', 'priority_safe',
#        'priority_propose', 'priority_fast', 'BaseFee', 'transactions_nbr:',
#        'blockreward_ETH;', 'trnx_fees;', 'burnet_fees;', 'blocksize_bytes;',
#        'blockgasused:', 'block_base_fee_per_gas_ETH:',
#        'trx_throughput_TPS:']
# heatmap_data = df_info[features]
# corr_matrix = heatmap_data.corr()
# sns.heatmap(corr_matrix, annot=True)

# plt.figure(figsize=(16, 13), dpi=100)
# features = ['gas_price_Gwei',
#        'safe_gas_price', 'ProposeGasPrice', 'fast_gas_price' ,'BaseFee']
# heatmap_data = df[features]
# corr_matrix = heatmap_data.corr()
# sns.heatmap(corr_matrix, annot=True)



# import matplotlib.pyplot as plt

# plt.figure(figsize=(14, 12)) # Set the figure size to 10 inches wide and 6 inches tall
# plt.scatter(df_info['current_datetime'], df_info['gas_price_Gwei'])
# plt.show()

# df_info['blockgasused:'] = df_info['blockgasused:'].str.replace(',', '')
# df_info['blockgasused:'] = df_info['blockgasused:'].astype(int)
# df_info['blocksize_bytes;'] = df_info['blocksize_bytes;'].str.replace(',', '')
# df_info['blocksize_bytes;'] = df_info['blocksize_bytes;'].astype(int)
# df_info['current_datetime'] = pd.to_datetime(df_info['current_datetime'] , format='%Y/%m/%d %H:%M:%S')

# # for i in range(0,11000):
# #   if(df_info['block_base_fee_per_gas_ETH:'][i]=="2.9542166e-08è"):
# df_info['block_base_fee_per_gas_ETH:'][102523]=2.9542166e-08
# df_info['block_base_fee_per_gas_ETH:'][102523]
# df_info['block_base_fee_per_gas_ETH:']= df_info['block_base_fee_per_gas_ETH:'].astype(float)

# df_info.index = pd.to_datetime(df_info['current_datetime'], format='%d.%m.%Y %H:%M:%S')
# # testdaa.index = pd.to_datetime(testdata['current_datetime'], format='%d.%m.%Y %H:%M:%S')

def from_normalized_to_normal(normalized_value, min_value, max_value):
    normal_value = (normalized_value * (max_value - min_value)) + min_value
    return normal_value

from sklearn import metrics
from sklearn.metrics import mean_squared_error as mse
from sklearn.metrics import mean_absolute_error as mae
from sklearn.preprocessing import MinMaxScaler
import sklearn

def plot_predictions1(model, X, y, start, end):

  predictions = model.predict(X).flatten()

  df = pd.DataFrame(data={'Predictions':predictions, 'Actuals':y})
  df1 = pd.DataFrame(index=df.index,columns=['Predictions', 'Actuals'])

  min = data1['gas_price_Gwei'].min()
  max = data1['gas_price_Gwei'].max()

  Ln=[]
  # L=[]
  # Lc=[]
  
  for i in range (0,len(df)):
    df1['Predictions'][i]= from_normalized_to_normal(df.iloc[i]['Predictions'] ,min,max)
    df1['Actuals'][i]= from_normalized_to_normal(df.iloc[i]['Actuals'] ,min,max)
    Ln.append(abs(df1['Predictions'][i] - df1['Actuals'][i]))
    # L.append(abs(df['Predictions'] - df['Actuals']))
  
  plt.figure(figsize=(12,6))
  plt.subplot(2,1,1)
  plt.title('Predictions vs Actuals (Normalized)')
  plt.plot(df['Predictions'][start:end])
  plt.plot(df['Actuals'][start:end])
  plt.legend(['Predictions', 'Actuals'], loc='upper left')

  plt.subplot(2,1,2)
  plt.title('Predictions vs Actuals ')
  plt.plot(df1['Predictions'][start:end])
  plt.plot(df1['Actuals'][start:end])
  plt.legend(['Predictions', 'Actuals'], loc='upper left')

  plt.tight_layout()
  plt.show()

  print('MAE:', metrics.mean_absolute_error(y, predictions))
  print('MSE:', metrics.mean_squared_error(y, predictions))
  print('RMSE:', np.sqrt(metrics.mean_squared_error(y, predictions)))

  print(Ln)

  return df[:],df1[:],Ln

from sklearn import metrics
from sklearn.metrics import mean_squared_error as mse
from sklearn.metrics import mean_absolute_error as mae
from sklearn.preprocessing import MinMaxScaler
import sklearn

def plot_predictions(model, X, y, start=11000, end=11400):

  predictions = model.predict(X).flatten()
  L=[]
  df = pd.DataFrame(data={'Predictions':predictions, 'Actuals':y})
  # df1 = pd.DataFrame(index=df.index,columns=['Predictions', 'Actuals'])

  for i in range (0,len(df)):
    L.append(abs(df['Predictions'][i] - df['Actuals'][i]))

  plt.figure(figsize=(12,6))
  plt.subplot(2,1,1)
  plt.title('Predictions vs Actuals ')
  plt.plot(df['Predictions'][start:end])
  plt.plot(df['Actuals'][start:end])
  plt.legend(['Predictions', 'Actuals'], loc='upper left')

  plt.tight_layout()
  plt.show()
  
  print('MAE:', metrics.mean_absolute_error(y, predictions))
  print('MSE:', metrics.mean_squared_error(y, predictions))
  print('RMSE:', np.sqrt(metrics.mean_squared_error(y, predictions)))
  print(L)
  return df[:],L

def df_to_X_y2(df, window_size=9):
  df_as_np = df.to_numpy()
  X = []
  y = []
  for i in range(len(df_as_np)-window_size):
    row = [r for r in df_as_np[i:i+window_size]]
    X.append(row)
    label = df_as_np[i+window_size][0]
    y.append(label)
  return np.array(X), np.array(y)

# df_info.drop('current_datetime', axis=1, inplace=True)
# df_info.drop('current_block_number', axis=1, inplace=True)
# # testdata.drop('current_datetime', axis=1, inplace=True)
# # testdata.drop('current_block_number', axis=1, inplace=True)

# df_info=df_info.reset_index(drop=True)

# data1 = df_info[['gas_price_Gwei', 'safe_gas_price', 'ProposeGasPrice', 'fast_gas_price','BaseFee','trnx_fees;', 'burnet_fees;','block_base_fee_per_gas_ETH:','trx_throughput_TPS:']]
data1 = df_info[['gas_price_Gwei', 'safe_gas_price', 'ProposeGasPrice', 'fast_gas_price','BaseFee']]

cols=['gas_price_Gwei', 'safe_gas_price', 'ProposeGasPrice', 'fast_gas_price','BaseFee']
# ,'trnx_fees;', 'burnet_fees;','block_base_fee_per_gas_ETH:','trx_throughput_TPS:']

# import pickle
# modelGRU  =pickle.load(open('modeLGRU32_64_32_OR.pkl','rb'))

# import pickle
# modelLSTM  =pickle.load(open('modeLLSTM32_048.pkl','rb'))

# sns.pairplot(data1)

# data1

# X4, y4 = df_to_X_y2(data1)
# X4.shape, y4.shape

# X4_test, y4_test =X4[:25840], y4[:25840]
# X4_train, y4_train=X4[25841:], y4[25841:]
# X4_train.shape, y4_train.shape, X4_test.shape, y4_test.shape

X3, y3 = df_to_X_y2(data1)
X3.shape, y3.shape

# data1

# X3_val, y3_val = X3[67000:70000], y3[67000:70000]
X3_train, y3_train=X3[:100], y3[:100]
X3_test, y3_test =X3[101:], y3[101:]
X3_train.shape, y3_train.shape, X3_test.shape, y3_test.shape

from sklearn.preprocessing import MinMaxScaler
import sklearn
scaler_x = sklearn.preprocessing .MinMaxScaler (feature_range=(0, 1))
scaler_y = sklearn.preprocessing .MinMaxScaler (feature_range=(0, 1))
X3_train = X3_train.reshape(len(X3_train) ,len(cols)*9)
X3_test = X3_test.reshape(len(X3_test) ,len(cols)*9)
y3_train = y3_train.reshape(len(y3_train),1)
y3_test = y3_test.reshape(len(y3_test), 1)
X3_train = scaler_x.fit_transform (X3_train)
y3_train = scaler_y.fit_transform (y3_train)
X3_test = scaler_x.transform (X3_test)
y3_test = scaler_y.transform (y3_test)

len(X3_train),len(y3_train),len(X3_test),len(y3_test)

X3_train.shape, y3_train.shape, X3_test.shape, y3_test.shape

X3_train = X3_train.reshape(len(X3_train), 9,len(cols))
X3_test = X3_test.reshape(len(X3_test), 9,len(cols))
y3_train = y3_train.reshape(len(y3_train), )
y3_test = y3_test.reshape(len(y3_test), )

X3_train.shape, y3_train.shape, X3_test.shape, y3_test.shape

modelLD = Sequential()
modelLD.add(InputLayer((9, 5  )))
modelLD.add(LSTM(units=32, return_sequences=True))
modelLD.add(LSTM(units=64))
modelLD.add(Dense(8, 'relu'))
modelLD.add(Dense(1,'linear'))

c = ModelCheckpoint('modeL', save_best_only=True)

from keras.losses import mean_absolute_error
modelLD.compile(loss=mean_absolute_error, optimizer=Adam(learning_rate=0.0001), metrics=[RootMeanSquaredError()])

from tensorflow.keras.callbacks import EarlyStopping

early_stopping = EarlyStopping(monitor='val_loss',patience=3,mode='min')
modelLD.fit(X3_train, y3_train, validation_data=(X3_test,y3_test), epochs=200, batch_size = 64, verbose = 1, callbacks=[c,early_stopping])

df,df1,listnLSTM=plot_predictions1(modelLD, X3_test, y3_test,0,400)

df1

import pickle
pickle.dump(modelLD,open('modeLLSTM_64_0.0001D_0048_2DAYS.pkl','wb'))

# df,df1,listnLSTM=plot_predictions1(modelLD, X3_test, y3_test)

# from tensorflow.keras.callbacks import EarlyStopping

# early_stopping = EarlyStopping(monitor='val_loss',patience=3,mode='min')
# modelLD.fit(X4_train, y4_train, validation_data=(X4_test,y4_test), epochs=200, batch_size = 32, verbose = 1, callbacks=[cp1N,early_stopping])

# modelL = Sequential()
# modelL.add(InputLayer((9, 5  )))
# modelL.add(LSTM(units=32, return_sequences=True))
# modelL.add(LSTM(units=64))
# modelL.add(Dense(8, 'relu'))
# modelL.add(Dense(1,'linear'))

# CV = ModelCheckpoint('mode', save_best_only=True)

# from keras.losses import mean_absolute_error
# modelL.compile(loss=mean_absolute_error, optimizer=Adam(learning_rate=0.001), metrics=[RootMeanSquaredError()])

# from tensorflow.keras.callbacks import EarlyStopping

# early_stopping = EarlyStopping(monitor='val_loss',patience=3,mode='min')
# modelL.fit(X3_train, y3_train, validation_data=(X3_test,y3_test), epochs=200, batch_size = 64, verbose = 1, callbacks=[CV,early_stopping])

# pickle.dump(modelLD1,open('modeLLSTM_64_32_NO.pkl','wb'))

# d,d1,listLSTMM=plot_predictions1(modelL, X3_test, y3_test)

# modelL1 = Sequential()
# modelL1.add(InputLayer((9, 5  )))
# modelL1.add(LSTM(units=32, return_sequences=True))
# modelL1.add(LSTM(units=64))
# modelL1.add(Dense(8, 'relu'))
# modelL1.add(Dense(1,'linear'))

# CV1 = ModelCheckpoint('mode1', save_best_only=True)

# from keras.losses import mean_absolute_error
# modelL1.compile(loss=mean_absolute_error, optimizer=Adam(learning_rate=0.0001), metrics=[RootMeanSquaredError()])

# from tensorflow.keras.callbacks import EarlyStopping

# early_stopping = EarlyStopping(monitor='val_loss',patience=3,mode='min')
# modelL1.fit(X3_train, y3_train, validation_data=(X3_test,y3_test), epochs=200, batch_size = 64, verbose = 1, callbacks=[CV1,early_stopping])

# dd,dd1,listLSTMM=plot_predictions1(modelL1, X3_test, y3_test)

# dfB,df1B,listnLSTM32nB=plot_predictions1(modelLD, X3_test, y3_test)

# d1

# dd1

import pickle
pickle.dump(modelL1,open('modeLLSTM_64_0.0001D_0.0042.pkl','wb'))

# df

# from tensorflow.keras.callbacks import EarlyStopping

# early_stopping = EarlyStopping(monitor='val_loss',patience=3,mode='min')
# modelLSTM.fit(X4_train, y4_train, validation_data=(X4_test,y4_test), epochs=200, batch_size = 32, verbose = 1, callbacks=[early_stopping])

# df,listnL=plot_predictions(modelLD, X4_test, y4_test)

# df,lista=plot_predictions(modelLSTM, X4_test, y4_test)

def comparison(lista,listl):
  Lc=[]
  for i in range(len(listl)):
      if lista[i] > listl[i]:
        Lc.append("a")
      else:
        Lc.append("b")  
  print(sum(lista)/len(lista))  
  print(sum(listl)/len(listl))    
  print(Lc)
  C1=Lc.count("a")
  C2=Lc.count("b")
  print(C1)
  print(C2)  
  if(C1>C2) :
    return("model 2 is better")
  else:
    return("model 1 is better")

# comparison(listnLSTM,listLSTMM)

# modelLDG = Sequential()
# modelLDG.add(InputLayer((9, 9)))
# modelLDG.add(GRU(units=32, return_sequences=True))
# modelLDG.add(GRU(units=64))
# modelLDG.add(Dense(8, 'relu'))
# modelLDG.add(Dense(1,'linear'))

# cp1G = ModelCheckpoint('modeLG', save_best_only=True)

# from keras.losses import mean_absolute_error
# modelLDG.compile(loss=mean_absolute_error, optimizer=Adam(learning_rate=0.00001), metrics=[RootMeanSquaredError()])

# from tensorflow.keras.callbacks import EarlyStopping

# early_stopping = EarlyStopping(monitor='val_loss',patience=3,mode='min')
# modelGRU.fit(X4_train, y4_train, validation_data=(X4_test,y4_test), epochs=200, batch_size = 32, verbose = 1, callbacks=[early_stopping])

# modelLDGn = Sequential()
# modelLDGn.add(InputLayer((9, 9)))
# modelLDGn.add(GRU(units=32, return_sequences=True))
# modelLDGn.add(GRU(units=64))
# modelLDGn.add(Dense(8, 'relu'))
# modelLDGn.add(Dense(1,'linear'))

# cp1Gn = ModelCheckpoint('modeLGNN', save_best_only=True)

# from keras.losses import mean_absolute_error
# modelLDGn.compile(loss=mean_absolute_error, optimizer=Adam(learning_rate=0.00001), metrics=[RootMeanSquaredError()])

# from tensorflow.keras.callbacks import EarlyStopping

# early_stopping = EarlyStopping(monitor='val_loss',patience=3,mode='min')
# modelLDGn.fit(X3_train, y3_train, validation_data=(X3_test,y3_test), epochs=200, batch_size = 32, verbose = 1, callbacks=[cp1Gn,early_stopping])

# import pickle
# pickle.dump(modelLDGn,open('modeLGRU32_64_32_NO.pkl','wb'))

# df,dff,listGRU32NO=plot_predictions1(modelLDGn, X3_test, y3_test)

# comparison(listGRU32NO,listGR)

# dfG,listL=plot_predictions(modelLSTM, X4_test, y4_test)

# comparison(listL,lista)

# modelLD1 = Sequential()
# modelLD1.add(InputLayer((9, 9)))
# modelLD1.add(LSTM(units=50, return_sequences=True,activation='relu'))
# modelLD1.add(Dropout(0.2))

# modelLD1.add(LSTM(units=60, return_sequences=True,activation='relu'))
# modelLD1.add(Dropout(0.3))


# modelLD1.add(LSTM(units=80, return_sequences=True,activation='relu'))
# modelLD1.add(Dropout(0.4))

# modelLD1.add(LSTM(units=80, return_sequences=True,activation='relu'))
# modelLD1.add(Dropout(0.4))

# modelLD1.add(LSTM(units=120, activation='relu'))
# modelLD1.add(Dropout(0.5))

# modelLD1.add(Dense(1,'linear'))

# cp2 = ModelCheckpoint('modeLLSTM', save_best_only=True)

# from keras.losses import mean_absolute_error
# modelLD1.compile(loss=mean_absolute_error, optimizer=Adam(learning_rate=0.0001), metrics=[RootMeanSquaredError()])

# from tensorflow.keras.callbacks import EarlyStopping

# early_stopping = EarlyStopping(monitor='val_loss',patience=3,mode='min')
# modelLD1.fit(X3_train, y3_train, validation_data=(X3_test,y3_test), epochs=200, batch_size = 32, verbose = 1, callbacks=[cp2,early_stopping])

# import pickle
# pickle.dump(modelLD,open('modeLLSTM32_048.pkl','wb'))

# modelGRU= Sequential()
# modelGRU.add(InputLayer((9, 9)))
# modelGRU.add(GRU(units=32, return_sequences=True))
# modelGRU.add(GRU(units=64))
# modelGRU.add(Dense(8, activation='relu'))
# modelGRU.add(Dense(1, activation='linear'))
# modelGRU.summary()

# cpG = ModelCheckpoint('modelGRU/',save_best_only=True)

# modelGRU.compile(loss=MeanSquaredError(), optimizer=Adam(learning_rate=0.0001), metrics=[RootMeanSquaredError()])

# from tensorflow.keras.callbacks import EarlyStopping

# early_stopping = EarlyStopping(monitor='val_loss',patience=3,mode='min')
# modelGRU.fit(X3_train, y3_train, validation_data=(X3_test,y3_test), epochs=200, batch_size = 32, verbose = 1, callbacks=[cpG,early_stopping])

# df2,df3,listnG=plot_predictions1(modelGRU, X3_test, y3_test)

# model5 = Sequential()
# model5.add(InputLayer((6, 9)))
# model5.add(LSTM(32, return_sequences=True))
# model5.add(Dropout(0.25))
# model5.add(LSTM(32, return_sequences=True))
# model5.add(Dropout(0.25))
# model5.add(LSTM(32, return_sequences=True))
# model5.add(Dropout(0.25))
# model5.add(LSTM(64))
# model5.add(Dense(8, 'relu'))
# model5.add(Dense(1, 'linear'))

# model5.summary()

# model8 = Sequential()
# model8.add(InputLayer((6, 9)))
# model8.add(Conv1D(64, kernel_size=2))
# model8.add(Flatten())
# model8.add(Dense(8, 'relu'))
# model8.add(Dense(1, 'linear'))

# model8.summary()

# setting the seed to achieve consistent and less random predictions at each execution
#np.random.seed(2016)

# from tensorflow.keras.models import Sequential
# from tensorflow.keras.layers import Dense
# from tensorflow.keras.layers import LSTM
# from tensorflow.keras.layers import Dropout



# # setting the model architecture
# model1=Sequential()
# model1.add(InputLayer((6, 9)))
# model1.add(LSTM(32,return_sequences=True,activation="relu"))
# # model.add(leakyRelu(alpha=0.5))
# model1.add(Dropout(0.2))
# model1.add(LSTM(32,activation="relu",return_sequences=True))
# # model.add(leakyRelu(alpha=0.5))
# model1.add(Dropout(0.2))
# model1.add(LSTM(32,activation="relu",return_sequences=True))
# # model.add(leakyRelu(alpha=0.5))
# model1.add(Dropout(0.2))
# model1.add(LSTM(32))
# # model.add(leakyRelu(alpha=0.5))
# model1.add(Dropout(0.2))
# model1.add(Dense(8, 'relu'))
# model1.add(Dense(1, 'linear'))

# # printing the model summary
# model1.summary()

# from keras.optimizers import SGD, Adam

# regressorLSTM = Sequential()
# # First GRU layer with Dropout regularisation

# regressorLSTM.add(InputLayer((9, 9)))
# regressorLSTM.add(LSTM(units=128))

# regressorLSTM.add(Dense(8, 'relu'))
# regressorLSTM.add(Dense(1, 'linear'))

# from tensorflow.keras.callbacks import EarlyStopping
# from keras.losses import mean_absolute_error
# early_stopping = EarlyStopping(monitor='val_loss',patience=3,mode='min')
# # Compiling the RNN
# cpB = ModelCheckpoint('modB/', save_best_only=True)
# regressorLSTM.compile(loss=mean_absolute_error, optimizer=Adam(learning_rate=0.0001), metrics=[RootMeanSquaredError()])

# regressorLSTM.fit(X4_train, y4_train, validation_data=(X4_test,y4_test), epochs=200, batch_size = 32, verbose = 1, callbacks=[cpB,early_stopping])
# optimizer=SGD(lr=0.01, decay=1e-7, momentum=0.9, nesterov=False),loss='mean_squared_error')

# DF4,listLSTM128=plot_predictions(regressorLSTM, X4_test, y4_test)

# pickle.dump(listLSTM128,open('listLSTM128_OR.pkl','wb'))

# comparison(listLSTM128,listGRU128)

# # The GRU architecture
# from keras.optimizers import SGD, Adam

# regressorGRU = Sequential()
# # First GRU layer with Dropout regularisation

# regressorGRU.add(InputLayer((9, 9)))
# regressorGRU.add(GRU(units=128))

# regressorGRU.add(Dense(8, 'relu'))
# regressorGRU.add(Dense(1, 'linear'))

# from tensorflow.keras.callbacks import EarlyStopping
# from keras.losses import mean_absolute_error
# early_stopping = EarlyStopping(monitor='val_loss',patience=3,mode='min')
# # Compiling the RNN
# cp = ModelCheckpoint('mod&/', save_best_only=True)
# regressorGRU.compile(loss=mean_absolute_error, optimizer=Adam(learning_rate=0.0001), metrics=[RootMeanSquaredError()])

# regressorGRU.fit(X4_train, y4_train, validation_data=(X4_test,y4_test), epochs=200, batch_size = 32, verbose = 1, callbacks=[cp,early_stopping])
# optimizer=SGD(lr=0.01, decay=1e-7, momentum=0.9, nesterov=False),loss='mean_squared_error')

# DF3,listGRU128=plot_predictions(regressorGRU, X4_test, y4_test)

# pickle.dump(listGRU128,open('listGRU128_OR.pkl','wb'))

# comparison(listL,listGRU128)

# # The GRU architecture
# from tensorflow.keras.callbacks import EarlyStopping

# early_stopping = EarlyStopping(monitor='val_loss',patience=3,mode='min')
# from keras.optimizers import SGD, Adam
# regressorGRU1 = Sequential()
# # First GRU layer with Dropout regularisation

# regressorGRU1.add(InputLayer((6, 9)))
# regressorGRU1.add(GRU(units=32, return_sequences=True, activation='tanh'))
# regressorGRU1.add(Dropout(0.2))
# # Second GRU layer
# regressorGRU1.add(GRU(units=32, return_sequences=True, activation='tanh'))
# regressorGRU1.add(Dropout(0.2))
# # Third GRU layer
# regressorGRU1.add(GRU(units=32, return_sequences=True,activation='tanh'))
# regressorGRU1.add(Dropout(0.2))
# # Fourth GRU layer
# regressorGRU1.add(GRU(units=32, activation='tanh'))
# regressorGRU1.add(Dropout(0.2))
# # The output layer
# # regressorGRU1.add(Dense(units=1))
# regressorGRU1.add(Dense(8, 'relu'))
# regressorGRU1.add(Dense(1,'linear'))
# cp9 = ModelCheckpoint('modeL9/', save_best_only=True)
# regressorGRU1.compile(loss=MeanSquaredError(), optimizer=Adam(learning_rate=0.0001), metrics=[RootMeanSquaredError()])
# regressorGRU1.fit(X3_train, y3_train, validation_data=(X3_test,y3_test), epochs=200, batch_size = 32, verbose = 1, callbacks=[cp9,early_stopping])
# # optimizer=SGD(lr=0.01, decay=1e-7, momentum=0.9, nesterov=False),loss='mean_squared_error')

# import pickle
# pickle.dump(regressorGRU,open('GRUModel_045_128.pkl','wb'))

# from google.colab import files

# # Download the file to your local machine
# files.download('dd,.csv')