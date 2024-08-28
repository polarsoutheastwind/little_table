def grade1(shu):
    shu = int(shu)
    if shu == 1:
        return "高"
    else:
        return "低"


def evaluate(a, b, c, d):
    s = int(a) + int(b) + int(c) + int(d)
    if s == 4:
        return "该生多项成绩优秀，是一名优等生"
    elif s == 3:
        return "该生虽然多项成绩优秀，但任然有欠缺，是一名中上层次的学生"
    elif s == 2:
        return "该生成绩好坏参半，欠缺略多，是一名中下层次的学生"
    else:
        return "该生有多项欠缺，比较糟糕，是一名下层次的学生"


def grade2(shu):
    shu = int(shu)
    if shu == 1:
        return "快"
    else:
        return "慢"


def grade3(shu):
    shu = int(shu)
    if shu == 1:
        return "早"
    else:
        return "晚"


def grade4(shu):
    shu = int(shu)
    if shu == 1:
        return "多"
    else:
        return "少"


def time_score(time, score, evaluation):
    time = int(time)
    score = int(score)
    evaluation = int(evaluation)
    if time > 0 and score > 0:
        return "完成时间和分数都非常优秀"
    elif time > 0 and score == 0 and evaluation == 1:
        return "完成时间非常快，但是成绩不高，存在敷衍"
    elif time > 0 and score == 0 and evaluation == 0:
        return "完成时间快，但是成绩不高，有点粗心"
    elif time == 0 and score > 0 and evaluation == 1:
        return "完成时间慢，但成绩较高"
    elif time == 0 and score > 0 and evaluation == 0:
        return "完成时间慢，但成绩略高，对待作业不用心"
    else:
        return "该生没有认真对待学习作业"


def note_page(note, page, note_and_page, score):
    note_and_page = int(note_and_page)
    note = int(note)
    page = int(page)
    score = int(score)
    if note > 0 and page > 0:
        return "该生观看页数多，笔记效果好"
    elif note > 0 and page == 0:
        if note_and_page == 1:
            return "该生笔记效果非常好，但是观看页面少，在课堂可能比较专注"
        else:
            return "该生笔记效果好，但任然有欠缺"
    elif note == 0 and page > 0:
        if note_and_page == 1:
            return "该生笔记效果一般，但观看较多页面，可能在期末期间复习时通过观看课件复习"
        elif note_and_page == 0 and score == 0:
            return "该生笔记效果一般，但观看页面较多，成绩一般，可能学习动机比较低"
        elif note_and_page == 0 and score == 1:
            return "该生笔记效果一般，但观看页面较多，成绩较好，除了笔记有自己的学习方法"
    else:
        return "该生没有注重笔记记录，课后也较少观看课件"


def score_percentage(data):
    s = float(data / 100)
    return s


def note_percentage(data):
    s = float(data / 20)
    return s


def percen(data):
    m1 = round(float(data) * 100, 2)
    m2 = "%.2f%%" % m1
    return m2


def compare1(data1, data2):
    if data1 > data2:
        return "高"
    elif data1 == data2:
        return "平"
    else:
        return "低"


def compare2(data1, data2):
    if data1 > data2:
        return "#229453"
    elif data1 == data2:
        return "#fc8c23"
    else:
        return "#ed3321"


def arr_message(result):
    set_result = [
        {
            'conversation_id': r[0],
            'message_index': r[1],
            'timestamp': r[2].strftime('%Y-%m-%d %H:%M:%S'),  # 转为字符串
            'username': r[3],
            'user_message': r[4],
            'assistant_reply': r[5]
        }
        for r in result
    ]
    return set_result
