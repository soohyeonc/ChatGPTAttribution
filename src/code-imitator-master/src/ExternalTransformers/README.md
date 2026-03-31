# External Transformers

Optional stand-alone tools for code rewriting during evasion attacks. If environment variables are not set, the respective transformers are automatically skipped.

## Include-What-You-Use (IWYU)

We use [IWYU](https://github.com/include-what-you-use/include-what-you-use) to detect unused headers and suggest missing includes.

### Setup

```bash
git clone https://github.com/include-what-you-use/include-what-you-use.git
cd include-what-you-use
git checkout clang_5.0
mkdir build && cd build
cmake -G "Unix Makefiles" -DIWYU_LLVM_ROOT_PATH=<path-to>/clang+llvm-5.0.0-linux-x86_64-ubuntu16.04 ..
make
```

**Requirements:**
- Checkout the branch matching Clang 5.0
- Create the `build/` directory inside the cloned repository
- Python 2 must be installed (needed by `src/ExternalTransformers/iwyu_replace.sh`)

After building, add the full path of `include-what-you-use/build/` to `config.ini` in PyProject.

### Troubleshooting

If you encounter build issues, install:
```bash
sudo apt-get install libncurses5-dev
```

## Adding Custom Transformers

1. Add an entry to the CSV file in this directory
2. Create a Python class that inherits from `TransformerBase`
3. Register it in `__load_external_transformers` in `TransformerHandler`
4. Add the executable path to `config.ini` and `Configuration.py`
