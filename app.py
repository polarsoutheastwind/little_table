import pymysql
from flask import Flask, render_template, request, redirect, url_for, session, jsonify, flash, send_from_directory
from flask_sqlalchemy import SQLAlchemy
import os
from simple_fuc import grade1, evaluate, grade2, time_score, grade3, grade4, note_page, score_percentage, \
    note_percentage, percen, compare1, compare2, arr_message

app = Flask(__name__)
app.secret_key = '123456'
conn = pymysql.connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    password='root',
    database='innovation competition'
)
cur = conn.cursor()

HOSTNAME = "127.0.0.1"
PORT = 3306
USERNAME = "root"
PASSWORD = "root"
DATABASE = "innovation competition"
app.config['SQLALCHEMY_DATABASE_URI'] = (f"mysql+pymysql://{USERNAME}:{PASSWORD}@{HOSTNAME}:{PORT}/{DATABASE}?charset"
                                         f"=utf8mb4&autocommit=true")
db = SQLAlchemy(app)

UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)
from class_data import User, Average, Detail, Rawdata, Homework, Test, Post, Comment
from sql_fuc import is_id_existed, is_existed, user_login, increase_comment, get_chat_history_with_time, \
    get_chat_history
from ai import ai_test_data, end_conversation

with app.app_context():
    db.create_all()


@app.route('/')
def index():
    return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if is_existed(username, password):
            user_new = user_login(username=username)
            session['user_now'] = {'username': username, 'identity': user_new.identity}
            session["data"] = []
            if user_new.identity == "administrators" or user_new.identity == "teacher":
                return redirect('/student/1')
            elif user_new.identity == "student":
                return redirect(url_for('detail', stu_id=user_new.username))
        else:
            login_massage = "登陆失败，请重新输入账号密码"
            return render_template('login.html', message=login_massage)
    return render_template("login.html")


@app.route("/login_out", methods=['GET', 'POST'])
def login_out():
    if request.method == 'POST':
        session.clear()
        return redirect('/login')
    return render_template("login_out.html")


@app.route("/student/<int:page>", methods=['GET', 'POST'])
def student(page=None):
    if session["user_now"]['identity'] == 'student':
        return redirect(url_for('detail', stu_id=session["user_now"]['username']))
    if page is None:  # 如果没有page则显示第一页
        page = 1
    page_data = db.session.query(User).paginate(page=page, per_page=10, max_per_page=15)
    return render_template("student.html", page_data=page_data)


@app.route("/homework", methods=["GET", "POST"])
def homework1():
    if session["user_now"]['identity'] == 'student':
        return redirect(url_for('detail', stu_id=session["user_now"]['username']))
    all_students_homework = db.session.query(Homework).all()
    stu_homework = []
    n = 0
    num_students = []
    name_student = []
    for per_homework in all_students_homework:
        dict_homework = [int(per_homework.id),
                         [per_homework.homework1, per_homework.homework2, per_homework.homework3,
                          per_homework.homework4, per_homework.homework5, per_homework.homework6,
                          per_homework.homework7, per_homework.homework8, per_homework.homework9,
                          per_homework.homework10, per_homework.homework11, per_homework.homework12,
                          per_homework.average]]
        stu_homework.append(dict_homework)
        name_student.append(int(per_homework.id))
        num_students.append(int(n))
        n += 1
    return render_template("homework.html", stu_homework=stu_homework, num_students=num_students,
                           name_student=name_student)


@app.route("/test", methods=["GET", "POST"])
def test1():
    if session["user_now"]['identity'] == 'student':
        return redirect(url_for('detail', stu_id=session["user_now"]['username']))
    all_students_test = db.session.query(Test).all()
    stu_test = []
    n = 0
    num_students = []
    name_student = []
    for per_test in all_students_test:
        dict_test = [int(per_test.id),
                     [per_test.test1, per_test.test2, per_test.test3, per_test.test4, per_test.test5, per_test.test6,
                      per_test.test7, per_test.test8, per_test.test9, per_test.test10, per_test.test11, per_test.test12,
                      per_test.test13, per_test.test14, per_test.test15, per_test.test16, per_test.test17,
                      per_test.average]]
        stu_test.append(dict_test)
        name_student.append(int(per_test.id))
        num_students.append(int(n))
        n += 1
    return render_template("test.html", stu_test=stu_test, name_student=name_student,
                           num_students=num_students)


