from flask import Flask, request
from werkzeug.exceptions import abort
from werkzeug.utils import redirect

from data db_session, news_api
from data.users import User
from data.news import News
from flask import render_template
from forms.user import RegisterForm, LoginForm
from forms.news import NewsForm
from flask_login import LoginManager, login_user, logout_user, login_required, current_user

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


def main():
    db_session.global_init("db/blogs.db")
    app.register_blueprint(news_api.blueprint)
    app.run()

    # ввод данных
    job = Jobs()
    db_sess = db_session.create_session()
    db_sess.add(job)
    job.team_leader = 1
    job.job = "deploymen of residential modules 1 and 2"
    job.work_size = 15
    job.collaborators = "2", "3"
    job.start_date = "now"
    job.is_finished = False
    db_sess.commit()
    # вывод данных
    db_sess = db_session.create_session()
    user = db_sess.query(User).first()
    # print(user.name)
    for user in db_sess.query(User).all():
        print(user)


if __name__ == '__main__':
    main()
