import numpy as np
import pandas as pd
import tensorflow as tf
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report, confusion_matrix


# Wczytanie danych
col_names = ['pregnant','glucose','bp','skin','insulin','bmi','pedigree','age','label']
pima = pd.read_csv('diabetes.csv',header=None,names=col_names)

# Sprawdzenie pierwszych kilku wierszy danych
print(data.head())


# Podział danych na cechy (X) i etykiety (y)
X = data.iloc[:, :-1].values  # Wszystkie kolumny oprócz ostatniej
y = data.iloc[:, -1].values    # Ostatnia kolumna

# Podział na zestawy treningowe i testowe
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Normalizacja danych
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)


# Tworzenie modelu
model = tf.keras.Sequential([
    tf.keras.layers.Dense(16, activation='relu', input_shape=(X_train.shape[1],)),
    tf.keras.layers.Dense(8, activation='relu'),
    tf.keras.layers.Dense(1, activation='sigmoid')  # Warstwa wyjściowa
])

# Kompilacja modelu
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])


# Trenowanie modelu
model.fit(X_train, y_train, epochs=100, batch_size=10, validation_split=0.2)


# Ocena modelu
loss, accuracy = model.evaluate(X_test, y_test)
print(f'Test Accuracy: {accuracy:.4f}')

# Predykcje
y_pred = (model.predict(X_test) > 0.5).astype("int32")

# Macierz pomyłek i raport klasyfikacji
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))


model.save('pima_diabetes_model.h5')
