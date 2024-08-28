from app import cur, conn
from class_data import UserLogin


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
