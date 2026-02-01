# Asteroids Game [LP#3]

A 2D arcade-style **Asteroids** game implemented in **Python**, built with modern tooling using **uv** for fast and reproducible dependency management.

This project recreates the classic spaceship game where the player navigates through floating asteroids, destroys them, and avoids collisions.

## Features

- Classic Asteroids-style gameplay  
- Written in Python and pygame with modular design  
- Uses **uv** for dependency and environment management  
- Simple graphics and responsive controls  
- Easy to run and extend  

## Requirements

- Python 3.8 or higher  
- `uv` package manager

Install `uv` if you don’t have it:

```bash
pip install uv
```
Or (recommended):
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

## Installation
Clone the repository:
```base
git clone https://github.com/GurusharanAK/asteroids.git
cd asteroids
```
Create the environment and install dependencies:
```bash
uv sync
```
This automatically sets up a environment and installs all required packages.

## Running the Game
Run the game using  `uv`:
```bash
uv run main.py
```
## Controls 
- **A** – Rotate left
- **D** – Rotate right
- **W** – Thrust forward
- **Space** – Shoot

---
---
---
## Project Structure
- `main.py` – Main game loop and entry point
- `player.py` – Player logic
- `asteroid.py` – Asteroid behavior
- `constants.py` – Game constants
- Other helper modules

## Why
- Object Oriented Programming
- Game Loop Architecture
- Event Handling & Input Processing
- Physics-Inspired Motion (Kinematics)
- Modular Software Design
- Dependency & Environment Management (uv)
