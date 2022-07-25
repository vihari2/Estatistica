from math import sqrt
from statistics import mean, stdev, median, variance
import statistics
from decimal import Decimal
from unicodedata import decimal
import matplotlib.pyplot as plt


print("------LISTA 1-------")
lista = [26.00, 28.00, 31.00, 31.00, 32.00, 32.00, 35.00, 35.00, 37.00, 37.00, 40.00, 43.00, 44.00, 44.00, 46.00, 46.00, 49.00, 49.00, 50.00, 50.00]
soma1 = sum(lista)
quant = len(lista) 

media1 = soma1 / quant 
print(f"a media é {media1:.2f}") 

i = 1 
for x in lista: 
    print(i, (x - media1)**2)
    i = i + 1 

    
mediana1 = median(lista)
print(f"a mediana é {mediana1:.2f}")

variancia1 = variance(lista)   
print(f"a variância é {variancia1:.2f}")

desviopadrao1 = sqrt(variancia1)
print(f"o desvio padrão é {desviopadrao1:.2f}")

coeficientev = desviopadrao1 / media1 * 100
print(f"o coeficiente de variação é {coeficientev:.2f}%")

try:
     tamanhom = (1.96 * desviopadrao1 / 0.10 * media1)**2
except ZeroDivisionError:
    tamanhom = 0 
print(f"o tamanho da amostra é {tamanhom:.2f}") 

if tamanhom < media1: 
    print(f"o tamanho da amostra é menor que a média")
if tamanhom > media1:
    print(f"o tamanho da amostra é maior que a média")

plt.hist(lista, 6, rwidth=0.9)
plt.show()


print("-------------------------------------------------------------------------------------------------------------------------------------------------")
print("------LISTA 2-------")

lista2 = [26.19, 26.31, 26.43, 27.71, 28.12, 29.57, 31.18, 31.25, 31.97, 32.65, 33.69, 34.91, 35.00, 35.74, 36.93, 37.76, 37.82, 38.08, 38.95, 40.87]
soma1 = sum(lista2)
quant = len(lista2) 

media1 = soma1 / quant 
print(f"a media é {media1:.2f}") 


i = 1 
for x in lista2: 
    print(i, (x - media1)**2)
    i = i + 1 

mediana1 = median(lista2)
print(f"a mediana é {mediana1:.2f}")

variancia1 = variance(lista2)   
print(f"a variância é {variancia1:.2f}")

desviopadrao1 = sqrt(variancia1)
print(f"o desvio padrão é {desviopadrao1:.2f}")

coeficientev = desviopadrao1 / media1 * 100
print(f"o coeficiente de variação é {coeficientev:.2f}%")

try:
     tamanhom = (1.96 * desviopadrao1 / 0.10 * media1)**2
except ZeroDivisionError:
    tamanhom = 0 
print(f"o tamanho da amostra é {tamanhom:.2f}") 

if tamanhom < media1: 
    print(f"o tamanho da amostra é menor que a média")
if tamanhom > media1:
    print(f"o tamanho da amostra é maior que a média")
    
plt.hist(lista2, 6, rwidth=0.9)
plt.show()

print("-------------------------------------------------------------------------------------------------------------------------------------------------")
print("------LISTA 3-------")

lista3 = [1.02, 1.55, 1.56, 1.99, 2.36, 2.43, 2.53, 2.97, 2.99, 3.01, 3.20, 3.23, 3.24, 3.34, 3.36, 3.58, 3.73, 3.78, 3.87, 3.99]

soma1 = sum(lista3)
quant = len(lista3) 

media1 = soma1 / quant 
print(f"a media é {media1:.2f}") 

i = 1 
for x in lista3: 
    print(i, (x - media1)**2)
    i = i + 1 


print(f"a media é {media1:.2f}") 

mediana1 = median(lista3)
print(f"a mediana é {mediana1:.2f}")

variancia1 = variance(lista3)   
print(f"a variância é {variancia1:.2f}")

desviopadrao1 = sqrt(variancia1)
print(f"o desvio padrão é {desviopadrao1:.2f}")

coeficientev = desviopadrao1 / media1 * 100
print(f"o coeficiente de variação é {coeficientev:.2f}%")

