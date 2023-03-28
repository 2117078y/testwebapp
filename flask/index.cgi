#! /home/xs522872/miniconda3/envs/condapy310/bin/python3.10
from wsgiref.handlers import CGIHandler
from hello import app

CGIHandler().run(app)