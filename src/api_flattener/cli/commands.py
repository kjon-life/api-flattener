# src/api_flattener/cli/commands.py
from pathlib import Path
import click
import yaml
from ..core.flattener import APIFlattener

@click.group()
def cli():
    """CLI tool for flattening OpenAPI specifications."""
    pass

@cli.command()
@click.argument('input_spec', type=click.Path(exists=True))
@click.argument('output_spec', type=click.Path())
@click.option('--base-path', type=click.Path(exists=True), help='Base path for resolving references')
def flatten(input_spec: str, output_spec: str, base_path: str = None):
    """Flatten an OpenAPI specification by resolving all references.
    
    Arguments:
        input_spec: Path to the input OpenAPI specification
        output_spec: Path where the flattened specification will be saved
        base_path: Optional base path for resolving references
    """
    try:
        flattener = APIFlattener(base_path)
        flattened_spec = flattener.flatten_spec(input_spec)
        
        # Ensure parent directory exists
        output_path = Path(output_spec)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        
        # Write the flattened spec
        with open(output_path, 'w') as f:
            yaml.dump(flattened_spec, f, sort_keys=False)
            
        click.echo(f"Successfully flattened specification: {output_spec}")
        
    except Exception as e:
        click.echo(f"Error: {str(e)}", err=True)
        raise click.Abort()

if __name__ == '__main__':
    cli()