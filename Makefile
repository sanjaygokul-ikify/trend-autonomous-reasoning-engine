# Makefile for Autonomous Reasoning Engine

install:
	pip install -r requirements.txt

run:
	python main.py

eval:
	python evaluation.py