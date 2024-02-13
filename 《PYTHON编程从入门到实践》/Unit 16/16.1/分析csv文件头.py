import csv
filename = 'sitka_weather_2018_full.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)  # 表头
    print(header_row)

    # 换一种方式打印表头
    for index, colum_header in enumerate(header_row):
        print(index, colum_header)

