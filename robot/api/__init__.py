from flask_restplus import Api as _Api

api = _Api(version="0.1", title="API Robot Gmail",
           description="Esta API executa um Robot que loga em uma conta gmail e dispara um e-mail.")
