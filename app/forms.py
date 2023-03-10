from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, PasswordField, EmailField, IntegerField, DateField
from wtforms.validators import DataRequired, Length, EqualTo, Email, InputRequired

class UserLoginForm(FlaskForm):
    phone = StringField('사용자이름', validators=[DataRequired("핸드폰 번호를 입력해주세요."), Length(min=11, max=11)])
    password = PasswordField('비밀번호', validators=[DataRequired("비밀 번호가 틀립니다.")])
    
class UserCreateForm(FlaskForm):
    phone = StringField('핸드폰 번호', validators=[DataRequired("핸드폰 번호를 입력해주세요. 010-1234-5678 -> 01012345678"), Length(min=11, max=11)])
    email = EmailField('이메일', validators=[DataRequired("이메일 주소를 입력해주세요."), Email()])
    username = StringField('실명', validators=[DataRequired("실명을 입력해주세요."), Length(min=3, max=25)])
    birth = StringField('생년월일 8자리', validators=[DataRequired("생년월일을 입력해주세요. 1995년 2월 25일 -> 19950225"), Length(min=8, max=8)])
    password1 = PasswordField('비밀번호', validators=[DataRequired("비밀번호가 일치하지 않습니다."), EqualTo('password2', '비밀번호가 일치하지 않습니다')])
    password2 = PasswordField('비밀번호확인', validators=[DataRequired("비밀번호가 일치하지 않습니다.")])
    
class BuyPointForm(FlaskForm):
    price = IntegerField('가격', validators=[DataRequired("구입할 포인트를 체크해 주세요.")])
    
    
class RequestPayForm(FlaskForm):
    userid = StringField('판매자 회원 아이디', validators=[DataRequired("판매자 회원 아이디")])
    shopname = StringField('상점명', validators=[DataRequired("상점명")])
    goodname = StringField('상품평', validators=[DataRequired("상품평")])
    price = IntegerField('가격', validators=[DataRequired("구입할 포인트를 체크해 주세요.")])
    recvphone = IntegerField("수신 휴대폰번호", validators=[DataRequired("수신 휴대폰번호")])
    memo = StringField("상품 정보 메세지", validators=[DataRequired("상품 정보 가격 입력")])
    reqaddr = IntegerField("주소 전송 여부", validators=[DataRequired("주소 정보 요청")])
    currency = StringField("통화 단위", validators=[DataRequired("통화를 선택해주세요")])
    
class ReserveCourtAreaDateForm(FlaskForm):
    area = StringField("지점명", validators=[DataRequired("지점을 선택해주세요.")])
    date = DateField("날짜", validators=[DataRequired("날짜를 선택해주세요.")])
    
class ReserveCourtForm(FlaskForm):
    phone = StringField('핸드폰 번호', validators=[DataRequired("핸드폰 번호를 입력해주세요. 010-1234-5678 -> 01012345678"), Length(min=11, max=11)])
    email = EmailField('이메일', validators=[DataRequired("이메일 주소를 입력해주세요."), Email()])
    username = StringField('실명', validators=[DataRequired("실명을 입력해주세요."), Length(min=3, max=25)])
    area = StringField("지점명", validators=[DataRequired("지점을 선택해주세요.")])
    date = DateField("날짜", validators=[DataRequired("날짜를 선택해주세요.")])
    court = StringField("코트", validators=[DataRequired("코트를 선택해주세요.")])
    time = StringField("이용 시간", validators=[DataRequired("이용 시간대를 선택해주세요.")])
    
class ReserveCourtCourtForm(FlaskForm):
    court = StringField("코트", validators=[DataRequired("코트를 선택해주세요.")])
    
class ReserveCourtTimeForm(FlaskForm):
    time = StringField("이용 시간", validators=[DataRequired("이용 시간대를 선택해주세요.")])

class DoorOpenForm(FlaskForm):
    area = StringField("Area")
    time = StringField("Time")

class VideoAgreementForm(FlaskForm):
    agree_4 = StringField('개인정보활용 동의')

class SendVideoForm(FlaskForm):
    area = StringField("Area")
    date = StringField("Date")
    time = StringField("Time")
    
    
class ChangePasswordForm(FlaskForm):
    before_password = PasswordField("이전 비밀번호", validators=[DataRequired("이전 비밀번호를 입력해주세요.")])
    new_password1 = PasswordField('새로 사용할 비밀번호', validators=[DataRequired("비밀번호가 일치하지 않습니다."), EqualTo('new_password2', '비밀번호가 일치하지 않습니다')])
    new_password2 = PasswordField('새로 사용할 비밀번호 확인', validators=[DataRequired("비밀번호가 일치하지 않습니다.")])
    
class AgreementForm(FlaskForm):
    agree_1 = StringField('볼랩 이용약관 (필수)', validators=[DataRequired("체크가 필요합니다")])
    agree_2 = StringField('개인정보 수집 및 이용 동의 (필수)', validators=[DataRequired("체크가 필요합니다.")])
    agree_3 = StringField('수집된 개인정보의 광고 및 홍보목적에 대한 동의(선택)')
    
class FindPassword(FlaskForm):
    phone = StringField('핸드폰 번호', validators=[DataRequired("핸드폰 번호를 입력해주세요. 010-1234-5678 -> 01012345678"), Length(min=11, max=11)])
    email = EmailField('이메일', validators=[DataRequired("이메일 주소를 입력해주세요."), Email()])
    
class FilterReservationForm(FlaskForm):
    username = StringField('실명')
    phone = StringField('핸드폰 번호')
    date = DateField("날짜")

class UserFilterForm(FlaskForm):
    username = StringField('실명')
    phone = StringField('핸드폰번호')
    
class ChangeUserInfoForm(FlaskForm):
    username = StringField('실명', validators=[DataRequired("실명을 입력해주세요."), Length(min=1, max=25)])
    phone = StringField('핸드폰 번호', validators=[DataRequired("핸드폰 번호를 입력해주세요. 010-1234-5678 -> 01012345678"), Length(min=11, max=11)])
    birth = StringField('생년월일 8자리', validators=[DataRequired("생년월일을 입력해주세요. 1995년 2월 25일 -> 19950225"), Length(min=8, max=8)])
    point = IntegerField("Point", validators=[InputRequired("포인트를 입력해주세요.")])
    admin_point = IntegerField("Point", validators=[InputRequired("관리자 지급 포인트를 입력해주세요.")])
    
class PointManagementForm(FlaskForm):
    price = IntegerField("Price", validators=[DataRequired("가격")])
    point = IntegerField("Point", validators=[DataRequired("포인트")])
    
class CourtManagementForm(FlaskForm):
    area = StringField("Area")
    price = IntegerField("Point", validators=[DataRequired("포인트")])
    
class CourtOnOffForm(FlaskForm):
    status = StringField("Status")