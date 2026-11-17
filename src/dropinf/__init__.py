import pandas
import numpy
import typing

DataFrameSeries: typing.TypeAlias = pandas.DataFrame | pandas.Series


def dropinf(
    dataframe: DataFrameSeries, *, infinity: float = numpy.inf, nan: float = numpy.nan
) -> DataFrameSeries:
    return dataframe.replace([infinity, -infinity], nan).dropna()
