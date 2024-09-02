from app import cur, conn
from class_data import UserLogin
from collections import Counter


def is_existed(username, password):
    sql = "SELECT * FROM users WHERE username ='%s' and password ='%s'" % (username, password)
    cur.execute(sql)
    result = cur.fetchall()
    if len(result) == 0:
        return False
    else:
        return True


def user_login(username):
    sql = "SELECT * FROM users WHERE username ='%s'" % username
    cur.execute(sql)
    result = cur.fetchall()
    return UserLogin(username, password=result[0][1], identity=result[0][2])


def is_id_existed(search_id):
    sql = "SELECT * FROM raw_data where id='%s'" % search_id
    cur.execute(sql)
    result = cur.fetchall()
    if len(result) == 0:
        return False
    else:
        return True


def increase_comment(post_id):
    sql = "UPDATE post_data SET numbers_of_comment=numbers_of_comment+1 where id='%d'" % post_id
    cur.execute(sql)
    conn.commit()


def get_chat_history_with_time(user_id, start_time, end_time):
    sql = """
        SELECT conversation_id, message_index, timestamp, username, user_message, assistant_reply 
        FROM chat_history 
        WHERE username = %s AND timestamp BETWEEN %s AND %s
        """
    params = (user_id, start_time, end_time)
    cur.execute(sql, params)
    result = cur.fetchall()
    return result


def get_chat_history(user_id):
    sql = """
        SELECT conversation_id, message_index, timestamp, username, user_message, assistant_reply 
        FROM chat_history 
        WHERE username = %s
        """
    cur.execute(sql, user_id)
    result = cur.fetchall()
    return result


def select_user():
    sql = "SELECT* FROM name_id"
    cur.execute(sql)
    res = cur.fetchall()
    return res


def sign_in(user_id):
    sql = "SELECT * FROM course_sign_in WHERE id='%s' " % user_id
    cur.execute(sql)
    result = cur.fetchall()
    return result[0]


def all_score(user_id):
    sql = "SELECT * FROM course_scores where id='%s' " % user_id
    cur.execute(sql)
    result = cur.fetchall()
    return result[0]


def select_user_id():
    result = select_user()
    user_id = [item[0] for item in result]
    return user_id


def select_user_name():
    result = select_user()
    user_name = [item[1] for item in result]
    return user_name


def sign_in_count(course_id):
    result = []
    user_id = select_user_id()
    for item in user_id:
        result.append(sign_in(item)[course_id])
    result = Counter(result)
    return result


def all_score_sort(course_id):
    all_score_result = []
    user_id = select_user_id()
    user_name = select_user_name()
    for item in range(len(user_id)):
        all_score_result.append(
            {"stu_id": user_id[item], "stu_name": user_name[item], "score": all_score(user_id[item])[course_id]})
    all_score_result.sort(key=lambda x: x['score'], reverse=True)
    return all_score_result


def select_course_name():
    name = []
    sql = "select * from course_name"
    cur.execute(sql)
    result = cur.fetchall()
    for item in result:
        name.append({"index": item[0], "name": item[1]})
    return name