try:
     tamanhom = (1.96 * desviopadrao1 / 0.10 * media1)**2
except ZeroDivisionError:
    tamanhom = 0 
print(f"o tamanho da amostra é {tamanhom:.2f}") 

if tamanhom < media1: 
    print(f"o tamanho da amostra é menor que a média")
if tamanhom > media1:
    print(f"o tamanho da amostra é maior que a média")

plt.hist(lista3, 6, rwidth=0.9)
plt.show()

print("-------------------------------------------------------------------------------------------------------------------------------------------------")
print("------LISTA 4-------")

lista4 = [5.45, 6.09, 6.29, 6.30, 6.60, 6.65, 6.91, 7.08, 7.14, 7.26, 7.78, 7.97, 8.27, 8.46, 9.12, 9.33, 9.48, 9.51, 9.56, 9.98]

soma1 = sum(lista4)
quant = len(lista4) 

media1 = soma1 / quant 
print(f"a media é {media1:.2f}") 

i = 1 
for x in lista4: 
    print(i, (x - media1)**2)
    i = i + 1 


print(f"a media é {media1:.2f}") 

mediana1 = median(lista4)
print(f"a mediana é {mediana1:.2f}")

variancia1 = variance(lista4)   
print(f"a variância é {variancia1:.2f}")

desviopadrao1 = sqrt(variancia1)
print(f"o desvio padrão é {desviopadrao1:.2f}")

coeficientev = desviopadrao1 / media1 * 100
print(f"o coeficiente de variação é {coeficientev:.2f}%")

try:
     tamanhom = (1.96 * desviopadrao1 / 0.10 * media1)**2
except ZeroDivisionError:
    tamanhom = 0 
print(f"o tamanho da amostra é {tamanhom:.2f}") 

if tamanhom < media1: 
    print(f"o tamanho da amostra é menor que a média")
if tamanhom > media1:
    print(f"o tamanho da amostra é maior que a média")

plt.hist(lista4, 6, rwidth=0.9)
plt.show()

print("-------------------------------------------------------------------------------------------------------------------------------------------------")
lista5 = [21.39, 21.86, 22.74, 23.68, 25.40, 26.28, 26.51, 26.63, 26.79, 29.37, 31.00, 31.97, 32.82, 33.23, 33.48, 33.67, 35.66, 36.04, 37.14, 38.87]
print("------LISTA 5-------")

soma1 = sum(lista5)
quant = len(lista5) 

media1 = soma1 / quant 
print(f"a media é {media1:.2f}") 

i = 1 
for x in lista5: 
    print(i, (x - media1)**2)
    i = i + 1 


print(f"a media é {media1:.2f}") 

mediana1 = median(lista5)
print(f"a mediana é {mediana1:.2f}")

variancia1 = variance(lista5)   
print(f"a variância é {variancia1:.2f}")

desviopadrao1 = sqrt(variancia1)
print(f"o desvio padrão é {desviopadrao1:.2f}")

coeficientev = desviopadrao1 / media1 * 100
print(f"o coeficiente de variação é {coeficientev:.2f}%")

try:
     tamanhom = (1.96 * desviopadrao1 / 0.10 * media1)**2
except ZeroDivisionError:
    tamanhom = 0 
print(f"o tamanho da amostra é {tamanhom:.2f}") 

if tamanhom < media1: 
    print(f"o tamanho da amostra é menor que a média")
if tamanhom > media1:
    print(f"o tamanho da amostra é maior que a média")

print("-------------------------------------------------------------------------------------------------------------------------------------------------")
print("------LISTA 6-------")

plt.hist(lista5, 6, rwidth=0.9)
plt.show()

lista6 = [6.08, 7.02, 7.03, 7.06, 7.21, 7.42, 7.59, 9.00, 10.09, 10.48, 10.65, 11.42, 11.81, 13.46, 13.47, 13.58, 14.88, 15.84, 18.33, 18.90]

soma1 = sum(lista6)
quant = len(lista6) 

media1 = soma1 / quant 
print(f"a media é {media1:.2f}") 

