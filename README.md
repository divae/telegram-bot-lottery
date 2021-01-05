# Telegram Bot Lottery

Prueba de concepto de un bot de Telegram accionado por WebHooks conectado a la API de El País para consultar los números premiados de la lotería.

> El proyecto está en construcción.

Éste proyecto está inspirado para su construcción en el trabajo de [Rafael Nogales](https://github.com/RNogales94) "[Telegram bot webhook](https://github.com/RNogales94/Telegram-Bot-Heroku-Webhook-For-Medium-)"

## Recursos
- Artículo base para la configuración, construcción y despliegue del bot: [Telegram Bot Webhook + Heroku](https://planetachatbot.com/telegram-bot-webhook-heroku-fa53c5d72081)
- Listado de premios: [API lotería de navidad](https://servicios.elpais.com/sorteos/loteria-navidad/api/)
- Conexión con Telegram: [Api Telegram Bots](https://core.telegram.org/bots)

## Tecnologías
- Servidor web: [Heroku](https://dashboard.heroku.com/)
- Lenguaje: [Python](https://www.python.org/)
- Framework: [Flask](https://flask.palletsprojects.com/en/1.1.x/)
- Entorno virtual: [Pipenv](https://pipenv-es.readthedocs.io/es/latest/)
- Librería Test: [Pytest](https://docs.pytest.org/en/stable/)

# Chatbot
- Nombre del bot en telegram: @resultados_loteria_bot
- Api para el bot: https://resultadosloteriabot.herokuapp.com/
    - Path GET "/" : Saludo : Hello, World!
    - Path POST "/" : Listado : Listado sin depurar de la lotería de navidad 2020.

## Funcionamiento
El código está preparado para que cuando se introduzca cualquier texto en el canal, 
el bot responda devolviendo la **lista sin formatear** de los números premiados de navidad,

En versiones posteriores se trabajará en mejorar la visualización de esos datos.
además de permitir poder consultar el sorteor del niño y poder consultar número a número.

## Arrancar el proyecto en local
Configurar la variable FLASK_APP en la maquina
```cmd=
export FLASK_APP = run.py
```

Instalar las dependencias del proyecto
```cmd=
pip install -r requirements.txt
```

Levantar el servidor
```cmd=
$ flask run

 * Serving Flask app "run.py" (lazy loading)
 * Environment: development
 * Debug mode: on
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 127-881-450
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
127.0.0.1 - - [05/Jan/2021 17:44:01] "?[37mGET / HTTP/1.1?[0m" 200 -
127.0.0.1 - - [05/Jan/2021 17:44:01] "?[33mGET /favicon.ico HTTP/1.1?[0m" 404 -

```

Lanzar los test

```cmd=
$ pytest

.....s.                                                                                                                                                                          [100%]
=============================================================================== short test summary info ===============================================================================
SKIPPED [1] project\tests\test_service.py:39: TypeError: 'MockResponse' object is not callable
6 passed, 1 skipped in 0.33s
```