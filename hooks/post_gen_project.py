# -*- coding: utf-8 -*-

import os

# Get the root project directory
PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)

# Create empty folders because they can't be committed to Git
folders = ['_build', '_static', 'img']

for f in folders:
	os.makedirs(os.path.join(PROJECT_DIRECTORY, f), exist_ok=True)

print('📖 Created your documentation. Happy writing ✒')
