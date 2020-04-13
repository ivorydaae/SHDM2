# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

# Read recipe inputs
fico_join = dataiku.Dataset("fico_join")
fico_join_df = fico_join.get_dataframe()


# Compute recipe outputs
# TODO: Write here your actual code that computes the outputs
# NB: DSS supports several kinds of APIs for reading and writing data. Please see doc.

fico_historic_df = fico_join_df[fico_join_df['Default'].notnull() == True]
fico_to_predict_df = fico_join_df[fico_join_df['Default'].isnull() == True]

# Write recipe outputs
fico_historic = dataiku.Dataset("fico_historic")
fico_historic.write_with_schema(fico_historic_df)
fico_to_predict = dataiku.Dataset("fico_to_predict")
fico_to_predict.write_with_schema(fico_to_predict_df)

