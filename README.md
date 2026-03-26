# 🚀 Alien Invasion

A 2D arcade-style space shooter built using **Python** and **Pygame**, based on the *Alien Invasion* project from *Python Crash Course* by Eric Matthes.

This version extends the original game by adding a **real-time adaptive difficulty system**, making gameplay more dynamic and responsive to player performance.

---

## 🎮 Overview

The player controls a spaceship at the bottom of the screen and must eliminate a fleet of descending aliens.

Unlike the base version, this game:

* Adapts difficulty in real time
* Responds to player accuracy
* Maintains a balanced challenge

---

## ✨ Features

### Core Gameplay

* Ship movement with keyboard controls
* Bullet firing system
* Alien fleet generation and movement
* Collision detection (bullets, aliens, ship)
* Score tracking and high score system
* Limited lives and game-over condition

---

### 🧠 Adaptive Difficulty System (Custom Feature)

This game includes a **two-level adaptive difficulty system**:

#### 1. 📊 Cross-Game Adaptation (Persistent)

* Stores performance from the last **4–5 games**
* Calculates average accuracy
* Sets **initial alien speed** for the next game based on past performance

#### 2. ⚡ Real-Time Adaptation (In-Game)

* Tracks the last **15 shots** (hit = 1, miss = 0)
* Computes rolling accuracy continuously
* Adjusts alien speed dynamically:

  * High accuracy → speed increases
  * Low accuracy → speed decreases

#### 3. ⏳ Stability Mechanisms

* Cooldown system prevents rapid difficulty changes
* Speed is clamped within safe limits

---

**Result:**

> The game adapts both **between sessions** and **during gameplay**, creating a smoother and more personalized challenge.


---

## 🎮 Controls

* **Left / Right Arrow** → Move ship
* **Spacebar** → Fire bullets
* **Mouse Click** → Start game

---
## 📸 Screenshot Feature

- **Take Screenshots:**  
  Press the **S** key during gameplay to instantly capture the current game screen.
- **Automatic Saving:**  
  Screenshots are saved in the `screenshots/` folder, named sequentially (e.g., `screenshot_1.png`, `screenshot_2.png`, ...).
- **Easy Sharing:**  
  Use these images to share your high scores or memorable moments!

Files are named sequentially:
```
screenshot_1.png
screenshot_2.png
screenshot_3.png
...
```

## 🛠️ Technologies Used

* Python 3
* Pygame

---

## 📁 Project Structure
```
alien_invasion/
│
├── alien_invasion.py
├── settings.py
├── ship.py
├── bullet.py
├── alien.py
├── game_stats.py
├── scoreboard.py
├── images/
└── sound_effects/
```

## 🔊 Sound Effects & Music
```
- **Background Music:**  
  - Plays a looping track (`when_started.wav`) on the main menu.
  - Switches to a different track (`while_playing.wav`) during gameplay.
- **Sound Effects:**  
  - **Bullet Fired:** Plays `shot_fired.wav` when you shoot.
  - **Alien Hit:** Plays `alien_collision.wav` when an alien is destroyed.
  - **Ship Hit:** Plays `ship_collision.wav` when your ship is hit.
  - **Game Over:** Plays `game_over.wav` when the game ends.
- All sound files are stored in the `sound_effects/` folder.
---

## ⚙️ Installation and Setup

1. Install dependencies:

```
pip install pygame
```

2. Run the game:

```
python alien_invasion.py
```

---

## 📸 Screenshots

### Gameplay

*Add your gameplay screenshot here*

### Adaptive Difficulty in Action

*Add screenshot showing gameplay at different difficulty levels*

---

## 🚧 Future Enhancements

* Power-ups and special abilities
* Multiple enemy types
* Better UI/UX
* Difficulty visualization/debug panel

---

## 🙏 Acknowledgements

* Based on *Python Crash Course* by Eric Matthes
* Built using the Pygame library

---

## 📌 Status

Core game complete.
Adaptive difficulty system implemented.
Further improvements and experimentation ongoing.
