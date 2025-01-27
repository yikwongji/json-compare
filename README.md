# JSON Key Comparator

This Python script compares two JSON files and checks if they have the same keys (IDs). If the keys are not the same, it lists the keys that are unique to each file.

## Table of Contents
- [Introduction](#introduction)
- [Requirements](#requirements)
- [Usage](#usage)
- [How It Works](#how-it-works)
- [Example](#example)
- [License](#license)

## Introduction
When working with JSON files, it's often necessary to compare their structures, especially when dealing with localization files, configuration files, or any data stored in JSON format. This script helps you quickly identify differences in the keys between two JSON files.

## Requirements
- Python 3.x
- Two JSON files to compare

## Usage
1. Clone or download this repository.
2. Ensure you have two JSON files to compare.
3. Update the `file1` and `file2` variables in the script with the paths to your JSON files.
4. Run the script using Python:

   ```bash
   python compare_json_keys.py