class GlobalVariables:
    
    APP_LOGS_PATH = "logs"
    APP_CONFIG_PATh = "portfolio/configs"

    LOGGER = None

    PROJECTS = [
        {
            "name": "Habit tracking app with Python and MongoDB",
            "thumb": "img/habit-tracking-hero.png",
            "hero": "img/habit-tracking-hero_original.png",
            "categories": ["python", "web"],
            "slug": "habit-tracking",
            "prod": "https://flask-habit-tracker-app.herokuapp.com/habit-tracker",
            "github": "https://github.com/rushikeshshelke/Habit-Tracker"
        },
        {
            "name": "Mircoblog app with Python and MongoDB",
            "thumb": "img/microblog.png",
            "hero": "img/microblog_original_800x300.png",
            "categories": ["python", "web"],
            "slug": "microblog",
            "prod": "https://restful-microblog-app.herokuapp.com/microblog",
            "github": "https://github.com/rushikeshshelke/Microblog"
        },
        {
            "name": "Store API with Python, Flask-RestFul and Swagger",
            "thumb": "img/store.png",
            "hero": "img/store_original_800x300.png",
            "categories": ["python", "rest-api", "swagger"],
            "slug": "store-api",
            "prod": "https://store-item-rest-api-v1.herokuapp.com/api/docs/",
            "github": "https://github.com/rushikeshshelke/Store-API"
        },
        {
            "name": "URL shortner with Python, Flask and MongoDB",
            "thumb": "img/url_shortner.png",
            "hero": "img/url_shortner_original_800x300.png",
            "categories": ["python", "web"],
            "slug": "url-shortner",
            "prod": "https://flask-short-url-app.herokuapp.com/",
            "github": "https://github.com/rushikeshshelke/URLShortner"
        }
    ]

    SLUG_IN_PROJECT = {project['slug']: project for project in PROJECTS}