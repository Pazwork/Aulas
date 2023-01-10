import pandas as pd

years = 5
percentage = 5
i = 0
year = []
new_list_values_final = []

vehicle_year = {"Hilux 2017": 300.00,
                "Corolla 2020": 200.00,
                "Civic 2021": 250.00,
                "HB20 2019": 200.00,
                "Prisma 2018": 150.00,
                "Onix 2020": 100.00}


def depreciation(j, percentage, years):
    t = [j]
    n = 1
    while n <= years:
        t.append((j * ((1 - (percentage / 100)) ** n)))
        n += 1
    return t


new_list_keys = list(vehicle_year.keys())
new_list_values = [float(x) for x in vehicle_year.values()]

for k in range(len(new_list_values)):
    new_list_values_final.append(depreciation(new_list_values[k], percentage, years))

vehicle_year_final = dict(zip(new_list_keys, new_list_values_final))

while i <= years:
    year.append("Ano " + str(i))
    i += 1

df = pd.DataFrame(vehicle_year_final, index=year)
pd.set_option('display.precision', 2)

df1 = df.T
print(df1)