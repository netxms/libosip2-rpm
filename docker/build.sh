#!/bin/bash

set -e

for V in 2 2023; do
   mock -r amazonlinux-$V-$(arch) --spec SPECS/*.spec --sources SOURCES
done

for V in 8 9; do
   mock -r rocky+epel-$V-$(arch) --spec SPECS/*.spec --sources SOURCES
done

for V in 40 41; do
   mock -r fedora-$V-$(arch) --spec SPECS/*.spec --sources SOURCES
done

cp /var/lib/mock/*/result/*.rpm /result/
