# music-matcher
A music recommendation engine

## Development

Create a virtual environment

```pyenv install 3.10.6 && pyenv local 3.10.6 && python3 -m venv . --copies && source bin/activate```

Install requirements (and optional dev requirements)

```pip install -r requirements.txt```

```pip install -r requirements-dev.txt``` (Includes pylint, black, isort, pdbpp)

Set the following environment variables

```export LAST_API_KEY="YOUR_LAST_FM_API_KEY"```

```export LAST_API_SECRET="YOUR_LAST_FM_API_SECRET"```

```export LAST_USER="YOUR_LAST_FM_USERNAME"```

```export LAST_PASSWORD="YOUR_LAST_FM_PASSWORD"```