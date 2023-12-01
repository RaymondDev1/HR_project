from django.shortcuts import render

import psycopg2 as pscpg
from psycopg2 import OperationalError

f1 = open("C:\Django\hr_project\hr_app\\templates\emp_id.txt", 'r')
empl_id = int(f1.readline())
f1.close()


def create_connection(db_name, db_user, db_password, db_host, db_port):
    connection = None
    try:
        connection = pscpg.connect(
            database=db_name,
            user=db_user,
            password=db_password,
            host=db_host,
            port=db_port,
        )
        print("Connection to PostgreSQL DB successful")
    except OperationalError as e:
        print(f"The error '{e}' occurred")
    return connection


def postgre_query(connection, query, new_data):
    connection.autocommit = True
    cursor = connection.cursor()
    try:
        cursor.execute(query, new_data)
        print("Query executed successfully")
    except OperationalError as e:
        print(f"The error '{e}' occurred")


def postgre_back_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except OperationalError as e:
        print(f"The error '{e}' occurred")


def index(request):
    return render(request, "index.html")


def personal(request):
    return render(request, "personal.html")


def add_employer(request):
    connect_postgre = create_connection("hr", "postgres", "jerry1", "127.0.0.1", "5432")
    rez_tup = postgre_back_query(connect_postgre, "select positions.position_code from positions")
    rez_list = []
    for zap in rez_tup:
        rez_list.append(list(zap)[0])
    add_rez = {'rez': rez_list}
    return render(request, "add_employer.html", add_rez)


def employer_list(request):
    connect_postgre = create_connection("hr", "postgres", "jerry1", "127.0.0.1", "5432")
    rez_tup = postgre_back_query(connect_postgre, "select * from employer")
    rez_list = []
    for zap in rez_tup:
        temp = list(zap)
        tmp = temp[1]
        temp[1] = temp[2]
        temp[2] = tmp
        rez_list.append(temp)
    add_rez = {'rez': rez_list}
    return render(request, "employer_list.html", add_rez)


def select_edit_employer(request):
    connect_postgre = create_connection("hr", "postgres", "jerry1", "127.0.0.1", "5432")
    rez_tup = postgre_back_query(connect_postgre, "select employer.emp_id from employer")
    rez_list = []
    for zap in rez_tup:
        rez_list.append(list(zap)[0])
    add_rez = {'rez': rez_list}
    return render(request, "select_edit_employer.html", add_rez)


def edit_employer(request):
    em_id = request.POST.get("employer_id")
    f1 = open("C:\Django\hr_project\hr_app\\templates\selected_id.txt", "w")
    f1.write(str(em_id))
    f1.close()
    connect_postgre = create_connection("hr", "postgres", "jerry1", "127.0.0.1", "5432")
    rez_tup = postgre_back_query(connect_postgre, "select positions.position_code from positions")
    rez_list = []
    for zap in rez_tup:
        rez_list.append(list(zap)[0])
    add_rez = {'rez': rez_list}
    return render(request, "edit_employer.html", add_rez)


def end_edit_employer(request):
    f1 = open("C:\Django\hr_project\hr_app\\templates\selected_id.txt", 'r')
    empl_id = int(f1.readline())
    f1.close()

    em_fn = request.POST.get("employer_fname")
    em_ln = request.POST.get("employer_lname")
    em_mn = request.POST.get("employer_mname")
    em_ps = request.POST.get("employer_position")
    em_dt = request.POST.get("employer_date")
    list1 = []

    list1.append(str(em_fn))
    list1.append(str(em_ln))
    list1.append(str(em_mn))
    list1.append(str(em_ps))
    list1.append(str(em_dt))
    list1.append(int(empl_id))
    ins_val = tuple(list1)

    connect_postgre = create_connection("hr", "postgres", "jerry1", "127.0.0.1", "5432")
    postgre_query(connect_postgre,
                  "update employer set fname=%s, lname=%s, mname=%s, position_code=%s, start_date=%s where employer.emp_id=%s",
                  ins_val)

    add_rez = {'ef': em_fn, 'el': em_ln, 'em': em_mn, 'ed': em_dt}
    return render(request, "end_edit_employer.html", add_rez)


def delete_employer(request):
    connect_postgre = create_connection("hr", "postgres", "jerry1", "127.0.0.1", "5432")
    rez_tup = postgre_back_query(connect_postgre, "select employer.emp_id from employer")
    rez_list = []
    for zap in rez_tup:
        rez_list.append(list(zap)[0])
    add_rez = {'rez': rez_list}
    return render(request, "delete_employer.html", add_rez)


