"""
This module provides SAS code templates for generating analysis outputs.

Each template is a string that can be formatted with study-specific
parameters like dataset name and treatment variable. The templates cover
a variety of common clinical trial analyses.
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

VS_CHANGE_TABLE_TEMPLATE = """
* Title: Vital Signs Change from Baseline;
* Dataset: {dataset};
* Treatment Variable: {treatment_var};

ods rtf file="vs_change.rtf";

proc means data={dataset} n mean stddev min max;
    class {treatment_var} AVISIT;
    var CHG;
    by PARAMCD;
    title "Vital Signs Change from Baseline by Visit";
run;

ods rtf close;
"""

LAB_SHIFT_TABLE_TEMPLATE = """
* Title: Lab Shift Table;
* Dataset: {dataset};
* Treatment Variable: {treatment_var};

ods rtf file="lab_shift.rtf";

proc freq data={dataset};
    tables BNTOXGR*WNTOXGR / nocol nopercent;
    by {treatment_var} PARAMCD;
    title "Laboratory Shift Table from Baseline to Worst Post-Baseline Grade";
run;

ods rtf close;
"""

TEAE_BY_SOC_PT_TABLE_TEMPLATE = """
* Title: TEAE by SOC and PT;
* Dataset: {dataset};
* Treatment Variable: {treatment_var};

ods rtf file="teae_by_soc_pt.rtf";

proc freq data={dataset} order=freq;
    where TEAEFL = 'Y';
    tables AEBODSYS*AEDECOD*{treatment_var} / nocol nopercent;
    title "TEAE by System Organ Class and Preferred Term";
run;

ods rtf close;
"""

TEAE_SUMMARY_TABLE_TEMPLATE = """
* Title: TEAE Summary;
* Dataset: {dataset};
* Treatment Variable: {treatment_var};

ods rtf file="teae_summary.rtf";

proc freq data={dataset};
    where TEAEFL = 'Y';
    tables {treatment_var} / nocol nopercent;
    title "Number of Subjects with at Least One TEAE";
run;

proc freq data={dataset};
    where SAEFL = 'Y';
    tables {treatment_var} / nocol nopercent;
    title "Number of Subjects with at Least One Serious TEAE";
run;

proc freq data={dataset};
    where AERELFL = 'Y';
    tables {treatment_var} / nocol nopercent;
    title "Number of Subjects with at Least One Related TEAE";
run;

proc freq data={dataset};
    where AESEV = 'SEVERE';
    tables {treatment_var} / nocol nopercent;
    title "Number of Subjects with at Least One Severe TEAE";
run;

proc freq data={dataset};
    where AEOUT = 'FATAL';
    tables {treatment_var} / nocol nopercent;
    title "Number of Subjects with TEAE Leading to Death";
run;

ods rtf close;
"""

EXPOSURE_TABLE_TEMPLATE = """
* Title: Exposure Summary;
* Dataset: {dataset};
* Treatment Variable: {treatment_var};

ods rtf file="exposure.rtf";

proc means data={dataset} n mean stddev min max;
    class {treatment_var};
    var CUMDOSE TRTDUR RELDOS;
    title "Exposure Summary by Treatment Arm";
run;

ods rtf close;
"""

DISPOSITION_TABLE_TEMPLATE = """
* Title: Subject Disposition;
* Dataset: {dataset};
* Treatment Variable: {treatment_var};

ods rtf file="disposition.rtf";

proc freq data={dataset};
    tables {treatment_var}*dcreason / nocol nopercent;
    title "Subject Disposition: Discontinuation Reasons by Treatment Arm";
run;

proc freq data={dataset};
    tables {treatment_var} / nocol nopercent;
    title "Subject Disposition: Total Subjects by Treatment Arm";
run;

ods rtf close;
"""
