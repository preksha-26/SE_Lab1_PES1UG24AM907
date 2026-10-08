import math
import random
from array import array

import pygame

from game.color_button import ColorButton

# ---- States ----
WATCH = "WATCH"
PLAYER_TURN = "PLAYER_TURN"
GAME_OVER = "GAME_OVER"

# ---- Task 2: playback speed (ms). Shrinks each round down to a floor. ----
FLASH_START, FLASH_MIN, FLASH_STEP = 600, 150, 40
PAUSE_START, PAUSE_MIN, PAUSE_STEP = 300, 80, 20
INTRO_DELAY = 700           # pause before each playback begins
CLICK_FLASH_MS = 200        # how long a clicked pad stays lit

# ---- Task 4: player-turn timer (ms) ----
TURN_BASE_MS = 3000         # fixed head start
TURN_PER_STEP_MS = 1000     # extra time per step in the pattern

BG = (24, 24, 32)
WHITE = (240, 240, 240)


def make_tone(freq, ms=300, volume=0.4, rate=44100):
    """Task 3: build a sine-wave Sound without needing numpy."""
    init = pygame.mixer.get_init()
    channels = init[2] if init else 1
    n = int(rate * ms / 1000)
    fade_in, fade_out = rate * 0.01, rate * 0.05
    buf = array("h")
    for i in range(n):
        env = min(1.0, i / fade_in, (n - i) / fade_out)   # avoids click noises
        s = int(32767 * volume * env * math.sin(2 * math.pi * freq * i / rate))
        for _ in range(channels):
            buf.append(s)
    return pygame.mixer.Sound(buffer=buf.tobytes())


