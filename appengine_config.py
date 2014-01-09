from gaesessions import SessionMiddleware

def webapp_add_wsgi_middleware(app):
 app = SessionMiddleware(app, cookie_key="q5ZKqpBL9StttsdzMBJYqRHA6MFsETtzheGPeMWfh53AJ3VPXtN2KgKvjmvJ9aSnKzQMPB6dUTUXTRB7jwCfjF4ZqZPGMNs6xfQ")
 return app