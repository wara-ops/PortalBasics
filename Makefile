DATA_DIRS := "img/*"

SOURCE_DIR=$(shell basename $(CURDIR))
TARGET_NAME := 
ifdef TARGET_NAME
	TARGET_DIR := $(realpath ../../$(TARGET_NAME))
else
	TARGET_DIR := $(realpath ../../$(SOURCE_DIR))
endif
OBJECTS := $(wildcard *.ipynb) $(DATA_DIRS)
TARGET_OBJECTS := $(addprefix $(TARGET_DIR)/,$(OBJECTS))

include ../Makefile