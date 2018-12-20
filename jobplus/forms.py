from flask_wtf import FlaskForm
from wtforms import (StringField, PasswordField, SubmitField, BooleanField,
                     ValidationError, IntegerField, FileField)
from wtforms.validators import Length, Email, DataRequired, EqualTo, URL
from jobplus.models import db, User, Company


class LoginForm(FlaskForm):
    email = StringField('邮箱', validators=[DataRequired(), Email(), Length(1, 254)])
    password = PasswordField('密码', validators=[DataRequired(), Length(6, 24)])
    remember_me = BooleanField('记住我')
    submit = SubmitField('提交')

    def validate_email(self, field):
        if field.data and not User.query.filter_by(email=field.data).first():
            raise ValidationError('该邮箱未注册')

    def validate_password(self, field):
        user = User.query.filter_by(email=self.email.data).first()
        if user and not user.check_pwd(field.data):
            raise ValidationError('密码错误')


class RegisterForm(FlaskForm):
    # username = StringField('用户名', validators=[DataRequired(), Length(1, 10)])
    email = StringField('邮箱', validators=[DataRequired(), Email(), Length(1, 254)])
    password = PasswordField('密码', validators=[DataRequired(), Length(6, 24)])
    repeat_password = PasswordField('重复密码', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('提交')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('该邮箱已经被注册')

    # def validate_username(self, field):
    #     if User.query.filter_by(username=field.data).first():
    #         raise ValidationError('这个名字已经被注册了')

    def create_user(self):
        # user = User(email=self.email.data, password=self.password.data)
        user = User()
        user.username = self.usename.data
        user.emil = self.email.data
        user.password = self.password.data
        db.session.add(user)
        db.session.commit()

    def create_boss(self):
        # user = User(email=self.email.data, password=self.password.data, role=20)
        user = User()
        user.email = self.emal.data
        user.password = self.password.data
        user.role = 20
        db.session.add(user)
        db.session.commit()


class UserForm(FlaskForm):
    username = StringField('用户名', validators=[DataRequired(), Length(3, 24)])
    phone_number = IntegerField('手机号', validators=[DataRequired()])
    work_year = IntegerField("工作经验", validators=[DataRequired()])
    # work_resume = FileField('简历',validators=[Required()])
    # company=StringField('公司')
    submit = SubmitField('提交')

    def complete(self, id):
        user = User.query.filter_by(id=id).first()
        # user.work_resume=self.work_resume.data
        user.username = self.username.data
        user.phone_number = self.phone_number.data
        user.work_year = self.work_year.data
        # user.company=self.company.data
        db.session.add(user)
        db.session.commit()


class BossForm(FlaskForm):
    email = StringField('邮箱', validators=[DataRequired(), Email()])
    name = StringField('企业名称', validators=[DataRequired(), Length(3, 50)])
    address = StringField('公司地址', validators=[DataRequired()])
    net_site = StringField('网站链接', validators=[DataRequired(), URL()])
    logo = StringField("logo图片链接", validators=[DataRequired(), URL()])
    introduce = StringField("一句话简介", validators=[DataRequired()])
    detail = StringField("详细介绍")
    financing = StringField("融资")
    company_field = StringField("领域")
    submit = SubmitField('提交')

    def complete(self, id):
        # TODO
        pass
