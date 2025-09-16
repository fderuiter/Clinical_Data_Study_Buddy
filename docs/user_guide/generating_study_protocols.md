# Generating Study Protocols

This project can also generate study protocol documents. This feature is useful for creating a quick draft of a protocol based on a few key parameters.

## Quickstart

To generate a study protocol, use the `generate study-protocols` command:

```bash
poetry run cdsb generate study-protocols \
    --therapeutic-area "Oncology" \
    --treatment-arm "Drug A + Placebo" \
    --treatment-arm "Drug B + Placebo" \
    --duration-weeks 52 \
    --phase 3 \
    --output-dir "my_protocol"
```

This will generate a `protocol.md` file and a `gantt_chart.png` file in the `my_protocol` directory.
