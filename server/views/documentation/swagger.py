template = {
    "swagger": "2.0.0",
    "info": {
        "title": "SideNotes Restful APIs",
        "description": "This is the initial version of the Sidenotes Restful APIs, "
                  "For all note and tasks implementation.",
        "contact": {
            "responsibleOrganization": "Kalundaah",
            "responsibleDeveloper": "Neville' Mwangangi",
            "email": "kalundaah@github.com",
            "url": "github.com/kalundaah",
        },
        "termsOfService": "",
        "version": "1.0.0"
    },
    #"basePath": "/api/v1/views",  # base bash for blueprint registration
    "schemes": [
        "http",
        "https"
    ],
    "securityDefinitions": {
        "CookieAuth": {
            "type": "apiKey",
            "name": "session_id",
            "in": "cookie",
            "description": "Session ID cookie for authentication"
        }
    },
}

swagger_config = {
    "headers": [
    ],
    "specs": [
        {
            "endpoint": 'apispec',
            "route": '/apispec.json',
            "rule_filter": lambda rule: True,  # all in
            "model_filter": lambda tag: True,  # all in
        }
    ],
    "static_url_path": "/flasgger_static",
    "swagger_ui": True,
    "specs_route": "/"
}
