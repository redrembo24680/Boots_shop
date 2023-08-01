from website import app
from website import routes, sort_routes
from db import Users, session, Country

if __name__ == "__main__":
    app.run(debug=True)

