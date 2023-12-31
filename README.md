# Python Flask OIDC :key: :unlock:
A [Flask app](https://github.com/pallets/flask/) using [Authlib](https://github.com/lepture/authlib) and [OpenID Connect `private_key_jwt` client authentication](https://openid.net/specs/openid-connect-core-1_0.html#ClientAuthentication).

# Setup
1. Generate a key pair for the client and register the client's public key with your identity provider.
```sh
make keys
```

2. Copy `.env.example` to `.env` and provide the required values.

3. Install the dependencies and start the app:
```sh
make install
make run
```

# Credit
This app was based on the [Authlib `flask-google-login` example](https://github.com/authlib/demo-oauth-client/tree/master/flask-google-login).