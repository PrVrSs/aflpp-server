import dynaconf


settings = dynaconf.Dynaconf(
    envvar_prefix='AFLPP_SERVER',
    environments=True,
    load_dotenv=True,
)
