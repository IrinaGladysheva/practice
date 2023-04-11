from app.app import create_app
from app.extensions.database import migrate

app = create_app()

if __name__ == '__main__':
    app.run()

