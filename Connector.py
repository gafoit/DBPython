import oracledb as odb

from ErrDialog import ErrDialog

user = 'gft'
pswd = 'Gaf01t'
odb.init_oracle_client()
con = odb.connect(user=user, password=pswd, dsn="localhost/XE")

cur = con.cursor()
out_cur = con.cursor()


def get_summary_report(connect: odb.Connection, f1: str, f2: str, f3: str):
    cursor = connect.cursor()
    out_cursor = connect.cursor()
    cursor.callproc('summary_report', [f1, f2, f3, out_cursor])
    return [[i[0] for i in out_cursor.description]] + out_cursor.fetchall()


def get_menu(connect: odb.Connection):
    cursor = connect.cursor()
    cursor.execute('''select * from menu''')
    return cursor.fetchall()


def get_rate(connect: odb.Connection):
    cursor = connect.cursor()
    cursor.execute('''select * from rate''')
    return cursor.fetchall()


def get_restraunt(connect: odb.Connection):
    cursor = connect.cursor()
    cursor.execute('''select * from restraunts''')
    return cursor.fetchall()


def get_entity_log(connect: odb.Connection):
    cursor = connect.cursor()
    cursor.execute('''select * from entity_log''')
    return cursor.fetchall()


def insert_restraunt(connect: odb.Connection, name: str, a_id: int, iine: str):
    cursor = connect.cursor()
    cursor.callproc('Restaurant_inserter', [name, a_id, iine])
    cursor.close()


def update_restraunt(connect: odb.Connection, r_id: int, r_name: str, a_id: int):
    cursor = connect.cursor()
    cursor.callproc('Update_restraunts', [r_id, r_name, a_id])
    cursor.close()


def get_view_logs(connect: odb.Connection, s_date: str, e_date: str, operation_type: str, date_format: str):
    cursor = connect.cursor()
    out_cursor = connect.cursor()
    cursor.callproc('view_logs', [s_date, e_date, operation_type, date_format, out_cursor])
    return [[i[0] for i in out_cursor.description]] + out_cursor.fetchall()


def commit(connect: odb.Connection):
    cursor = connect.cursor()
    cursor.execute('''commit''')
    cursor.close()


def insert_menu(connect: odb.Connection, res_id: int, M_name: str, meat_id: int, sauce_id: int, price: int):
    cursor = connect.cursor()
    cursor.callproc('Menu_inserter', [res_id, M_name, meat_id, sauce_id, price])
    cursor.close()


def insert_rank(connect: odb.Connection, res_id: int, menu_id: int, new_rate: int, new_rate_date: int):
    cursor = connect.cursor()
    cursor.callproc('rate_inserter', [res_id, menu_id, new_rate, new_rate_date, 'DD.MM.YYYY HH24:MI'])
    cursor.close()


def update_menu(connect: odb.Connection, menu_id: int, res_id: int, new_name: str, meat_id: int, sauce_id: int,
                new_price: int):
    cursor = connect.cursor()
    cursor.callproc('Update_menu', [menu_id, res_id, new_name, meat_id, sauce_id, new_price])
    cursor.close()


def update_rank(connect: odb.Connection, rate_id: int, menu_id: int, res_id: int, rate: int, rate_date: str):
    cursor = connect.cursor()
    cursor.callproc('Update_rate', [rate_id, menu_id, res_id, rate, rate_date])
    cursor.close()


def deleter(connect: odb.Connection, table_name: str, id_column: str, id_value: int):
    cursor = connect.cursor()
    cursor.callproc('delete_from_any_table', [table_name, id_column, id_value])
    cursor.close()


def time_walk(connect: odb.Connection, e_id: int):
    cursor = connect.cursor()
    cursor.callproc('time_walk', [e_id])
    cursor.close()
