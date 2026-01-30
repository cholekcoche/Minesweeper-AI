# Minesweeper-AI


# Python Minesweeper & AI Autonomous Solver

A robust, Object-Oriented Minesweeper implementation in Python. This project features a fully playable CLI game and an intelligent agent (Bot) that solves the board using deterministic logic and heuristic risk analysis.

##  Technical Features & Logic

This project implements several advanced programming and algorithmic techniques:

### 1. Object-Oriented Programming (OOP)

The system is built on a clean, class-based architecture to ensure scalability and separation of concerns:

* `Configuracion`: Manages game rules, board dimensions (perfect squares), and customizable "skins" for tiles.
* `Casilla`: An entity-level class storing tile state (bomb status, visual character, and weight values).
* `Partida`: The engine handling the game loop, coordinate validation, and board rendering.
* `Bot`: The AI agent that interacts with the game state to make autonomous moves.

### 2. Flood Fill Algorithm

The clearing logic uses a **Breadth-First Search (BFS)** style approach (often called **Flood Fill**). When a tile with 0 adjacent mines is revealed, the `Cambiar_valor` method automatically expands and clears all connected empty tiles until it hits a numbered boundary, providing the classic Minesweeper feel.

### 3. Deterministic Inference Solver

The Bot first attempts to solve the board with 100% certainty using **Constraint Satisfaction**:

* **Flagging Logic:** If a tile's number equals the count of surrounding hidden tiles, it marks them all as mines.
* **Safe Clearing:** If a tile's number equals the count of surrounding flags, it clears all remaining hidden neighbors as they are guaranteed to be safe.

### 4. Heuristic Weighting System (Decision under Uncertainty)

When the logic gets "stuck" (no 100% safe moves), the Bot switches to **Method 2**. It calculates a **probability-based weight** for each available tile based on nearby numbers. It then selects the tile with the lowest "risk score" to maximize the chances of survival during forced guesses.

### 5. Robust Input Validation

* **Safe-Start Generation:** The `set_bombas` method ensures the first click (and its immediate neighbors) is always safe.
* **Dynamic UI:** The CLI scales the coordinate axis automatically based on board size (supporting up to 3600 tiles).
* **Error Handling:** Uses `try/except` blocks to manage invalid user inputs without crashing the game.

##  Installation & Usage

1. **Clone the repo:**
```bash
git clone https://github.com/your-username/minesweeper-ai-solver.git

```


2. **Run the script:**
```bash
python main.py

```



##  Game Controls

* **1. Consultas:** Check current game settings.
* **2. Configuración:** Change board size or mine density.
* **3. Comenzar juego:** Enter the arena.
* Once inside, you can **Flag**, **Reveal**, or trigger the **Bot** to solve the board for you.
