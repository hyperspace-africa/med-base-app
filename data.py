import sqlite3 as sql

global_email = ""
global_password = ""

def create_password():
    db = sql.connect("database.db")
    db.execute("DROP TABLE IF EXISTS login")
    db.execute("CREATE TABLE login(id INTEGER PRIMARY KEY, email TEXT NOT NULL UNIQUE, password TEXT NOT NULL)")
    db.execute("INSERT INTO login(email, password) VALUES (?, ?)", ("victorelezua@gmail.com", "12345"))
    db.commit()
    print("password done")


def add_user(email, password):
    db = sql.connect("database.db")
    try:
        db.execute("INSERT INTO login(email, password) VALUES (?, ?)", (email, password))
    except:
        print("Add user failed")
        return False
    db.commit()


def check_user(email, password):
    global global_email
    global global_password

    db = sql.connect("database.db")
    db.row_factory = sql.Row
    cursor_email = db.execute("SELECT email FROM login WHERE email=?", (email,))
    main_cursor = db.execute("SELECT email, password FROM login WHERE email=?", (email,))
    for row in cursor_email:
        if len(dict(row)) != 1:
            return False
        else:
            for nrow in main_cursor:
                global_email = dict(nrow).get("email")
                global_password = dict(nrow).get("password")

            if global_password == password and global_email == email:
                return True
            else:
                return False


def read_pass():
    db = sql.connect("database.db")
    db.row_factory = sql.Row
    cursor = db.execute("SELECT * FROM login")
    return cursor
    # for row in cursor:
    #     print(row)


def create():
    db = sql.connect('database.db')
    db.execute('DROP TABLE patients')
    db.execute("CREATE TABLE patients(id INTEGER PRIMARY KEY, first_name TEXT NOT NULL, last_name TEXT NOT NULL, "
               "dob DATETIME NOT NULL, sex TEXT NOT NULL, home_address TEXT NOT NULL, phone TEXT NOT NULL, home_town TEXT NOT NULL, "
               "city TEXT NOT NULL, state TEXT NOT NULL, marital_status INTEGER NOT NULL, cancer INTEGER NOT NULL, hepatitis_a INTEGER NOT NULL, "
               "hepatitis_b INTEGER NOT NULL, hepatitis_c INTEGER NOT NULL, tuberculosis INTEGER NOT NULL, lupus INTEGER NOT NULL, meningitis INTEGER NOT NULL, "
               "chicken_pox INTEGER NOT NULL, pneumonia INTEGER NOT NULL, diabetes INTEGER NOT NULL, anaemia INTEGER NOT NULL, phone_next_of_kin TEXT NOT NULL)")


def insert(
        fname, lname,
        dob, sex,
        home_addr, tel,
        home_town,
        city, state,
        m_status, cancer,
        hepatitis_a, hepatitis_b,
        hepatitis_c, tuberculosis,
        lupus, meningitis, chicken_pox,
        pneumonia, diabetes, anaemia, next_of_kin):
    db = sql.connect('database.db')
    db.execute("INSERT INTO patients (first_name, last_name, dob, sex, home_address, phone, home_town,"
               "city, state, marital_status, cancer, hepatitis_a,"
               "hepatitis_b, hepatitis_c,"
               "tuberculosis, lupus,"
               "meningitis, chicken_pox, pneumonia, diabetes,"
               "anaemia, phone_next_of_kin) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
               (fname, lname, dob, sex,
                home_addr, tel, home_town,
                city, state, m_status,
                cancer, hepatitis_a,
                hepatitis_b, hepatitis_c,
                tuberculosis, lupus,
                meningitis, chicken_pox, pneumonia, diabetes,
                anaemia, next_of_kin))
    db.commit()
    print("Done")


def read_users():
    db = sql.connect("database.db")
    db.row_factory = sql.Row
    cursor = db.execute("SELECT email FROM login")
    return cursor


def get_patient(name):
    db = sql.connect("database.db")
    db.row_factory = sql.Row
    cursor = db.execute("SELECT id, first_name, last_name FROM patients WHERE LOWER(first_name) = ? OR LOWER(last_name) = ?", (name.lower(), name.lower()))
    return cursor


def read_one(id):
    db = sql.connect("database.db")
    db.row_factory = sql.Row
    cursor = db.execute("SELECT * FROM patients WHERE id=? ", (id,))
    return cursor


def read():
    db = sql.connect("database.db")
    db.row_factory = sql.Row
    cursor = db.execute("SELECT * FROM patients")
    return cursor
    # for row in cursor:
    #     print(row)


read_pass()


#insert("Victor", "Elezua", "01/09/1998", "M",
#       "Umuahia", "09076282648", "Owerri",
#      "Aba", "Abia", "Single", 0, 0,
#       0, 0, 0, 0, 0, 0, 0, 0, 0, "08031356955")

#read()


print("Program finished")
