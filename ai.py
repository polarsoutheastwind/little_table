import dashscope
from dashscope import Generation
from dashscope.api_entities.dashscope_response import Role
from app import session, cur, db
from class_data import ConversationUser

dashscope.api_key = "sk-10fb1eb7ce4b47ad8b5f81ac0647739f"


def get_new_conversation_id():
    # 获取当前最大 conversation_id，并返回新的 conversation_id
    cur.execute("SELECT MAX(conversation_id) FROM chat_history")
    max_id = cur.fetchone()[0]
    return (max_id or 0) + 1


def ai_test_data(user_message):
    username = session['user_now']['username']
    # 检查当前会话是否已经存在 conversation_id，如果没有则创建新的
    if 'conversation_id' not in session:
        session['conversation_id'] = get_new_conversation_id()
        session['message_index'] = 0

    # 增加 message_index 计数
    session['message_index'] += 1

    if user_message:
        # 这里调用了 AI 模型
        assistant_reply = generate_message(user_message)
        conversation_user = ConversationUser(conversation_id=session['conversation_id'],
                                             message_index=session['message_index'],
                                             username=username, user_message=user_message,
                                             assistant_reply=assistant_reply)
        db.session.add(conversation_user)
        db.session.commit()
        db.session.refresh(conversation_user)
        return assistant_reply


def end_conversation():
    session.pop('conversation_id', None)
    session.pop('message_index', None)
    session.pop('data', None)


def generate_message(send_message):
    session['data'].append({'role': Role.USER, 'content': send_message})
    whole_message = ''
    responses = Generation.call(Generation.Models.qwen_plus, messages=session['data'], result_format='message'
                                , stream=True, incremental_output=True)
    for response in responses:
        whole_message += response.output.choices[0]['message']['content']
    session['data'].append({'role': 'assistant', 'content': whole_message})
    return whole_message
