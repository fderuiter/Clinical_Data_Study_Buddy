import click
import sys
import os

# Add src to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from analysisgen.generator import AnalysisGenerator

@click.command()
@click.option('--language', type=click.Choice(['sas', 'r'], case_sensitive=False), required=True, help='Language for the generated code.')
@click.option('--dataset', required=True, help='Source dataset (e.g., ADSL).')
@click.option('--output-type', required=True, help='Type of analysis output (e.g., Demographics).')
@click.option('--treatment-var', required=True, help='Treatment variable (e.g., TRT01A).')
@click.option('--output-file', required=True, help='Path to the output file.')
def generate(language, dataset, output_type, treatment_var, output_file):
    """
    Generates analysis code in SAS or R.
    """
    generator = AnalysisGenerator(language, dataset, output_type, treatment_var)
    code = generator.generate_code()

    try:
        with open(output_file, 'w') as f:
            f.write(code)
        click.echo(f"Successfully generated {language.upper()} code in {output_file}")
    except IOError as e:
        click.echo(f"Error writing to file: {e}", err=True)

if __name__ == '__main__':
    generate()
