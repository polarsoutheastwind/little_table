from datetime import datetime

from app import db


class UserLogin(db.Model):
    __tablename__ = 'users'
    username = db.Column(db.String(100), primary_key=True)
    password = db.Column(db.String(100), nullable=False)
    identity = db.Column(db.String(100), nullable=False)

    def __init__(self, username, password, identity):
        self.username = username
        self.password = password
        self.identity = identity


class User(db.Model):
    __tablename__ = "index"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    eopscore = db.Column(db.String(100), nullable=False)


class Detail(db.Model):
    __tablename__ = "label"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    homework_score = db.Column(db.String(100), nullable=False)
    test_score = db.Column(db.String(100), nullable=False)
    score = db.Column(db.String(100), nullable=False)
    end_of_period_score = db.Column(db.String(100), nullable=False)
    Submission_time_of_homework = db.Column(db.String(100), nullable=False)
    homework_time = db.Column(db.String(100), nullable=False)
    test_time = db.Column(db.String(100), nullable=False)
    Submission_time_of_test = db.Column(db.String(100), nullable=False)
    test_time_and_score = db.Column(db.String(100), nullable=False)
    sum_number_of_homework = db.Column(db.String(100), nullable=False)
    sum_page_of_homework = db.Column(db.String(100), nullable=False)
    sum_number_of_test = db.Column(db.String(100), nullable=False)
    sum_page_of_test = db.Column(db.String(100), nullable=False)
    note = db.Column(db.String(100), nullable=False)
    note_and_page = db.Column(db.String(100), nullable=False)
    Attendance_rate = db.Column(db.String(100), nullable=False)
    interaction = db.Column(db.String(100), nullable=False)
    homework_time_and_score = db.Column(db.String(100), nullable=False)


class Homework(db.Model):
    __tablename__ = "homework_data"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    homework1 = db.Column(db.String(100), nullable=False)
    homework2 = db.Column(db.String(100), nullable=False)
    homework3 = db.Column(db.String(100), nullable=False)
    homework4 = db.Column(db.String(100), nullable=False)
    homework5 = db.Column(db.String(100), nullable=False)
    homework6 = db.Column(db.String(100), nullable=False)
    homework7 = db.Column(db.String(100), nullable=False)
    homework8 = db.Column(db.String(100), nullable=False)
    homework9 = db.Column(db.String(100), nullable=False)
    homework10 = db.Column(db.String(100), nullable=False)
    homework11 = db.Column(db.String(100), nullable=False)
    homework12 = db.Column(db.String(100), nullable=False)
    average = db.Column(db.String(100), nullable=False)
    average_all = db.Column(db.String(100), nullable=False)


class Test(db.Model):
    __tablename__ = "test_data"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    test1 = db.Column(db.String(100), nullable=False)
    test2 = db.Column(db.String(100), nullable=False)
    test3 = db.Column(db.String(100), nullable=False)
    test4 = db.Column(db.String(100), nullable=False)
    test5 = db.Column(db.String(100), nullable=False)
    test6 = db.Column(db.String(100), nullable=False)
    test7 = db.Column(db.String(100), nullable=False)
    test8 = db.Column(db.String(100), nullable=False)
    test9 = db.Column(db.String(100), nullable=False)
    test10 = db.Column(db.String(100), nullable=False)
    test11 = db.Column(db.String(100), nullable=False)
    test12 = db.Column(db.String(100), nullable=False)
    test13 = db.Column(db.String(100), nullable=False)
    test14 = db.Column(db.String(100), nullable=False)
    test15 = db.Column(db.String(100), nullable=False)
    test16 = db.Column(db.String(100), nullable=False)
    test17 = db.Column(db.String(100), nullable=False)
    average = db.Column(db.String(100), nullable=False)
    average_all = db.Column(db.String(100), nullable=False)


class Rawdata(db.Model):
    __tablename__ = 'raw_data'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    class_score = db.Column(db.String(100), nullable=False)
    attend_rate = db.Column(db.String(100), nullable=False)
    Completion_rate_of_homework = db.Column(db.String(100), nullable=False)
    Completion_rate_of_test = db.Column(db.String(100), nullable=False)
    View_page_percentage_of_test = db.Column(db.String(100), nullable=False)
    View_page_percentage_of_homework = db.Column(db.String(100), nullable=False)
    note_score = db.Column(db.String(100), nullable=False)
    eopscore = db.Column(db.String(100), nullable=False)


class Average(db.Model):
    __tablename__ = 'average_all'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    test1 = db.Column(db.String(100), nullable=False)
    test2 = db.Column(db.String(100), nullable=False)
    test3 = db.Column(db.String(100), nullable=False)
    test4 = db.Column(db.String(100), nullable=False)
    test5 = db.Column(db.String(100), nullable=False)
    test6 = db.Column(db.String(100), nullable=False)
    test7 = db.Column(db.String(100), nullable=False)
    test8 = db.Column(db.String(100), nullable=False)
    test9 = db.Column(db.String(100), nullable=False)
    test10 = db.Column(db.String(100), nullable=False)
    test11 = db.Column(db.String(100), nullable=False)
    test12 = db.Column(db.String(100), nullable=False)
    test13 = db.Column(db.String(100), nullable=False)
    test14 = db.Column(db.String(100), nullable=False)
    test15 = db.Column(db.String(100), nullable=False)
    test16 = db.Column(db.String(100), nullable=False)
    test17 = db.Column(db.String(100), nullable=False)
    homework1 = db.Column(db.String(100), nullable=False)
    homework2 = db.Column(db.String(100), nullable=False)
    homework3 = db.Column(db.String(100), nullable=False)
    homework4 = db.Column(db.String(100), nullable=False)
    homework5 = db.Column(db.String(100), nullable=False)
    homework6 = db.Column(db.String(100), nullable=False)
    homework7 = db.Column(db.String(100), nullable=False)
    homework8 = db.Column(db.String(100), nullable=False)
    homework9 = db.Column(db.String(100), nullable=False)
    homework10 = db.Column(db.String(100), nullable=False)
    homework11 = db.Column(db.String(100), nullable=False)
    homework12 = db.Column(db.String(100), nullable=False)


class ConversationUser(db.Model):
    __tablename__ = 'chat_history'
    id = db.Column(db.Integer,primary_key=True)
    conversation_id = db.Column(db.Integer, nullable=False)
    message_index = db.Column(db.String(100), nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.now, index=True)
    username = db.Column(db.String(100), nullable=False)
    user_message = db.Column(db.Text, nullable=False)
    assistant_reply = db.Column(db.Text, nullable=False)


class Post(db.Model):
    __tablename__ = 'Post_data'
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, default=datetime.now, index=True)
    title = db.Column(db.String(200), nullable=False)
    body = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.String(100), nullable=False)
    numbers_of_comment = db.Column(db.Integer)
    comments = db.relationship('Comment', backref='post', lazy=True)


class Comment(db.Model):
    __tablename__ = 'Comment_data'
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow, index=True)
    body = db.Column(db.Text, nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey('Post_data.id'), nullable=False)
    user_id = db.Column(db.String(100), nullable=False)
