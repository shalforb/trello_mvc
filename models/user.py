from init import db, ma

class User(db.Model):
    __tablename__ = "users"

    id=db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)

class UserSchema(ma.Schema):
    class Meta:
        fields = ("id", "name", "email", "password", "is_admin")

user_schema = UserSchema(exclude=["password"])