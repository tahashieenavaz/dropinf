import pandas
import numpy
import typing

DataFrameSeries = pandas.DataFrame | pandas.Series


def dropinf(dataframe: DataFrameSeries) -> DataFrameSeries:
    return dataframe.replace([numpy.inf, -numpy.inf], numpy.nan).dropna()
