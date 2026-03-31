# Source Code Attribution Pipeline

This directory contains the source code for the authorship attribution and evasion pipeline, adapted from [code-imitator](https://github.com/EQuiw/code-imitator) by Erwin Quiring et al.

## Structure

| Directory | Description |
|-----------|-------------|
| [**LibToolingAST/**](LibToolingAST/) | Clang-based AST feature extraction and code transformers |
| [**CodeStyloJava/**](CodeStyloJava/) | Java-based lexical and layout feature extraction (optional) |
| [**PyProject/**](PyProject/) | Python project for classification, evaluation, and evasion |
| [**ExternalTransformers/**](ExternalTransformers/) | Optional external tools (e.g., Include-What-You-Use) |

## Setup

### 1. Environment Variables (Optional)

Add the following to your `.profile` or `.bashrc`:

```bash
export AUTHORSHIP_EVASION="PATH/TO/REPO/authorship-evasion/"
```

### 2. Build Sub-Projects

Each sub-project has its own README with detailed build instructions:

1. **LibToolingAST** (required) -- Compile the feature extractors and code transformers.
   See [LibToolingAST/README.md](LibToolingAST/README.md).

2. **CodeStyloJava** (optional) -- Java-based features for lexical and layout analysis.
   See [CodeStyloJava/README.md](CodeStyloJava/README.md).
   > Pre-extracted features for the full dataset are already included. Only needed if extracting features for new files.

3. **PyProject** -- Python-based classification and evaluation.
   See [PyProject/README.md](PyProject/README.md) (if available).

4. **ExternalTransformers** (optional) -- Stand-alone tools for code rewriting.
   See [ExternalTransformers/README.md](ExternalTransformers/README.md).