def end_delete_employer(request):
    empl_id = request.POST.get("employer_id")
    list1 = []
    list1.append(int(empl_id))
    ins_val = tuple(list1)

    connect_postgre = create_connection("hr", "postgres", "jerry1", "127.0.0.1", "5432")
    postgre_query(connect_postgre, "delete from employer where employer.emp_id=%s", ins_val)
    add_rez = {'em_id': empl_id}
    return render(request, "end_delete_employer.html", add_rez)


def managing_job_directory(request):
    return render(request, "managing_job_directory.html")


def add_position(request):
    return render(request, "add_position.html")


def add_position_info(request):
    tp_n = request.POST.get("title_pos_name")
    cp_n = request.POST.get("code_pos_name")

    list1 = []
    list1.append(str(cp_n))
    list1.append(str(tp_n))
    ins_val = tuple(list1)

    connect_postgre = create_connection("hr", "postgres", "jerry1", "127.0.0.1", "5432")
    postgre_query(connect_postgre, "insert into positions values (%s, %s)", ins_val)

    add_rez = {'tpn': tp_n, 'cp_n': cp_n}
    return render(request, "add_position_info.html", add_rez)


def position_list(request):
    connect_postgre = create_connection("hr", "postgres", "jerry1", "127.0.0.1", "5432")
    rez_tup = postgre_back_query(connect_postgre, "select * from positions")
    rez_list = []
    for zap in rez_tup:
        rez_list.append(list(zap))
    add_rez = {'rez': rez_list}
    return render(request, "position_list.html", add_rez)


def select_edit_position(request):
    connect_postgre = create_connection("hr", "postgres", "jerry1", "127.0.0.1", "5432")
    rez_tup = postgre_back_query(connect_postgre, "select positions.position_code from positions")
    rez_list = []
    for zap in rez_tup:
        rez_list.append(list(zap)[0])
    add_rez = {'rez': rez_list}
    return render(request, "select_edit_position.html", add_rez)


def edit_position(request):
    pos_code = request.POST.get("position_code")
    f1 = open("C:\Django\hr_project\hr_app\\templates\selected_pos_code.txt", "w")
    f1.write(str(pos_code))
    f1.close()
    return render(request, "edit_position.html")


def end_edit_position(request):
    f1 = open("C:\Django\hr_project\hr_app\\templates\selected_pos_code.txt", 'r')
    pos_code = f1.readline()
    f1.close()

    tp_n = request.POST.get("title_pos_name")

    list1 = []
    list1.append(str(tp_n))
    list1.append(str(pos_code))
    ins_val = tuple(list1)

    connect_postgre = create_connection("hr", "postgres", "jerry1", "127.0.0.1", "5432")
    postgre_query(connect_postgre, "update positions set position_name=%s where positions.position_code=%s", ins_val)
    add_rez = {'tpn': tp_n, 'cp_n': pos_code}
    return render(request, "end_edit_position.html", add_rez)


def delete_position(request):
    connect_postgre = create_connection("hr", "postgres", "jerry1", "127.0.0.1", "5432")
    rez_tup = postgre_back_query(connect_postgre, "select positions.position_code from positions")
    rez_list = []
    for zap in rez_tup:
        rez_list.append(list(zap)[0])
    add_rez = {'rez': rez_list}
    return render(request, "delete_position.html", add_rez)


def end_delete_position(request):
    pos_code = request.POST.get("code_pos")
    list1 = []
    list1.append(pos_code)
    ins_val = tuple(list1)

    connect_postgre = create_connection("hr", "postgres", "jerry1", "127.0.0.1", "5432")
    postgre_query(connect_postgre, "delete from positions where positions.position_code=%s", ins_val)
    add_rez = {'id': pos_code}
    return render(request, "end_delete_position.html", add_rez)


def add_info(request):
    global empl_id
    empl_id = empl_id + 1
    em_fn = request.POST.get("employer_fname")
    em_ln = request.POST.get("employer_lname")
    em_mn = request.POST.get("employer_mname")
    em_ps = request.POST.get("employer_position")
    em_dt = request.POST.get("employer_date")

    list1 = []
    list1.append(int(empl_id))
    list1.append(str(em_fn))
    list1.append(str(em_ln))
    list1.append(str(em_mn))
    list1.append(str(em_ps))
    list1.append(str(em_dt))
    ins_val = tuple(list1)

    connect_postgre = create_connection("hr", "postgres", "jerry1", "127.0.0.1", "5432")
    postgre_query(connect_postgre, "insert into employer values (%s,%s,%s,%s,%s,%s)", ins_val)

    f1 = open("C:\Django\hr_project\hr_app\\templates\emp_id.txt", "w")
    f1.write(str(empl_id))
    f1.close()

    add_rez = {'ef': em_fn, 'el': em_ln, 'em': em_mn, 'ed': em_dt}
    return render(request, "add_info.html", add_rez)
