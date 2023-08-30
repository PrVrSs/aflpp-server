from sqlalchemy import MetaData
from sqlalchemy.orm import DeclarativeBase


convention = {
    'all_column_names': lambda constraint, table: '_'.join([
        column.name
        for column in constraint.columns.values()
    ]),
    'ix': 'ix__%(table_name)s__%(all_column_names)s',
    'uq': 'uq__%(table_name)s__%(all_column_names)s',
    'ck': 'ck__%(table_name)s__%(constraint_name)s',
    'fk': 'fk__%(table_name)s__%(all_column_names)s__%(referred_table_name)s',
    'pk': 'pk__%(table_name)s',
}

metadata_obj = MetaData(naming_convention=convention)


def _columns(data):
    return ', '.join([
        f'{k}={repr(v)}'
        for k, v in data.items()
        if not k.startswith('_')
    ])


class Base(DeclarativeBase):
    __abstract__ = True

    metadata = metadata_obj

    def __repr__(self) -> str:
        return f'<{self.__class__.__name__}({_columns(self.__dict__)})>'
