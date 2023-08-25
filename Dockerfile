FROM aflplusplus/aflplusplus as compile-image

RUN apt-get update && apt-get full-upgrade -y && \
    apt-get -y install --no-install-suggests --no-install-recommends \
    libssl-dev liblzma-dev libsqlite3-dev libffi-dev libreadline-dev libbz2-dev zlib1g-dev

ENV PYTHONFAULTHANDLER=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONHASHSEED=random \
    PYTHONDONTWRITEBYTECODE=1 \
    # pip:
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    # poetry:
    POETRY_VERSION=1.1.13 \
    POETRY_HOME="/opt/poetry" \
    POETRY_NO_INTERACTION=1 \
    POETRY_CACHE_DIR='/var/cache/pypoetry' \
    PATH="$PATH:/root/.local/bin" \
    PYENV_ROOT=/pyenv

# prepend poetry and venv to path
ENV PATH="$POETRY_HOME/bin:$VENV_PATH/bin:$PATH"

RUN git clone https://github.com/pyenv/pyenv.git /pyenv
RUN /pyenv/bin/pyenv install 3.11.4
RUN eval "$(/pyenv/bin/pyenv init -)" && /pyenv/bin/pyenv local 3.11.4

ENV PATH /pyenv/versions/3.11.4/bin:${PATH}

RUN python3.11 -m pip install poetry setuptools wheel six

WORKDIR /code

COPY ./poetry.lock ./pyproject.toml /code/
COPY ./aflpp_server /code/aflpp_server

# install dependencies
RUN python3.11 -m poetry config virtualenvs.in-project true --local
RUN python3.11 -m poetry install --no-dev --no-root --no-interaction --no-ansi

EXPOSE 50051

CMD ["python3.11", "-m", "poetry",  "run", "python", "-m", "aflpp_server"]