class GameEngine:
    def __init__(self, width, height):
        self.width, self.height = width, height
        self.font_big = pygame.font.SysFont(None, 64)
        self.font = pygame.font.SysFont(None, 36)
        self.font_small = pygame.font.SysFont(None, 26)

        # Layout: header on top, 2x2 grid, timer bar at the bottom
        size, gap = 170, 16
        x0 = (width - (2 * size + gap)) // 2
        y0 = 90
        self.grid_left, self.grid_width = x0, 2 * size + gap
        specs = [  # (dim, lit, pitch) -> C4, E4, G4, C5
            ((110, 30, 30), (255, 80, 80), 261.63),    # Red
            ((30, 50, 120), (80, 130, 255), 329.63),   # Blue
            ((30, 110, 50), (80, 230, 110), 392.00),   # Green
            ((130, 120, 30), (255, 235, 80), 523.25),  # Yellow
        ]
        self.buttons = []
        for i, (dim, lit, freq) in enumerate(specs):
            r, c = divmod(i, 2)
            rect = (x0 + c * (size + gap), y0 + r * (size + gap), size, size)
            self.buttons.append(ColorButton(rect, dim, lit, freq))

        self.sounds = self._load_sounds()
        self.error_sound = self._load_error_sound()
        self.reset()

    # ---------- audio ----------
    def _load_sounds(self):
        try:
            if not pygame.mixer.get_init():
                pygame.mixer.init(44100, -16, 1, 512)
            return [make_tone(b.freq) for b in self.buttons]
        except pygame.error:
            return [None] * len(self.buttons)   # no audio device: game still runs

    def _load_error_sound(self):
        try:
            return make_tone(110, ms=500, volume=0.5)
        except pygame.error:
            return None

    def _play(self, idx):
        if self.sounds[idx]:
            self.sounds[idx].play()

    # ---------- state ----------
    def reset(self):
        self.sequence = []
        self.score = 0
        self.click_idx = None
        self.click_until = 0
        self._start_round()

    def _start_round(self):
        # Task 1 fix: exactly ONE new step per round
        self.sequence.append(random.randrange(len(self.buttons)))
        self.state = WATCH
        self.input_index = 0
        self.play_index = 0
        self.phase = "intro"
        self.phase_start = pygame.time.get_ticks()
        for b in self.buttons:
            b.lit = False

    @property
    def round_no(self):
        return len(self.sequence)

    def flash_ms(self):   # Task 2
        return max(FLASH_MIN, FLASH_START - (self.round_no - 1) * FLASH_STEP)

    def pause_ms(self):   # Task 2
        return max(PAUSE_MIN, PAUSE_START - (self.round_no - 1) * PAUSE_STEP)

    def turn_limit_ms(self):  # Task 4
        return TURN_BASE_MS + TURN_PER_STEP_MS * len(self.sequence)

    def _game_over(self):
        self.state = GAME_OVER
        for b in self.buttons:
            b.lit = False
        if self.error_sound:
            self.error_sound.play()

    # ---------- events ----------
    def handle_event(self, event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
            if self.state == GAME_OVER:
                self.reset()
        elif (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1
              and self.state == PLAYER_TURN):
            for idx, b in enumerate(self.buttons):
                if b.contains(event.pos):
                    self._player_pick(idx)
                    break

    def _player_pick(self, idx):
        now = pygame.time.get_ticks()
        self._unlight_click()
        self.click_idx, self.click_until = idx, now + CLICK_FLASH_MS
        self.buttons[idx].lit = True
        self._play(idx)

        if idx != self.sequence[self.input_index]:
            self._game_over()          # wrong pad -> immediate game over
            return
        self.input_index += 1
        if self.input_index == len(self.sequence):
            self.score += 1
            self._start_round()        # next round (adds one step)

    def _unlight_click(self):
        if self.click_idx is not None:
            self.buttons[self.click_idx].lit = False
            self.click_idx = None

    # ---------- update ----------
    def update(self):
        now = pygame.time.get_ticks()

        # click feedback fades out (also while the next round is starting)
        if self.click_idx is not None and now >= self.click_until:
            if self.state != WATCH or self.phase != "flash":
                self._unlight_click()

        if self.state == WATCH:
            self._update_watch(now)
        elif self.state == PLAYER_TURN:
            if now >= self.turn_deadline:   # Task 4: time ran out
                self._game_over()

    def _update_watch(self, now):
        elapsed = now - self.phase_start
        if self.phase == "intro":
            if elapsed >= INTRO_DELAY:
                self._begin_flash(now)
        elif self.phase == "flash":
            if elapsed >= self.flash_ms():
                self.buttons[self.sequence[self.play_index]].lit = False
                self.phase, self.phase_start = "gap", now
        elif self.phase == "gap":
            if elapsed >= self.pause_ms():
                self.play_index += 1
                if self.play_index >= len(self.sequence):
                    self.state = PLAYER_TURN
                    self.turn_start = now
                    self.turn_deadline = now + self.turn_limit_ms()
                else:
                    self._begin_flash(now)

    def _begin_flash(self, now):
        idx = self.sequence[self.play_index]
        self.buttons[idx].lit = True
        self._play(idx)
        self.phase, self.phase_start = "flash", now

    # ---------- render ----------
    def render(self, screen):
        screen.fill(BG)
        self._text(screen, self.font, f"Score: {self.score}", 20, 18, left=True)
        self._text(screen, self.font, f"Round {self.round_no}", self.width - 20, 18, right=True)

        status = {WATCH: "Watch the pattern...", PLAYER_TURN: "Your turn!",
                  GAME_OVER: "Game over"}[self.state]
        self._text(screen, self.font_small, status, self.width // 2, 62, center=True)

        for b in self.buttons:
            b.draw(screen)

        self._draw_timer(screen)
        if self.state == GAME_OVER:
            self._draw_game_over(screen)

    def _draw_timer(self, screen):
        bar = pygame.Rect(self.grid_left, 470, self.grid_width, 18)
        pygame.draw.rect(screen, (60, 60, 75), bar, border_radius=9)
        if self.state == PLAYER_TURN:
            frac = max(0.0, (self.turn_deadline - pygame.time.get_ticks()) / self.turn_limit_ms())
            color = (80, 220, 110) if frac > 0.5 else (240, 200, 60) if frac > 0.25 else (235, 70, 70)
            fill = bar.copy()
            fill.width = int(bar.width * frac)
            if fill.width > 0:
                pygame.draw.rect(screen, color, fill, border_radius=9)
        pygame.draw.rect(screen, WHITE, bar, 2, border_radius=9)

    def _draw_game_over(self, screen):
        overlay = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 175))
        screen.blit(overlay, (0, 0))
        cx, cy = self.width // 2, self.height // 2
        self._text(screen, self.font_big, "GAME OVER", cx, cy - 50, center=True)
        self._text(screen, self.font, f"Final score: {self.score}", cx, cy + 5, center=True)
        self._text(screen, self.font_small, "Press R to restart", cx, cy + 45, center=True)

    def _text(self, screen, font, msg, x, y, left=False, right=False, center=False):
        surf = font.render(msg, True, WHITE)
        rect = surf.get_rect()
        if center:
            rect.midtop = (x, y)
        elif right:
            rect.topright = (x, y)
        else:
            rect.topleft = (x, y)
        screen.blit(surf, rect)