from app import db

class ServiceModel(db.Model):
    """
    DocString
    """
    __tablename__ = "service"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    client_nome = db.Column(db.String(255), nullable=False)
    service_nome = db.Column(db.String(255), nullable=False)
    pay_date = db.Column(db.Date, nullable=False)
    pay_type = db.Column(db.Date, nullable=False)
    hairdresser = db.Column(db.String(255), nullable=False)
    