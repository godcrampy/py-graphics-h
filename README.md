# PYCC: Python Parser for graphics.h

This is a CLI to read, interpret and execute C programs having `graphics.h` dependency. At its core, it is a small
interpreter for C with support for `graphics.h`

### Supported Functions

* `initgraph`
* `getchar` or `getch`
* `closegraph`
* `outtextxy`
* `setcolor`
* `arc`
* `bar`
* `line`
* `rectangle`
* `ellipse`
* `fillellipse`
* `fillpoly`
* `fillcircle`
* `drawpoly`
* `getfontcolor`
* `pieslice`
* `sector`
* `cleardevice`
* `getmaxx`
* `getmaxx`

### Major Things Not Supported Yet

* Control Flow
* Function Definitions
* Function calls other than the ones mentioned above

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing
purposes.

### Prerequisites

You need `pipenv` or any other virtual environment tool.

```shell
$ pip install pipenv
```

### Installing

Install the dependencies:

```shell
$ pipenv install
```

### Usage

```shell
# setup shell in root of this repo
$ pipenv shell

$ ./pycc <path/to/main.c>
```

### Running Samples

```shell
$ ./pycc samples/sample.c

$ ./pycc samples/car.c 

$ ./pycc samples/smiley.c 
```

## Running the tests

### Unit Tests

```shell
$ pipenv run test
```

### Coverage

```shell
$ pipenv run cov
```

## Built With

* [pycparser](https://github.com/eliben/pycparser) - Complete C99 parser in pure Python
* [PyEasyGraphics](https://github.com/royqh1979/PyEasyGraphics) - A Turbo C Graphics Style Graphics library for python
* [pytest](https://docs.pytest.org/en/stable/) - Testing

## License

This project is licensed under the MIT License - see
the [LICENSE](https://github.com/godcrampy/py-graphics-h/blob/main/LICENSE) file for details
