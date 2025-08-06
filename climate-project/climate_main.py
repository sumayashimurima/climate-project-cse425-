import csv
# Data_Loading_Parsing
def data_loading(filename):
    data = []
    with open("global_warming_dataset.csv",'r',encoding='utf-8') as File:

        Reader = csv.DictReader(File)
        for row in Reader:
            Record = {
                "Country": row["Country"],
                "Years": int(row["Year"]),
                "Temperature_Anomaly": float(row["Temperature_Anomaly"]),
                "CO2": float(row["CO2_Emissions"]),
                "GDP": float(row["GDP"]),
                "Extreme_Weather_Events": int(row["Extreme_Weather_Events"])
            }
            data.append(Record)
    return data

# Data_Filtering_Searching

def search_by_country(data, country_name):
    return [d for d in data if d["Country"].lower() == country_name.lower()]

def search_by_yearRange(data, start_year, end_year):
    return [d for d in data if start_year <= d["Years"] <= end_year]

def find_extreme_weather_events(data, top_n=5):
    sorted_data = sorted(data, key=lambda x: x["Extreme_Weather_Events"], reverse=True)
    return sorted_data[:top_n], sorted_data[-top_n:]

def find_high_co2_emitters(data, year, top_n=5):
    filtered = [d for d in data if d["Years"] == year]
    sorted_data = sorted(filtered, key=lambda x: x["CO2"], reverse=True)
    return sorted_data[:top_n]

#  Sorting_Aggregation

def sort_by_temperature_anomaly(data, ascending=True):
    return sorted(data, key=lambda x: x["Temperature_Anomaly"], reverse=not ascending)

def sort_by_Gdp(data, year, ascending=True):
    filtered = [d for d in data if d["Years"] == year]
    return sorted(filtered, key=lambda x: x["GDP"], reverse=not ascending)

def average_metrics(data, country_name):
    filtered = [d for d in data if d["Country"].lower() == country_name.lower()]
    if not filtered:
        return None
    avgTemp=sum(d["Temperature_Anomaly"] for d in filtered) / len(filtered)
    avgCo2=sum(d["CO2"] for d in filtered) / len(filtered)
    avgGdp=sum(d["GDP"] for d in filtered) / len(filtered)
    return {"avg_temp": avgTemp, "avg_co2": avgCo2, "avg_gdp": avgGdp}

def main():
    filename = "global_warming_dataset.csv"
    data = data_loading(filename)

    print("\nSearch by CountryName Like:Bangladesh")
    bd_data = search_by_country(data,"Bangladesh")
    for record in bd_data[:5]:
        print(record)

    print("\nRecords from 1950 to 2000")
    range_data=search_by_yearRange(data, 1950, 2000)
    print(f"Total Records: {len(range_data)}")

    print("\nTop 5 Countries by Extreme Events")
    top_extreme,bottom_extreme=find_extreme_weather_events(data)
    print("Highest Extreme Events:")
    for d in top_extreme:
        print(d)
    print("Lowest Extreme Events:")
    for d in bottom_extreme:
        print(d)

    print("\nTop 5 CO₂ Emitters in 2000")
    top_emitters=find_high_co2_emitters(data, 2000)
    for d in top_emitters:
        print(d)

    print("\nSort by Temperature_Anomaly (Descending)")
    sorted_temp=sort_by_temperature_anomaly(data, ascending=False)
    for d in sorted_temp[:5]:
        print(d)

    print("\nSort by GDP in 2000 (Ascending)")
    sorted_gdp=sort_by_Gdp(data, 2000, ascending=True)
    for d in sorted_gdp[:5]:
        print(d)

    print("\nAverage Metrics for Bangladesh")
    avg_bd = average_metrics(data, "Bangladesh")
    print(avg_bd)


if __name__ == "__main__":
    main()

    

# import csv

# # data_loading and parsing

# def data_load(file_path):
#    data = []
#    with open(r"C:\Users\Hp\Downloads\global_warming_dataset.csv",'r',encoding='utf-8') as file :
#         reader=csv.DictReader(file)
#         # print(reader)
#         for row in reader:
#             try:
#                 record={'Country':row['Country'].strip(),
#                         'Year':int(row['Year']),
#                         'TempAnomaly': float(row['Temperature_Anomaly']),
#                         'CO2':float(row['CO2_Emissions']),
#                         'Extreme_Weather_Events':int(row['Extreme_Weather_Events']),
#                         'GDP':float(row['GDP'])


