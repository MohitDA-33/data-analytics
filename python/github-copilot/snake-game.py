# We created a snake game using AI (github co-pilot) and pygame, a popular python library for making games.

"""A polished, single-file Snake game built with Pygame."""

import random

import pygame   # pygame is a python library for making games.


WINDOW_WIDTH = 960
WINDOW_HEIGHT = 640
CELL_SIZE = 24
BOARD_COLUMNS = 25
BOARD_ROWS = 21
BOARD_X = 32
BOARD_Y = 104
BOARD_WIDTH = BOARD_COLUMNS * CELL_SIZE
BOARD_HEIGHT = BOARD_ROWS * CELL_SIZE
MOVE_INTERVAL = 0.105

BACKGROUND = (16, 22, 29)
SURFACE = (24, 32, 41)
BOARD_COLOR = (19, 27, 34)
GRID_COLOR = (27, 37, 45)
TEXT = (235, 241, 238)
MUTED = (145, 160, 165)
ACCENT = (113, 220, 157)
SNAKE_COLOR = (83, 194, 133)
SNAKE_HEAD = (129, 235, 166)
FOOD_COLOR = (255, 116, 104)


class SnakeGame:
	def __init__(self):
		pygame.init()
		pygame.display.set_caption("Snake")
		self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
		self.clock = pygame.time.Clock()
		self.title_font = pygame.font.SysFont("segoeui", 30, bold=True)
		self.heading_font = pygame.font.SysFont("segoeui", 21, bold=True)
		self.body_font = pygame.font.SysFont("segoeui", 16)
		self.small_font = pygame.font.SysFont("segoeui", 13)
		self.best_score = 0
		self.reset()

	def reset(self, start=False):
		center = (BOARD_COLUMNS // 2, BOARD_ROWS // 2)
		self.snake = [center, (center[0] - 1, center[1]), (center[0] - 2, center[1])]
		self.direction = (1, 0)
		self.next_direction = self.direction
		self.score = 0
		self.food = self.new_food()
		self.elapsed = 0.0
		self.paused = False
		self.game_over = False
		self.started = start

	def new_food(self):
		empty_cells = [
			(x, y)
			for x in range(BOARD_COLUMNS)
			for y in range(BOARD_ROWS)
			if (x, y) not in self.snake
		]
		return random.choice(empty_cells) if empty_cells else None

	def handle_key(self, key):
		directions = {
			pygame.K_UP: (0, -1),
			pygame.K_w: (0, -1),
			pygame.K_DOWN: (0, 1),
			pygame.K_s: (0, 1),
			pygame.K_LEFT: (-1, 0),
			pygame.K_a: (-1, 0),
			pygame.K_RIGHT: (1, 0),
			pygame.K_d: (1, 0),
		}

		if key in (pygame.K_ESCAPE, pygame.K_q):
			return False
		if not self.started:
			if key in (pygame.K_RETURN, pygame.K_SPACE):
				self.started = True
			elif key == pygame.K_r:
				self.reset(start=True)
			return True
		if key in (pygame.K_RETURN, pygame.K_SPACE) and self.game_over:
			self.reset(start=True)
		elif key == pygame.K_SPACE:
			self.paused = not self.paused
		elif key == pygame.K_r:
			self.reset(start=True)
		elif key in directions and not self.game_over:
			candidate = directions[key]
			if candidate != (-self.direction[0], -self.direction[1]):
				self.next_direction = candidate
		return True

	def start_button_rect(self):
		center_x = BOARD_X + BOARD_WIDTH // 2
		center_y = BOARD_Y + BOARD_HEIGHT // 2
		return pygame.Rect(center_x - 86, center_y + 31, 172, 48)

	def handle_click(self, position):
		if not self.started and self.start_button_rect().collidepoint(position):
			self.started = True

	def update(self, delta_time):
		if not self.started or self.paused or self.game_over:
			return

		self.elapsed += delta_time
		while self.elapsed >= MOVE_INTERVAL and not self.game_over:
			self.elapsed -= MOVE_INTERVAL
			self.direction = self.next_direction
			head_x, head_y = self.snake[0]
			new_head = (head_x + self.direction[0], head_y + self.direction[1])
			growing = new_head == self.food
			body = self.snake if growing else self.snake[:-1]

			if (
				not 0 <= new_head[0] < BOARD_COLUMNS
				or not 0 <= new_head[1] < BOARD_ROWS
				or new_head in body
			):
				self.game_over = True
				break

			self.snake.insert(0, new_head)
			if growing:
				self.score += 10
				self.best_score = max(self.best_score, self.score)
				self.food = self.new_food()
				if self.food is None:
					self.game_over = True
			else:
				self.snake.pop()

	def draw_text(self, text, font, color, position, anchor="topleft"):
		image = font.render(text, True, color)
		rect = image.get_rect()
		setattr(rect, anchor, position)
		self.screen.blit(image, rect)

	def draw_board(self):
		board_rect = pygame.Rect(BOARD_X, BOARD_Y, BOARD_WIDTH, BOARD_HEIGHT)
		pygame.draw.rect(self.screen, BOARD_COLOR, board_rect, border_radius=8)

		for x in range(1, BOARD_COLUMNS):
			line_x = BOARD_X + x * CELL_SIZE
			pygame.draw.line(
				self.screen,
				GRID_COLOR,
				(line_x, BOARD_Y),
				(line_x, BOARD_Y + BOARD_HEIGHT),
			)
		for y in range(1, BOARD_ROWS):
			line_y = BOARD_Y + y * CELL_SIZE
			pygame.draw.line(
				self.screen,
				GRID_COLOR,
				(BOARD_X, line_y),
				(BOARD_X + BOARD_WIDTH, line_y),
			)

		if self.food is not None:
			food_rect = pygame.Rect(
				BOARD_X + self.food[0] * CELL_SIZE + 5,
				BOARD_Y + self.food[1] * CELL_SIZE + 5,
				CELL_SIZE - 10,
				CELL_SIZE - 10,
			)
			pygame.draw.ellipse(self.screen, FOOD_COLOR, food_rect)
			highlight = food_rect.move(3, 3).inflate(-9, -9)
			pygame.draw.ellipse(self.screen, (255, 190, 155), highlight)

		for index, (x, y) in enumerate(self.snake):
			segment = pygame.Rect(
				BOARD_X + x * CELL_SIZE + 2,
				BOARD_Y + y * CELL_SIZE + 2,
				CELL_SIZE - 4,
				CELL_SIZE - 4,
			)
			color = SNAKE_HEAD if index == 0 else SNAKE_COLOR
			pygame.draw.rect(self.screen, color, segment, border_radius=6)

	def draw_sidebar(self):
		panel_x = 666
		self.draw_text("YOUR RUN", self.small_font, MUTED, (panel_x, 112))
		self.draw_text(str(self.score).zfill(3), self.title_font, TEXT, (panel_x, 135))
		self.draw_text("BEST", self.small_font, MUTED, (panel_x, 195))
		self.draw_text(str(self.best_score).zfill(3), self.heading_font, ACCENT, (panel_x, 216))

		pygame.draw.line(self.screen, (47, 59, 66), (panel_x, 266), (928, 266), 1)
		self.draw_text("CONTROLS", self.small_font, MUTED, (panel_x, 288))

		controls = (
			("MOVE", "Arrow keys / WASD"),
			("PAUSE", "Space"),
			("RESTART", "R"),
			("QUIT", "Esc"),
		)
		for index, (action, key) in enumerate(controls):
			row_y = 322 + index * 38
			self.draw_text(action, self.small_font, MUTED, (panel_x, row_y))
			self.draw_text(key, self.body_font, TEXT, (panel_x, row_y + 16))

		pygame.draw.line(self.screen, (47, 59, 66), (panel_x, 497), (928, 497), 1)
		self.draw_text("EAT TO GROW", self.small_font, ACCENT, (panel_x, 519))
		self.draw_text("Avoid the walls and your tail.", self.body_font, MUTED, (panel_x, 543))

	def draw_overlay(self, title, subtitle):
		overlay = pygame.Surface((BOARD_WIDTH, BOARD_HEIGHT), pygame.SRCALPHA)
		overlay.fill((10, 15, 20, 185))
		self.screen.blit(overlay, (BOARD_X, BOARD_Y))
		center_x = BOARD_X + BOARD_WIDTH // 2
		center_y = BOARD_Y + BOARD_HEIGHT // 2
		self.draw_text(title, self.title_font, TEXT, (center_x, center_y - 18), "center")
		self.draw_text(subtitle, self.body_font, MUTED, (center_x, center_y + 20), "center")

	def draw_start_screen(self):
		overlay = pygame.Surface((BOARD_WIDTH, BOARD_HEIGHT), pygame.SRCALPHA)
		overlay.fill((10, 15, 20, 185))
		self.screen.blit(overlay, (BOARD_X, BOARD_Y))
		center_x = BOARD_X + BOARD_WIDTH // 2
		center_y = BOARD_Y + BOARD_HEIGHT // 2
		self.draw_text("Ready to play?", self.title_font, TEXT, (center_x, center_y - 39), "center")
		self.draw_text("Eat, grow, and avoid your tail.", self.body_font, MUTED, (center_x, center_y - 7), "center")

		button = self.start_button_rect()
		button_color = (139, 235, 175) if button.collidepoint(pygame.mouse.get_pos()) else ACCENT
		pygame.draw.rect(self.screen, button_color, button, border_radius=8)
		self.draw_text("START", self.heading_font, BACKGROUND, button.center, "center")

	def draw(self):
		self.screen.fill(BACKGROUND)
		self.draw_text("SNAKE", self.title_font, TEXT, (32, 34))
		self.draw_text("CLASSIC ARCADE", self.small_font, MUTED, (34, 72))
		pygame.draw.line(self.screen, (47, 59, 66), (32, 91), (928, 91), 1)

		self.draw_board()
		self.draw_sidebar()
		if self.game_over:
			self.draw_overlay("Game over", "Press Space or Enter to play again")
		elif self.paused:
			self.draw_overlay("Paused", "Press Space to continue")
		elif not self.started:
			self.draw_start_screen()

		pygame.display.flip()

	def run(self):
		running = True
		while running:
			delta_time = min(self.clock.tick(60) / 1000, 0.1)
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					running = False
				elif event.type == pygame.KEYDOWN:
					running = self.handle_key(event.key)
				elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
					self.handle_click(event.pos)

			self.update(delta_time)
			self.draw()

		pygame.quit()


def main():
	SnakeGame().run()


if __name__ == "__main__":
	main()
