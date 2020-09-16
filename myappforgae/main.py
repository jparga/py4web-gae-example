import os
import site

site.addsitedir(os.path.join(os.path.dirname(__file__), "lib"))

from py4web.core import Reloader, bottle  # Esto tiene que ir aquí, después de marcar el path de lib

os.environ["PY4WEB_DASHBOARD_MODE"] = "demo"
os.environ["PY4WEB_SERVICE_DB_URI"] = "sqlite:memory"  # "google:datastore"  #
os.environ["PY4WEB_APPS_FOLDER"] = os.path.join(os.path.dirname(__file__), "apps")
os.environ["PY4WEB_SERVICE_FOLDER"] = os.path.join(
    os.path.dirname(__file__), "apps/.service"
)
Reloader.import_apps()
app = bottle.default_app()


#  Esta parte solo se activa cuando queremos probarlo localmente con main.py
if os.getenv("GAE_ENV", "").startswith("standard"):
    # Production in the standard environment muestra
    message = "do whatever"
else:
    # Local execution.
    if __name__ == "__main__":
        # This is used when running locally only. When deploying to Google App
        # Engine, a webserver process such as Gunicorn will serve the app. This
        # can be configured by adding an `entrypoint` to app.yaml.
        # App Engine itself will serve those files as configured in app.yaml.

        app.run(host="127.0.0.1", port=9000, debug=True)

