
# Wrangler (0.0.7)

Wrangler is an application that parses `yaml` files into `lua` scripts in the Global Work Flow.

# Installation

To install from pypi:
`pip install gwf-wrangler`

To install from the repository:
`pip install .`

# Usage
Wranglers only requirement are an output directory and a variable number of inputs.  These inputs
can be either a single yaml, a directory of yaml files, or a combination of the two.

## Example Usage
`wrangler --output-path "./temp" file1.yaml directory1 directory2/file2.yaml`


1. Part of NOAA EMC Org
