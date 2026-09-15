#!/usr/bin/env python3
import secrets

answer_list = [
	"Yes!",
	"No!",
	"Maybe someday...",
	"Try again later.",
	"Absolutely not.",
	"Ask me again.",
	"It is certain.",
	"Probably.",
	"Not today.",
	"Only if you behave.",
	"Only if you believe.",
	"Linus Torvalds knows.",
	"Ask GNU.",
	"You already know.",
	"The answer is... no.",
	"Perhaps.",
	"Go outside...",
	"Go shower...",
	"Do it!",
	"Don't do it!",
	"...",
	"Let me think... KERNEL PANIC!",
	"Don't even think about it.",
	"sudo rm -fr --no-preserve-root",
	"KERNEL PANIC!",
	"Better install Windows...",
	"Linux isn't for you..."
	]

answer = secrets.choice(answer_list)

#ascii from https://www.asciiart.eu/art/ea1ab399bf03d655
tux_ascii = r'''
			  ----------------------------      .-"""-.
			<                              >   '       \
		          ----------------------------    |,.  ,-.  |
					             \    |()L( ()| |
						      \   |,'  `".| |
						          |.___.',| `
						         .j `--"' `  `.
						        / '        '   \
						       / /          `   `.
						      / /            `    .
						     / /              l   |
						    . ,               |   |
						    ,"`.             .|   |
						 _.'   ``.          | `..-'l
						|       `.`,        |      `.
						|         `.    __.j         )
						|__        |--""___|      ,-'
						   `"--...,+""""   `._,.-'
'''

width = 30

answer_replace = f"<{answer:^{width}}>"
tux_ascii = tux_ascii.replace("<" + (" " * width) + ">", answer_replace)

print(tux_ascii)
