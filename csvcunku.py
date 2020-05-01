import pymysql
import csv
import codecs
def get_conn():
    conn = pymysql.connect(host='106.15.192.35', port=3306, user='root', passwd='123456', db='pachong', charset='utf8')
    return conn
def insert(cur, sql, args):
    cur.execute(sql, args)
def read_csv_to_mysql(filename):
    with codecs.open(filename=filename, mode='r',  encoding = "unicode_escape") as f:
        reader = csv.reader(f)
        head = next(reader)
        conn = get_conn()
        cur = conn.cursor()
        sql = 'insert into tb_finance_range values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        for item in reader:
            if item[1] is None or item[1] == '':
                continue
            args = tuple(item)
            print(args)
            insert(cur, sql=sql, args=args)
        conn.commit()
        cur.close()
        conn.close()
if __name__ == '__main__':
    read_csv_to_mysql('fubiao.csv')



