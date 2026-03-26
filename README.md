---

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

### 🎯 Core Gameplay

* Ship movement with keyboard controls
* Bullet firing system
* Alien fleet generation and movement
* Collision detection (bullets, aliens, ship)
* Score tracking and high score system
* Limited lives and game-over condition

---

## 🧠 Adaptive Difficulty System (Custom Feature)

This game includes a **two-level adaptive difficulty system**:

### 1. 📊 Cross-Game Adaptation (Persistent)

* Stores performance from the last **4–5 games**
* Calculates **average accuracy**
* Sets **initial alien speed** for the next game based on past performance

### 2. ⚡ Real-Time Adaptation (In-Game)

* Tracks the last **15 shots** *(hit = 1, miss = 0)*
* Computes **rolling accuracy continuously**

**Dynamic Adjustment:**

* High accuracy → speed increases
* Low accuracy → speed decreases

### 3. ⏳ Stability Mechanisms

* Cooldown system prevents rapid difficulty changes
* Speed is clamped within safe limits

**Result:**
The game adapts both **between sessions** and **during gameplay**, creating a smoother and more personalized challenge.

---

## 📈 Adaptive Logic (Simplified)

```python
# Track last N shots (N = 15)
shots = [1, 0, 1, 1, 0, ...]  # 1 = hit, 0 = miss

accuracy = sum(shots) / len(shots)

if N==15 and COOL_DOWN_PASSED:
    if accuracy > HIGH_THRESHOLD:
        alien_speed += SPEED_STEP
    elif accuracy < LOW_THRESHOLD:
        alien_speed -= SPEED_STEP

# Stability controls
alien_speed = clamp(alien_speed, MIN_SPEED, MAX_SPEED)

```

**Key Ideas:**

* Uses a **sliding window** instead of total accuracy → more responsive
* Applies **bounded updates** → avoids extreme difficulty spikes
* Introduces **cooldown** → prevents oscillations

---

## 🎮 Controls

| Action          | Key/Input          |
| --------------- | ------------------ |
| Move Ship       | Left / Right Arrow |
| Fire Bullets    | Spacebar           |
| Start Game      | Mouse Click        |
| Take Screenshot | **S Key**          |

---

## 📸 Screenshot Feature

**Take Screenshots:**
Press the **S key** during gameplay to instantly capture the current game screen.

**Automatic Saving:**
Screenshots are saved in the `screenshots/` folder, named sequentially:

* `screenshot_1.png`
* `screenshot_2.png`
* `screenshot_3.png`
* ...

**Easy Sharing:**
Use these images to share your high scores or memorable moments.

---

## 🔊 Sound Effects & Music

### 🎵 Background Music

* Plays a looping track (`when_started.wav`) on the main menu
* Switches to a different track (`while_playing.wav`) during gameplay

### 🔉 Sound Effects

* **Bullet Fired:** `shot_fired.wav`
* **Alien Hit:** `alien_collision.wav`
* **Ship Hit:** `ship_collision.wav`
* **Game Over:** `game_over.wav`

**Storage:**
All sound files are stored in the `sound_effects/` folder

---

## 🛠️ Technologies Used

* **Python 3**
* **Pygame**

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

---

## ⚙️ Installation and Setup

### 1. Install Dependencies

```bash
pip install pygame
```

### 2. Run the Game

```bash
python alien_invasion.py
```

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

* ✅ Core game complete
* ✅ Adaptive difficulty system implemented
* 🚧 Further improvements and experimentation ongoing

---

## 🧩 Design Philosophy

This project focuses on **bridging game development with intelligent systems** by introducing adaptive mechanics that:

* React to **player skill in real time**
* Maintain **engagement without frustration**
* Simulate **feedback-driven systems similar to early ML concepts**

---
