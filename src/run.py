# Este script inicializa todo o processo da aplicacao
# flask

from app import app, db

if __name__ == "__main__":
    # Tranzendo o contexto para a aplicacao
    app.app_context().push()
    # criando o database
    db.create_all()
    app.run()