#!/bin/bash

cd AllegroREST/AllegroREST
dotnet run
cd ../../AllegroWebApi
source venv/bin/activate
python3 main.py
