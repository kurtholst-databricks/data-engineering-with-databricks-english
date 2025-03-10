# Databricks notebook source
# MAGIC %md
# MAGIC # MLOps end to end

# COMMAND ----------

# MAGIC %pip install dbdemos

# COMMAND ----------

# Restarting with dbutils:
dbutils.library.restartPython() 

# COMMAND ----------

# MAGIC %md
# MAGIC # Data Engineering

# COMMAND ----------

import dbdemos
dbdemos.install('pandas-on-spark')

# COMMAND ----------

# MAGIC %md
# MAGIC # Machine Learning

# COMMAND ----------

# Included in the demoes is also mlops
import dbdemos
dbdemos.install('mlops-end2end')
