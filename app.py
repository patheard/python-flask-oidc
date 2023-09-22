"""
Flask OIDC client example using Authlib with `private_key_jwt` authentication:
https://openid.net/specs/openid-connect-core-1_0.html#ClientAuthentication
"""
from flask import Flask, url_for, session
from flask import render_template, redirect
from authlib.common.security import generate_token
from authlib.integrations.flask_client import OAuth
from authlib.oauth2.rfc7523 import PrivateKeyJWT


app = Flask(__name__)
app.secret_key = "!secret"
app.config.from_object("config")

oauth = OAuth(app)
oauth.register(
    name="logingov",
    server_metadata_url=app.config["IDP_CONF_URL"],
    token_endpoint_auth_method=PrivateKeyJWT(),
    client_kwargs={
        "scope": "openid email",
    },
)


@app.route("/")
def homepage():
    """Render the homepage"""
    user = session.get("user")
    return render_template("home.html", user=user)


@app.route("/login")
def login():
    """Start the login flow"""
    redirect_uri = url_for("auth", _external=True)
    return oauth.logingov.authorize_redirect(
        redirect_uri,
        acr_values=app.config["IDP_ACR_VALUES"],
        nonce=generate_token(22),
    )


@app.route("/auth")
def auth():
    """Complete the login flow"""
    token = oauth.logingov.authorize_access_token()
    session["user"] = token["userinfo"]
    return redirect("/")


@app.route("/logout")
def logout():
    """Log the user out"""
    session.pop("user", None)
    return redirect("/")
