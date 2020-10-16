# Installation

```sh
pip3 install requests
```

# Directory Structure

You should have a directory named `data`,

inside the `data` directory, if the problem id is **12880**,

the input file name should be **12880_00.in**, **12880_01.in**, ....

the output file name should be **12880_00.out**, **12880_01.out**, ...

For example:

```
hw3-12880
├── data
│   ├── 12880_00.in
│   ├── 12880_00.out
│   ├── 12880_01.in
│   ├── 12880_01.out
│   ├── 12880_02.in
│   ├── 12880_02.out
│   ├── 12880_03.in
│   ├── 12880_03.out
│   ├── 12880_04.in
│   └── 12880_04.out
├── generate.py
├── solution.c
└── upload.py
```

# Usage

```sh
python3 upload.py
```

Enter the username, password, problem_id and the number of testcases.

Then all files should be uploaded.
