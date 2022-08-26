
import pandas as pd
import csv

# data = pd.read_csv("/media/i3/DATA/test/testcsv.csv")
#
# # data.head(5)
#
# data = data.where((pd.notnull(data)), None)
#
# print(data)

f = open("/media/i3/DATA/test/dbupdate.csv", 'r', encoding='utf-8')
rd = csv.reader(f)

import pymysql

# db = pymysql.connect(host='localhost', port=3306, user='root', password='i3system7890\', db='pythonDB', charset='utf8')   # charset: ??? ??
# db = pymysql.connect(host='localhost', user='root', password='i3system7890\\', db='pythonDB', charset='utf8')   # charset: ??? ??
db = pymysql.connect(host='localhost', user='2sensor', password='i3system7890', db='LWIRXGA12UM', charset='utf8')   # charset: ??? ??
print(db)

# 3. curosr ??
cursor = db.cursor()

sql = "SELECT * FROM rawdata"
cursor.execute(sql)
#rows = cursor.fetchall()
#print(rows)

sql = "DESC rawdata"
cursor.execute(sql)

sql = 'INSERT IGNORE INTO rawdata (IMG_no, IMG_name, IMG_date, IMG_time, IMG_place, IMG_weather, env_temp, outside, detector, ' \
      'NETD_30C, lens, lens_fov, SW_Contrast, SW_Brightness, CAR_exist, MAN_exist) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
# sql = 'UPDATE INTO rawdata (csv_id, csv_date, csv_name, csv_on) values (%s, %s, %s, %s)'

for line in rd:
    # print('0 : '+line[0])
    # print('1 : '+line[1])
    # print('2 : '+line[2])
    # line0 = float(line[0])
    # line0 = int(line0)
    cursor.execute(sql, (line[0], line[1], line[2], line[3], line[4], line[5], line[6], line[7], line[8], line[9], line[10], line[11], line[12], line[13], line[14], line[15]))

# # 4. insert value
# sql = 'INSERT INTO ????(???1, ???2, ...) VALUES(%s, %s, ...)'
#
# # 5. ??? import
# for idx in range(len(data)):
#     cursor.execute(sql, tuple(data.values[idx]))

# 6. db update
db.commit()

# 7. DB & csv close
db.close()
f.close()
