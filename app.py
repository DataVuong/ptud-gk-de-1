from flask import Flask, render_template, request, redirect, url_for, flash
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, EqualTo

app = Flask(__name__)
app.secret_key = "supersecretkey"

# Cấu hình Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

# Danh sách tài khoản (tạm thời lưu trong bộ nhớ)
users = {
    "admin": {"password": generate_password_hash("admin123"), "role": "admin"}
}

# Lớp User để sử dụng với Flask-Login
class User(UserMixin):
    def __init__(self, username, role):
        self.id = username
        self.role = role

@login_manager.user_loader
def load_user(username):
    if username in users:
        return User(username, users[username]["role"])
    return None

# Form đăng ký
class RegisterForm(FlaskForm):
    username = StringField("Tên đăng nhập", validators=[InputRequired(), Length(min=3, max=20)])
    password = PasswordField("Mật khẩu", validators=[InputRequired(), Length(min=6)])
    confirm_password = PasswordField("Nhập lại mật khẩu", validators=[InputRequired(), EqualTo("password")])
    submit = SubmitField("Đăng ký")

# Form đăng nhập
class LoginForm(FlaskForm):
    username = StringField("Tên đăng nhập", validators=[InputRequired(), Length(min=3, max=20)])
    password = PasswordField("Mật khẩu", validators=[InputRequired()])
    submit = SubmitField("Đăng nhập")

# Danh sách bài viết với bình luận
posts = [
    {"id": 1, "title": "Cách Học Lập Trình Hiệu Quả", "image": "https://picsum.photos/600/400?random=1",
     "content": "Học lập trình hiệu quả với Python!", "followers": 10, "comments": []},
    {"id": 2, "title": "Những Nguyên Tắc Vàng Khi Code", "image": "https://picsum.photos/600/400?random=2",
     "content": "Tuân theo các nguyên tắc SOLID để viết code tốt hơn.", "followers": 25, "comments": []},
    {"id": 3, "title": "Flask: Framework Nhẹ Nhất Cho Web", "image": "https://picsum.photos/600/400?random=3",
     "content": "Học Flask để xây dựng ứng dụng web.", "followers": 15, "comments": []}
]

@app.route("/")
def home():
    return render_template("index.html", posts=posts)

@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        if username in users:
            flash("Tên đăng nhập đã tồn tại!", "danger")
        else:
            users[username] = {"password": generate_password_hash(password), "role": "user"}
            flash("Đăng ký thành công!", "success")
            return redirect(url_for("login"))
    return render_template("register.html", form=form)

@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        if username in users and check_password_hash(users[username]["password"], password):
            login_user(User(username, users[username]["role"]))
            flash("Đăng nhập thành công!", "success")
            return redirect(url_for("home"))
        else:
            flash("Sai tên đăng nhập hoặc mật khẩu!", "danger")
    return render_template("login.html", form=form)

@app.route("/logout")
@login_required
def logout():
    logout_user()
    flash("Đăng xuất thành công!", "success")
    return redirect(url_for("login"))

@app.route("/follow/<int:post_id>")
@login_required
def follow(post_id):
    for post in posts:
        if post["id"] == post_id:
            post["followers"] += 1
            break
    return redirect(url_for("home"))

@app.route("/post/<int:post_id>", methods=["GET", "POST"])
@login_required
def post_detail(post_id):
    post = next((p for p in posts if p["id"] == post_id), None)
    if not post:
        return "Bài viết không tồn tại!", 404

    if request.method == "POST":
        comment_text = request.form.get("comment")
        if comment_text:
            post["comments"].append({"user": current_user.id, "text": comment_text})  # ✅ Cập nhật: Admin có thể bình luận

    return render_template("post_detail.html", post=post)

@app.route("/delete_comment/<int:post_id>/<int:comment_index>")
@login_required
def delete_comment(post_id, comment_index):
    post = next((p for p in posts if p["id"] == post_id), None)
    if post and 0 <= comment_index < len(post["comments"]):
        if current_user.role == "admin":  # ✅ Admin có quyền xóa bình luận
            del post["comments"][comment_index]
    return redirect(url_for("post_detail", post_id=post_id))

@app.route("/admin")
@login_required
def admin():
    if current_user.role != "admin":
        return "Truy cập bị từ chối!", 403
    return render_template("admin.html", users=users)

if __name__ == "__main__":
    app.run(debug=True)