#                 }
#                 data.append(record)
#             except ValueError:
#                 continue
#             return data
        
# # 2. FILTERING & SEARCHING

# def search_by_country(data, country):
#     return [record for record in data if record['Country'].lower() == country.lower()]

# def search_by_year_range(data, start_year, end_year):
#     return [record for record in data if start_year <= record['Year'] <= end_year]

# def Extreme_Weather_Events(data, highest=True):
#     country_events = {}
#     for r in data:
#         country_events[r['Country']] = country_events.get(r['Country'], 0) + r['Extreme_Weather_Events']
#     sorted_events = sorted(country_events.items(), key=lambda x: x[1], reverse=highest)
#     return sorted_events[:10] 

# def top_co2_emitters(data, year, n=10):
#     filtered = [r for r in data if r['Year'] == year]
#     sorted_list = sorted(filtered, key=lambda x: x['CO2'], reverse=True)
#     return sorted_list[:n]

# # 3. SORTING & AGGREGATION

# def sort_by_temp_anomaly(data, reverse=False):
#     return sorted(data, key=lambda x: x['TempAnomaly'], reverse=reverse)

# def sort_by_gdp(data, year, reverse=False):
#     filtered = [r for r in data if r['Year'] == year]
#     return sorted(filtered, key=lambda x: x['GDP'], reverse=reverse)

# def average_metrics(data, country):
#     records = search_by_country(data, country)
#     if not records:
#         return None
#     avg_co2 = sum(r['CO2'] for r in records) / len(records)
#     avg_temp = sum(r['TempAnomaly'] for r in records) / len(records)
#     avg_gdp = sum(r['GDP'] for r in records) / len(records)
#     return {
#         'Country': country,
#         'AvgCO2': round(avg_co2, 2),
#         'AvgTempAnomaly': round(avg_temp, 2),
#         'AvgGDP': round(avg_gdp, 2)
#     }

# # 4. DISPLAY FUNCTIONS

# def display_records(records, limit=10):
#     for r in records[:limit]:
#         print(f"{r['Country']:20} Year: {r['Year']} TempAnomaly: {r['TempAnomaly']} "
#               f"CO2: {r['CO2']} Extreme_Weather_Events: {r['Extreme_Weather_Events']} GDP: {r['GDP']}")

# # MAIN
# if __name__ == "__main__":
#     file_path = "global_warming.csv"  # Change to your dataset path
#     data = data_load(file_path)

#     print("\n--- Search by Country: Bangladesh ---")
#     display_records(search_by_country(data, "Bangladesh"))

#     print("\n--- Search by Year Range: 1950-1960 ---")
#     display_records(search_by_year_range(data, 1950, 1960))

#     print("\n--- Top 10 Countries with Highest Extreme Events ---")
#     print(Extreme_Weather_Events(data, highest=True))

#     print("\n--- Top 10 CO2 Emitters in 2020 ---")
#     display_records(top_co2_emitters(data, 2020, n=10))

#     print("\n--- Sort by Temperature Anomaly (Descending) ---")
#     display_records(sort_by_temp_anomaly(data, reverse=True))

#     print("\n--- Sort by GDP for Year 2020 (Descending) ---")
#     display_records(sort_by_gdp(data, 2020, reverse=True))

#     print("\n--- Average Metrics for Bangladesh ---")
#     print(average_metrics(data, "Bangladesh"))
        
# #     def load_data(file_path):
#     # data = []
#     # with open(file_path, 'r', encoding='utf-8') as f:
#     #     reader = csv.DictReader(f)
#     #     for row in reader:
#     #         try:
#     #             record = {
#     #                 'Country': row['Country'].strip(),
#     #                 'Year': int(row['Year']),
#     #                 'TempAnomaly': float(row['Temperature anomaly']),
#     #                 'CO2': float(row['CO2 emissions']),
#     #                 'ExtremeEvents': int(row['Extreme events']),
#     #                 'GDP': float(row['GDP'])
#     #             }
#     #             data.append(record)
#     #         except ValueError:
#     #             # Skip rows with invalid/missing data
#     #             continue
#     # return data

    