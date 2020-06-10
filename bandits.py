"""
Multi-armed bandit problem
"""

import numpy as np
import pygame
from pygame.locals import *


if __name__ == '__main__':
    """
    Main program
    """
    # Initialize the game
    pygame.init()
    width, height = 1264, 380
    screen = pygame.display.set_mode((width, height))

    # Define colors
    WHITE = (255, 255, 255)

    # Load fonts
    game_font = pygame.font.SysFont('Sans', 18)

    # Load images
    slot_machine_idle = pygame.image.load("assets/slot-machine-idle.png")
    slot_machine_win = pygame.image.load("assets/slot-machine-win.png")
    slot_machine_lose = pygame.image.load("assets/slot-machine-lose.png")
    slot_machine_best = pygame.image.load("assets/slot-machine-best.png")

    # Setting conversion rates and the number of samples
    conversion_rates = [0.13, 0.04, 0.18, 0.11, 0.05]
    N = 1000
    d = len(conversion_rates)

    # Creating the data set
    X = np.zeros((N, d))
    for i in range(N):
        for j in range(d):
            if np.random.rand() < conversion_rates[j]:
                X[i][j] = 1

    # Making arrays to count our losses and wins
    pos_rewards = np.zeros(d)
    neg_rewards = np.zeros(d)

    # Taking our best slot machine through beta distribution
    i = 0
    while True:
        if i < N:
            selected = 0
            max_random = 0
            for j in range(d):
                random_beta = np.random.beta(pos_rewards[j] + 1, neg_rewards[j] + 1)
                if random_beta > max_random:
                    max_random = random_beta
                    selected = j

            # Update the losses and wins
            if X[i][selected] == 1:
                pos_rewards[selected] += 1
            else:
                neg_rewards[selected] += 1

            # Clear the screen
            screen.fill(0)

            # Draw global stats
            pygame.draw.line(screen, WHITE, (200, 0), (200, height))
            screen.blit(game_font.render("Total rounds: {}".format(N), False, WHITE), (20, 15))
            screen.blit(game_font.render("Round: {}".format(i + 1), False, WHITE), (20, 35))

            # Draw slot machines stats
            for j in range(d):
                screen.blit(game_font.render("Slot machine nr. {}".format(j + 1),
                                             False, WHITE), (20, 75 + 60 * j))
                screen.blit(game_font.render("Wins / Losses: {} / {}".format(int(pos_rewards[j]), int(neg_rewards[j])),
                                             False, WHITE), (20, 95 + 60 * j))

            # If all the rounds are completed, we will mark the best slot machine
            if i == N - 1:
                selected = np.argmax(pos_rewards + neg_rewards)

            # Draw the slot machines
            for j in range(d):
                if j != selected:
                    screen.blit(slot_machine_idle, (240 + 200 * j, 10))
                else:
                    if i == N - 1:
                        screen.blit(slot_machine_best, (240 + 200 * j, 10))
                    elif X[i][j] == 1:
                        screen.blit(slot_machine_win, (240 + 200 * j, 10))
                    else:
                        screen.blit(slot_machine_lose, (240 + 200 * j, 10))

            # Update the screen
            pygame.display.flip()

            # Next round
            i = i + 1

        # Handle any incoming event
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit(0)

        # Sleep for a given time to display a nice animation
        pygame.time.wait(250)
