"""
SAS code templates for analysis generation.
"""

DEMO_TABLE_TEMPLATE = """
* Title: Demographics Table;
* Dataset: {dataset};
* Treatment Variable: {treatment_var};

ods rtf file="demographics.rtf";

proc freq data={dataset};
    tables {treatment_var}*sex / nocol nopercent;
    title "Demographics: Sex by Treatment Arm";
run;

proc means data={dataset} n mean stddev min max;
    class {treatment_var};
    var age;
    title "Demographics: Age Summary by Treatment Arm";
run;

ods rtf close;
"""
