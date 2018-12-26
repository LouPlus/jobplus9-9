from flask_wtf import FlaskForm
from wtforms import (StringField, PasswordField, SubmitField, BooleanField,
                     ValidationError, IntegerField, FileField)
from wtforms.validators import Length, Email, DataRequired, EqualTo, URL
<<<<<<< HEAD
from jobplus.models import db, User, Company
=======
from .models import db, User, Company
from .decorators import create
>>>>>>> a1fa68e6590dca79d1e4aa85a6c5370657a8e1b6


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


<<<<<<< HEAD
class RegisterForm(FlaskForm):
    # username = StringField('用户名', validators=[DataRequired(), Length(1, 10)])
    email = StringField('邮箱', validators=[DataRequired(), Email(), Length(1, 254)])
    password = PasswordField('密码', validators=[DataRequired(), Length(6, 24)])
    repeat_password = PasswordField('重复密码', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('提交')

=======
class Register(FlaskForm):
>>>>>>> a1fa68e6590dca79d1e4aa85a6c5370657a8e1b6
    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('该邮箱已经被注册')

<<<<<<< HEAD
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
=======
    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('这个名字已经被注册了')

    def validate_phone_number(self, field):
        if User.query.filter_by(phone_number=field.data).first():
            raise ValidationError("手机号已存在")

    def validate_company(self, field):
        if not Company.query.filter_by(name=field.data).first():
            raise ValidationError('该公司不存在')

    @create(role=10)
    def create_user(self):
        return True

    @create(role=20)
    def create_boss(self):
        return True

    @create(role=30)
    def create_admin(self):
        return True


class RegisterForm(Register):
    username = StringField('姓名', validators=[DataRequired(), Length(1, 10)])
    email = StringField('邮箱', validators=[DataRequired(), Email(), Length(1, 254)])
    password = PasswordField('密码', validators=[DataRequired(), Length(6, 24)])
    repeat_password = PasswordField('重复密码', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('提交')


class UserForm(Register):
    phone_number = StringField('手机号', validators=[DataRequired()])
    work_year = IntegerField("工作经验", validators=[DataRequired()])
    work_resume = StringField('简历', validators=[DataRequired(), URL()])
    company = StringField('公司')
    submit = SubmitField('提交')

    def complete(self, id):
        user = User.query.filter_by(id=id).first()
        user.company = Company.query.filter_by(name=self.company.data).first()
        user.phone_number = self.phone_number.data
        user.work_resume = self.work_resume.data
        user.work_year = self.work_year.data
        db.session.add(user)
        db.session.commit()


class BossForm(FlaskForm):
    name = StringField('企业名称', validators=[DataRequired(), Length(3, 50)])
    address = StringField('公司地址', validators=[DataRequired()])
    net_site = StringField('网站链接', validators=[DataRequired(), URL()])
    logo = StringField("logo图片链接", validators=[DataRequired(), URL()])
    introduce = StringField("一句话简介", validators=[DataRequired()])
    detail = StringField("详细介绍")
    city = StringField("城市")
    financing = StringField("融资")
    company_field = StringField("领域")
    submit = SubmitField('提交')

    def complete(self, id):
        company = Company()
        self.populate_obj(company)
        user = User.query.filter_by(id=id).first()
        user.company = company
        db.session.add(company)
>>>>>>> a1fa68e6590dca79d1e4aa85a6c5370657a8e1b6
        db.session.add(user)
        db.session.commit()


<<<<<<< HEAD
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
=======
class AddUser(Register):
    username = StringField('姓名', validators=[DataRequired(), Length(1, 10)])
    email = StringField('邮箱', validators=[DataRequired(), Email(), Length(1, 254)])
    password = PasswordField('密码', validators=[DataRequired(), Length(6, 24)])
    phone_number = StringField('手机号', validators=[DataRequired()])
    submit = SubmitField('提交')

    def create_user(self):
        user = User()
        self.populate_obj(user)
>>>>>>> a1fa68e6590dca79d1e4aa85a6c5370657a8e1b6
        db.session.add(user)
        db.session.commit()


<<<<<<< HEAD
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
=======
class AddBoss(Register):
    username = StringField('公司名称', validators=[DataRequired(), Length(1, 10)])
    email = StringField('邮箱', validators=[DataRequired(), Email(), Length(1, 254)])
    password = PasswordField('密码', validators=[DataRequired(), Length(6, 24)])
    net_site = StringField('网站链接', validators=[DataRequired(), URL()])
    introduce = StringField("一句话简介", validators=[DataRequired()])
    submit = SubmitField('提交')

    def complate(self):
        company = Company()
        user = User.query.filter_by(email=self.email.data).first()
        self.populate_obj(company)
        company.name = user.username
        user.company = company
        db.session.add(company)
        db.session.add(user)
        db.session.commit()


class EditBoss(AddBoss):
    def validate_email(self, field):
        pass

    def validate_username(self, field):
        pass


class EditUser(AddUser):
    def update_user(self, id):
        user = User.query.get_or_404(id)
        self.populate_obj(user)
        db.session.add(user)
        db.session.commit()

    def validate_email(self, field):
        pass

    def validate_username(self, field):
        pass

    def validate_phone_number(self, field):
>>>>>>> a1fa68e6590dca79d1e4aa85a6c5370657a8e1b6
        pass
