# Makefile for source rpm: zip
# $Id$
NAME := zip
SPECFILE = $(firstword $(wildcard *.spec))

include ../common/Makefile.common