@app.route("/all_detail", methods=['GET', 'POST'])
def all_detail():
    if session["user_now"]['identity'] == 'student':
        return redirect(url_for('detail', stu_id=session["user_now"]['username']))
    all_students_detail = db.session.query(Rawdata).all()
    stu_detail = []
    n = 0
    num_students = []
    name_student = []
    for per_detail in all_students_detail:
        dict_detail = [int(per_detail.id), per_detail.attend_rate, per_detail.class_score,
                       per_detail.Completion_rate_of_homework, per_detail.Completion_rate_of_test,
                       per_detail.View_page_percentage_of_homework, per_detail.View_page_percentage_of_test,
                       per_detail.eopscore, per_detail.note_score]
        stu_detail.append(dict_detail)
        name_student.append(int(per_detail.id))
        num_students.append(int(n))
        n += 1
    return render_template("all_detail.html", stu_detail=stu_detail, name_student=name_student,
                           num_students=num_students)


@app.route("/detail/id=<int:stu_id>", methods=['GET', 'POST'])
def detail(stu_id=None):
    detail_data = db.session.query(Detail).filter_by(id=stu_id).first()
    return render_template("detail.html", stu_id=stu_id, detail_data=detail_data, grade1=grade1,
                           evaluate=evaluate, grade2=grade2, time_score=time_score, grade3=grade3, grade4=grade4,
                           note_page=note_page)


@app.route("/rawdata/id=<int:stu_id>", methods=['GET', 'POST'])
def rawdata(stu_id=None):
    raw_data = db.session.query(Rawdata).filter_by(id=stu_id).first()
    homework_data = db.session.query(Homework).filter_by(id=stu_id).first()
    test_data = db.session.query(Test).filter_by(id=stu_id).first()
    average_all = db.session.query(Average).filter_by(id=stu_id).first()
    user = db.session.query(User).filter_by(id=stu_id).first()
    data1 = [raw_data.attend_rate, raw_data.class_score, raw_data.Completion_rate_of_homework,
             raw_data.Completion_rate_of_test, raw_data.View_page_percentage_of_homework,
             raw_data.View_page_percentage_of_test, raw_data.eopscore, raw_data.note_score]
    homework = [homework_data.homework1, homework_data.homework2, homework_data.homework3,
                homework_data.homework4, homework_data.homework5, homework_data.homework6,
                homework_data.homework7, homework_data.homework8, homework_data.homework9,
                homework_data.homework10, homework_data.homework11, homework_data.homework12,
                homework_data.average]
    homework_average = [average_all.homework1, average_all.homework2, average_all.homework3,
                        average_all.homework4, average_all.homework5, average_all.homework6,
                        average_all.homework7, average_all.homework8, average_all.homework9,
                        average_all.homework10, average_all.homework11, average_all.homework12,
                        homework_data.average_all]
    test = [test_data.test1, test_data.test2, test_data.test3, test_data.test4, test_data.test5,
            test_data.test6, test_data.test7, test_data.test8, test_data.test9, test_data.test10,
            test_data.test11, test_data.test12, test_data.test13, test_data.test14, test_data.test15,
            test_data.test16, test_data.test17, test_data.average]
    test_average = [average_all.test1, average_all.test2, average_all.test3, average_all.test4,
                    average_all.test5, average_all.test6, average_all.test7, average_all.test8,
                    average_all.test9, average_all.test10, average_all.test11, average_all.test12,
                    average_all.test13, average_all.test14, average_all.test15, average_all.test16,
                    average_all.test17, test_data.average_all]
    return render_template("rawdata.html", stu_id=stu_id, raw_data=raw_data, score_percentage=score_percentage,
                           note_percentage=note_percentage, percen=percen, homework_data=homework_data,
                           test_data=test_data, average_all=average_all, compare2=compare2, compare1=compare1,
                           data1=data1, user=user, homework=homework, homework_average=homework_average,
                           test_average=test_average, test=test)


