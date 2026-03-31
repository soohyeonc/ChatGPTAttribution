# LibToolingAST

Clang-based AST feature extraction and code transformations using LLVM/Clang LibTooling.

## Prerequisites

- **LLVM/Clang 5.0.0** -- Download pre-compiled packages from [LLVM Releases](http://releases.llvm.org/download.html) (e.g., `Clang for x86_64 Ubuntu 16.04`)
- **CMake** >= 3.9
- **GNU Parallel** >= 20161122
- **Boost** (header files only, no build required) -- Download [Boost 1.65.1](https://www.boost.org/users/history/)

### Optional System Packages

```bash
sudo apt-get install libstdc++-5-dev libtinfo-dev lib32z1-dev build-essential
# Ubuntu 20+:
sudo apt-get install libncurses5
# If needed:
sudo apt-get install libgmp-dev
```

> **Important:** Use Clang 5.0.0 exactly (not 5.0.1) to avoid path compatibility issues.

## Compilation

### Option A: Command Line

```bash
cd LibToolingAST
mkdir cmake-build-release && cd cmake-build-release
cmake .. \
  -DMY_CLANG_ROOT_DIR=<path-to>/clang+llvm-5.0.0-linux-x86_64-ubuntu16.04 \
  -DMY_BOOST_ROOT_DIR=<path-to>/boost_1_65_1
make
```

### Option B: IDE (CLion)

1. Open the `LibToolingAST` directory as a project
2. Set CMake options:
   - `-DMY_CLANG_ROOT_DIR=/path/to/clang+llvm-5.0.0-linux-x86_64-ubuntu16.04`
   - `-DMY_BOOST_ROOT_DIR=/path/to/boost_1_65_1`
3. Compile in **Release** mode (Debug mode enables debug logging)

## Project Structure

| Directory | Description |
|-----------|-------------|
| `feature_extraction/` | Lexical feature extractor |
| `feature_extraction_single/` | AST feature extractor |
| `codeinfo/` | Tools for listing source file information (variable names, typedefs, etc.) |
| `transformers/` | Code transformation tools for evasion attacks |
| `tests/` | Unit tests (Catch framework) |
| `Utilities/` | Shared utility functions |

### Key Files

- **`ourerrors.h`** -- Common includes required for compilation (extends `microsoft_errors.h` with a bool type fix)
- **`config_transformeroptions.csv`** -- Configuration of all code transformations, including parameters needed for Python integration

## Feature Extraction

Each feature set has two files: one with the logic and one with the `main` entry point. This separation allows the test suite to reuse the feature logic independently.

All feature extraction tools are invoked via `extractfeatures_single.sh`. See the [PyProject documentation](../PyProject/README_ATTRIBUTION.md) for details.

## Code Transformers

### Quick Start

Start with `compoundstmt_transf.cpp` -- it is the simplest transformer and illustrates the general pattern.

### Calling a Transformer

```
<file> <transformer-options> -- <compiler-options>
```

Example:
```bash
./if_transformer sometest.cpp -strategy=1 -seed=31 -- \
  -I<path-to>/clang+llvm-5.0.0/lib/clang/5.0.0/include \
  -include <path-to>/LibToolingAST/ourerrors.h
```

> **Important:** Run `clang-format` before and after calling a code transformer. Some transformations assume properly formatted input.

### Status Codes

| Code | Meaning |
|------|---------|
| 124 | No applicable code location found |
| 123 | Failed to rewrite an available code location |

### Limitations

- Only single-file programs are supported (sufficient for Google Code Jam, but multi-file projects require adaptation)
- Transformer names may not map 1:1 to the paper (grouping was changed for clarity without refactoring all files)
