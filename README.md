# diffusion2d

## Instructions for students

Please follow the instructions in [pypi_exercise.md](https://github.com/Simulation-Software-Engineering/Lecture-Material/blob/main/03_building_and_packaging/pypi_exercise.md).

The code used in this exercise is based on [Chapter 7 of the book "Learning Scientific Programming with Python"](https://scipython.com/book/chapter-7-matplotlib/examples/the-two-dimensional-diffusion-equation/).

## Description

This package solves the two-dimensional diffusion equation using finite difference methods. The implementation simulates heat diffusion in a square plate with initial conditions: a cold square domain (300 K) with a hot circular disc (700 K) at the center. The simulation uses forward-difference in time and central-difference in space to propagate the temperature field over time.

## Installing the package

```bash
pip install elsherzd_diffusion2d
```

## Running this package

```python
from elsherzd_diffusion2d import solve
solve()
```
