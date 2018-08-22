#!/usr/bin/env bash
set -e

for n in `find testcases/ -type f \( -name "*.json" -o -name "*.yml" \)`; do
    exec hrun ${n}
done