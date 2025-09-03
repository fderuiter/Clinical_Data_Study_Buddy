"""
This module provides R code templates for generating analysis outputs.

Each template is a string that can be formatted with study-specific
parameters like dataset name and treatment variable.
"""

DEMO_TABLE_TEMPLATE = """
# Title: Demographics Table
# Dataset: {dataset}
# Treatment Variable: {treatment_var}

library(tidyverse)
library(rtables)

# Assuming '{dataset}.csv' is in the working directory
data <- read.csv("{dataset}.csv")

# Demographics: Sex by Treatment Arm
sex_table <- data %>%
  group_by({treatment_var}, SEX) %>%
  summarise(n = n(), .groups = 'drop') %>%
  pivot_wider(names_from = {treatment_var}, values_from = n, values_fill = 0)

print("Demographics: Sex by Treatment Arm")
print(sex_table)

# Demographics: Age Summary by Treatment Arm
age_summary <- data %>%
  group_by({treatment_var}) %>%
  summarise(
    n = n(),
    mean = mean(AGE, na.rm = TRUE),
    sd = sd(AGE, na.rm = TRUE),
    min = min(AGE, na.rm = TRUE),
    max = max(AGE, na.rm = TRUE)
  )

print("Demographics: Age Summary by Treatment Arm")
print(age_summary)

# Note: RTF output in R requires additional packages and setup.
# This example prints to the console. For a production-ready RTF,
# you would typically use a package like 'rtables' or 'reporter'
# and write the table objects to an RTF file.
"""