i = 1 
for x in lista6: 
    print(i, (x - media1)**2)
    i = i + 1 


print(f"a media é {media1:.2f}") 

mediana1 = median(lista6)
print(f"a mediana é {mediana1:.2f}")

variancia1 = variance(lista6)   
print(f"a variância é {variancia1:.2f}")

desviopadrao1 = sqrt(variancia1)
print(f"o desvio padrão é {desviopadrao1:.2f}")

coeficientev = desviopadrao1 / media1 * 100
print(f"o coeficiente de variação é {coeficientev:.2f}%")

try:
     tamanhom = (1.96 * desviopadrao1 / 0.10 * media1)**2
except ZeroDivisionError:
    tamanhom = 0 
print(f"o tamanho da amostra é {tamanhom:.2f}") 

if tamanhom < media1: 
    print(f"o tamanho da amostra é menor que a média")
if tamanhom > media1:
    print(f"o tamanho da amostra é maior que a média")

plt.hist(lista6, 6, rwidth=0.9)
plt.show()

print("-------------------------------------------------------------------------------------------------------------------------------------------------")
print("------LISTA 7-------")

lista7 = [35.30, 42.12, 42.12, 42.52, 46.79, 47.69, 47.74, 49.24, 49.58, 54.92, 56.04, 56.36, 59.59, 60.57, 67.57, 67.09, 68.39, 69.67, 69.73, 70.60]
soma1 = sum(lista7)
quant = len(lista7) 

media1 = soma1 / quant 
print(f"a media é {media1:.2f}") 

i = 1 
for x in lista7: 
    print(i, (x - media1)**2)
    i = i + 1 


print(f"a media é {media1:.2f}") 

mediana1 = median(lista7)
print(f"a mediana é {mediana1:.2f}")

variancia1 = variance(lista7)   
print(f"a variância é {variancia1:.2f}")

desviopadrao1 = sqrt(variancia1)
print(f"o desvio padrão é {desviopadrao1:.2f}")

coeficientev = desviopadrao1 / media1 * 100
print(f"o coeficiente de variação é {coeficientev:.2f}%")

try:
     tamanhom = (1.96 * desviopadrao1 / 0.10 * media1)**2
except ZeroDivisionError:
    tamanhom = 0 
print(f"o tamanho da amostra é {tamanhom:.2f}") 

if tamanhom < media1: 
    print(f"o tamanho da amostra é menor que a média")
if tamanhom > media1:
    print(f"o tamanho da amostra é maior que a média")

plt.hist(lista7, 6, rwidth=0.9)
plt.show()

print("-------------------------------------------------------------------------------------------------------------------------------------------------")
print("------LISTA 8-------")

lista8 = [72.01, 74.46, 75.08, 77.74, 79.66, 92.47, 94.64, 96.23, 98.90, 99.01, 101.03, 106.40, 106.13, 108.33, 109.09, 109.69, 110.42, 111.43, 112.99, 118.98]
soma1 = sum(lista8)
quant = len(lista8) 

media1 = soma1 / quant 
print(f"a media é {media1:.2f}") 

i = 1 
for x in lista8: 
    print(i, (x - media1)**2)
    i = i + 1 


print(f"a media é {media1:.2f}") 

mediana1 = median(lista8)
print(f"a mediana é {mediana1:.2f}")

variancia1 = variance(lista8)   
print(f"a variância é {variancia1:.2f}")

desviopadrao1 = sqrt(variancia1)
print(f"o desvio padrão é {desviopadrao1:.2f}")

coeficientev = desviopadrao1 / media1 * 100
print(f"o coeficiente de variação é {coeficientev:.2f}%")

try:
     tamanhom = (1.96 * desviopadrao1 / 0.10 * media1)**2
except ZeroDivisionError:
    tamanhom = 0 
print(f"o tamanho da amostra é {tamanhom:.2f}") 

if tamanhom < media1: 
    print(f"o tamanho da amostra é menor que a média")
if tamanhom > media1:
    print(f"o tamanho da amostra é maior que a média")

plt.hist(lista8, 6, rwidth=0.9)
plt.show()

print("-------------------------------------------------------------------------------------------------------------------------------------------------")



