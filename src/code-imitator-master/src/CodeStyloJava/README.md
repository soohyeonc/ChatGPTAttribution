# CodeStyloJava

Java-based lexical and layout feature extraction, adapted from [CodeStylometry](https://github.com/calaylin/CodeStylometry) by Aylin Caliskan.

## Prerequisites

- Java 8 or higher (OpenJDK is supported)

## About

This module extracts lexical and layout features from source code using regex-based analysis. Only the **Naive Baseline** directory is required.

**Modifications from the original:**
- Excluded features that are more reliably extracted via Clang (e.g., branching factor)
- Fixed encoding issues
- Adapted the driver class to accept command-line arguments (author directory path or individual source file)

## Getting Started

1. **Import as a Java project** (e.g., in IntelliJ IDEA).

2. **Set up libraries** -- Ensure the libraries under `SCAA/` are imported. If you encounter issues, download the full SCAA directory from the [original repository](https://github.com/calaylin/CodeStylometry).

3. **Compile** with `Driver.java` as the main class.

4. **Create a JAR file** (e.g., via IntelliJ: Build > Build Artifacts).
   The JAR will typically be located at:
   ```
   CodeStyloJava/out/artifacts/CodeStyloJava_jar/CodeStyloJava.jar
   ```

5. **Configure the path** -- Choose one of:
   - Edit `data/extractfeatures_single.sh` line 7 (`CMD_DIR_NAIVEBASELINE` variable)
   - Set an environment variable in `~/.bashrc`:
     ```bash
     export CMD_DIR_NAIVEBASELINEJAR="<path-to>/CodeStyloJava/out/artifacts/CodeStyloJava_jar/CodeStyloJava.jar"
     ```
   - For the Python project, set `naivebaselinecmd` in `config.ini`

> **Note:** Pre-extracted Java-based features for the full dataset are already included. This setup is only required if you need to extract features for new files.