@app.route("/compare/id=<int:stu_id>", methods=['GET', 'POST'])
def compare(stu_id=None):
    if session["user_now"]['identity'] == 'student':
        return redirect(url_for('detail', stu_id=session["user_now"]['username']))
    stu1 = db.session.query(Rawdata).filter_by(id=stu_id).first()
    user1 = db.session.query(User).filter_by(id=stu_id).first()
    stu2 = stu1
    user2 = user1
    data1 = [stu1.eopscore, stu1.attend_rate, stu1.class_score,
             stu1.Completion_rate_of_homework, stu1.Completion_rate_of_test,
             stu1.View_page_percentage_of_homework, stu1.View_page_percentage_of_test,
             stu1.note_score]
    data2 = data1
    if request.method == 'POST':
        search_id = request.form.get('search_id')
        if is_id_existed(search_id):
            stu2 = db.session.query(Rawdata).filter_by(id=search_id).first()
            user2 = db.session.query(User).filter_by(id=search_id).first()
            data2 = [stu2.eopscore, stu2.attend_rate, stu2.class_score,
                     stu2.Completion_rate_of_homework, stu2.Completion_rate_of_test,
                     stu2.View_page_percentage_of_homework, stu2.View_page_percentage_of_test,
                     stu2.note_score]
            render_template("compare.html", stu2=stu2, user2=user2, data2=data2,
                            stu1=stu1, user1=user1, data1=data1)
        else:
            fail_massage = "没有找到该学生,请重试"
            return render_template("compare.html", stu_id=stu_id, message=fail_massage,
                                   stu1=stu1, user1=user1, data1=data1,
                                   user2=user2, data2=data2, stu2=stu2)
    return render_template("compare.html", stu_id=stu_id, stu1=stu1, user1=user1, data1=data1,
                           stu2=stu2, user2=user2, data2=data2)


@app.route("/ai_testing", methods=['POST', 'GET'])
def ai_testing():
    bot_message = "这是ai回复"
    if request.method == 'POST':
        user_message = request.json.get('user_message')  # 获取JSON中的用户消息
        data = request.json.get('data')
        if data == '结束对话':
            end_conversation()
        elif not data:
            if not user_message:
                return jsonify({'reply': "输入为空，重新提交"})  # 返回一个JSON响应
            # 根据用户消息生成回复
            bot_message = ai_test_data(user_message)
            return jsonify({'reply': bot_message})  # 返回AI的回复给前端
    return render_template("ai_testing.html", bot_message=bot_message)


@app.route('/dialogue_history', methods=['GET', 'POST'])
def dialogue_history():
    result = []
    if request.method == 'POST':
        if session['user_now']['identity'] == "administrators" or session['user_now']['identity'] == "teacher":
            data = request.json  # 确保数据被正确接收
            username = data.get('username')
            start_time = data.get('start_time')
            end_time = data.get('end_time')
            if start_time and end_time:
                result = get_chat_history_with_time(username, start_time, end_time)
            else:
                result = get_chat_history(username)
        elif session['user_now']['identity'] == "student":
            start_time = request.json.get('start_time')
            end_time = request.json.get('end_time')
            if start_time and end_time:
                result = get_chat_history_with_time(session['user_now']['username'], start_time, end_time)
            else:
                result = get_chat_history(session['user_now']['username'])
        set_result = jsonify(arr_message(result))
        return set_result
    return render_template("dialogue_history.html")


@app.route("/refresh", methods=['POST', 'GET'])
def refresh():
    return redirect(url_for('ai_testing'))


@app.route("/post", methods=['POST', 'GET'])
def post():
    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        new_post = Post(title=title, body=body, user_id=session['user_now']['username'], numbers_of_comment=0)
        db.session.add(new_post)
        db.session.commit()
        flash('帖子创建成功！')

        return redirect(url_for('post'))

    all_posts = Post.query.order_by(Post.timestamp.desc()).all()
    return render_template('post_list.html', posts=all_posts)


@app.route('/post/<int:post_id>', methods=['GET', 'POST'])
def post_detail(post_id=None):
    now_post = Post.query.get_or_404(post_id)
    if request.method == 'POST':
        body = request.form['body']
        new_comment = Comment(body=body, post_id=now_post.id, user_id=session['user_now']['username'])
        db.session.add(new_comment)
        db.session.commit()
        flash('评论添加成功！')
        increase_comment(now_post.id)
        return redirect(url_for('post_detail', post_id=now_post.id))

    return render_template('post_detail.html', post=now_post)


@app.route('/resource', methods=['GET', 'POST'])
def resource():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('没有文件部分')
            return redirect(request.url)

        file = request.files['file']

        if file.filename == '':
            flash('没有选择文件')
            return redirect(request.url)

        if file:
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
            flash('文件上传成功')
            return redirect(request.url)

    files = os.listdir(app.config['UPLOAD_FOLDER'])
    return render_template('resource.html', files=files)


@app.route('/download/<filename>')
def download_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)


if __name__ == '__main__':
    app.run()
