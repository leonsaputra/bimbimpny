from sample_config import Config


class Development(Config):
    # get this values from the my.telegram.org
    APP_ID = 10545971
    API_HASH = "523293b62d5810a3b448314351e3f470"
    # the name to display in your alive message
    ALIVE_NAME = "Albert Zhang"
    # create any PostgreSQL database (i recommend to use elephantsql) and paste that link here
    DB_URI = "postgres://edhuvnjn:4-TwNAEQXN0x7zK-17TVTGxptoU06xx_@ziggy.db.elephantsql.com/edhuvnjn"
    # After cloning the repo and installing requirements do python3 stringsetup.py an fill that value with this
    STRING_SESSION = "1BVtsOMgBux-hf0PgeDQsMj8Wu43vIPeNYfEuT5K6hABbUuiZqR3UmUnJfnk92Pk4ANzck3nDh6R6zzCUZOmdf7fayxW5rfpL7vhD7M6zN_hsbkC2D6xGLhiRE-s47zTQS67DHndiOgQKWD_j19RNeM1VNrItFrAkGCUzNetH-A6lvWaRdCW8KPWy7jTCP4zyWGF-EyJGNZreCo3fKX0GwoYcxh-vVqpcUa_q1fhUXtKdw6UQdFwXa3thl4DHuZrboSzAIEvy8wXGIKcokyPuOr7Ba7BaBzFD1h_t39NftI3Y7ppfDe0MbxrlBQwifu0xtF2xTIzXLIGi-EK81Dbj7naF5iP_uiE="
    # create a new bot in @botfather and fill the following vales with bottoken
    TG_BOT_TOKEN = "5406935497:AAFmNlmQjrzt-4UHNHizPerwJjUKeSHYUJM"
    # create a private group and a rose bot to it and type /id and paste that id here (replace that -100 with that group id)
    PRIVATE_GROUP_BOT_API_ID = -1001757563842
    # command handler
    COMMAND_HAND_LER = "?"
    # command hanler for sudo
    SUDO_COMMAND_HAND_LER = "!"
    # External plugins repo
    EXTERNAL_REPO = "https://github.com/TgCatUB/CatPlugins"
    # if you need badcat plugins set "True"
    BADCAT = "True"
