# Markdown generators

The scripts in this directory convert TSV files into individual markdown files for
the academicpages template.

```bash
python markdown_generator/publications.py
python markdown_generator/talks.py
```

Both scripts can also be pointed at custom inputs and output directories:

```bash
python markdown_generator/publications.py --input path/to/publications.tsv --output-dir _publications
python markdown_generator/talks.py --input path/to/talks.tsv --output-dir _talks
```

The notebooks are retained as interactive documentation, but the Python scripts
are the maintainable entry points for command-line use.
