import psycopg2

#  'NAME': 'tyutor',
#         'USER': 'tyutoruser',
#         'PASSWORD': 'Hfazliddin98',
#         'HOST': 'localhost',
#   
#       'PORT': '',
try:
    conn = psycopg2.connect(
        host = 'localhost',
        dbname = 'tyutor',
        user = 'postgres',
        password = 'Hfazliddin98',
        port = 5432
    )
    print('ulandi')
    conn.close()
    print('uzildi')

except Exception as error:
    print(error)