#                  _ _     _
#    ___ ___ ___ _| |_|___| |_
#   |   |  _   _|   | |  _   _|
#   |  _|_| |___ ___|_|___  |
#   |_|                   |_|
#   makefile ( yupp, gcc )

# -- binary name (without prefix and extension)
BIN = ev3dev-c

# -- platform (core)
ifeq ($(OS),Windows_NT)
# WIN32
PLATFORM = __MINGW__
else
# UNIX
PLATFORM = __UNIX__
endif

TOP = ../..

# -- compilers
CC = gcc
CXX = g++
LINK = ar

# -- on EV3 BRICK
ifeq ($(PLATFORM),__UNIX__)
EV3 = $(if $(shell $(CC) -dM -E - < /dev/null | grep __ARM_ARCH_4T__),1,0)
else
EV3 = 0
endif

# -- yupp preprocessor
YUPP_HOME = $(TOP)/yupp

# -- perform preprocessing anywhere
# SKIP_PP = 0
# -- skip preprocessing on the EV3 brick (it's a bit slow), would be better to use pre-generated sources
SKIP_PP = $(EV3)
# -- skip preprocessing anywhere
# SKIP_PP = 1

ifeq ($(SKIP_PP),0)
PP = python -u $(YUPP_HOME)/yup.py
else
PP = @echo makefile: warning: preprocessing step is skipped,
endif

# -- output subdirectory
ifeq ($(PLATFORM),__MINGW__)
D_PLATFORM = mingw
else
D_PLATFORM =
endif

# -- install directory
ifeq ($(PLATFORM),__MINGW__)
D_INSTALL = $(MINGW_HOME)
else
D_INSTALL = /usr/local
endif

# -- yupp import directories
D_YU = $(TOP)/source/ev3

# -- source directories
D_C = . $(TOP)/3d_party

ifeq ($(EV3),0)
D_C := $(D_C) ev3_link
endif

D_CXX = $(D_C)
D_ASM = $(TOP)/source

# -- include directories
D_H = $(D_C)

# -- binary directory
D_BIN = $(TOP)/lib
D_BIN := $(if $(D_PLATFORM), $(D_BIN)/$(D_PLATFORM), $(D_BIN))

# -- object directory
D_OBJ = $(TOP)/object
D_OBJ := $(if $(D_PLATFORM), $(D_OBJ)/$(D_PLATFORM), $(D_OBJ))

# -- source code suffix
E_YU = .yu
E_YUH = .yu-h
E_YUC = .yu-c
E_YUCXX = .yu-cpp

E_H = .h
E_C = .c
E_CXX = .cpp
E_ASM = .asm

# -- object suffix
E_OBJ = .o

# -- binary suffix
ifeq ($(OS),Windows_NT)
E_BIN = .a
else
E_BIN = .a
endif

# -- binary full name
F_BIN = $(D_BIN)/lib$(BIN)$(E_BIN)

# -- link options
LFLAGS = rcs

# -- preprocessor flags
PPFLAGS = --pp-no-skip-c-comment -q $(addprefix -d, $(D_YU))

# -- compiler flags
CFLAGS = $(addprefix -I, $(D_H)) -O2 -W -Wall -Wno-comment -std=gnu99

ifeq ($(PLATFORM),__UNIX__)
CFLAGS := $(CFLAGS) -fPIC
endif

CXXFLAGS = $(addprefix -I, $(D_H)) -O2 -ffast-math -funroll-loops -fno-exceptions -fomit-frame-pointer -g -W -Wall -Wno-comment

ifeq ($(PLATFORM),__UNIX__)
CXXFLAGS := $(CXXFLAGS) -fPIC
endif

ASMFLAGS = -Wall

# ---------------------------------
#   files lists
# ---------------------------------

S_YU = $(wildcard $(addsuffix /*$(E_YU), $(D_YU)))
S_YUH = $(wildcard $(addsuffix /*$(E_YUH), $(D_H)))
S_YUC = $(wildcard $(addsuffix /*$(E_YUC), $(D_C)))
S_YUCXX = $(wildcard $(addsuffix /*$(E_YUCXX), $(D_CXX)))

G_CXX = $(addsuffix $(E_CXX), $(basename $(S_YUCXX)))
G_C = $(addsuffix $(E_C), $(basename $(S_YUC)))
G_H = $(addsuffix $(E_H), $(basename $(S_YUH)))

S_C = $(sort $(wildcard $(addsuffix /*$(E_C), $(D_C))) $(G_C))
S_CXX = $(sort $(wildcard $(addsuffix /*$(E_CXX), $(D_CXX))) $(G_CXX))
S_ASM = $(wildcard $(addsuffix /*$(E_ASM), $(D_ASM)))

O_CXX = $(addprefix $(D_OBJ)/, $(addsuffix $(E_OBJ), $(basename $(notdir $(S_CXX)))))
O_C = $(addprefix $(D_OBJ)/, $(addsuffix $(E_OBJ), $(basename $(notdir $(S_C)))))
O_ASM = $(addprefix $(D_OBJ)/, $(addsuffix $(E_OBJ), $(basename $(notdir $(S_ASM)))))

O = $(O_CXX) $(O_C) $(O_ASM)

# ---------------------------------
#   commands
# ---------------------------------

# -- wrap compiler arguments
ifeq ($(OS),Windows_NT)
# -- too long command line workaround
define wrap
	echo $2 > args
	$1 @args
	-rm args
endef
else
define wrap
	$1 $2
endef
endif

# -- optional final tools
define final
endef

# -- removal list
R = $(F_BIN) $(O)

ifeq ($(SKIP_PP),0)
R := $(R) $(G_H) $(G_C) $(G_CXX)
endif

ifeq ($(OS),Windows_NT)
#CLEAN = cmd /c "del $(subst /,\,$(R))"
CLEAN = rm -rf $(R)
else
CLEAN = rm -rf $(R)
endif

# -- install
define install
	cp -f $(F_BIN) $(D_INSTALL)/lib
	cp -f $(G_H) $(D_INSTALL)/include
endef

# ---------------------------------
#   make rules
# ---------------------------------

vpath %$(E_CXX) $(D_CXX)
vpath %$(E_C) $(D_C)
vpath %$(E_ASM) $(D_ASM)
vpath %$(E_YUCXX) $(D_CXX)
vpath %$(E_YUC) $(D_C)

# -- build project
.PHONY: all

all: $(F_BIN)

$(F_BIN): $(O)
	$(call wrap,$(LINK),$(LFLAGS) $@ $^)
	$(call final,$@)
	@echo "*** $(F_BIN) ***"

$(G_C) $(G_CXX) $(G_H): $(S_YU)

$(G_C): %$(E_C): %$(E_YUC)
	$(call wrap,$(PP),$(PPFLAGS) $<)

$(G_CXX): %$(E_CXX): %$(E_YUCXX)
	$(call wrap,$(PP),$(PPFLAGS) $<)

$(G_H): %$(E_H): %$(E_YUH)
	$(call wrap,$(PP),$(PPFLAGS) $<)

$(S_C) $(S_CXX): $(G_H)

$(O_C): $(D_OBJ)/%$(E_OBJ): %$(E_C)
	$(call wrap,$(CC),$(CFLAGS) -c $< -o $@)

$(O_CXX): $(D_OBJ)/%$(E_OBJ): %$(E_CXX)
	$(call wrap,$(CXX),$(CXXFLAGS) -c $< -o $@)

$(O_ASM): $(D_OBJ)/%$(E_OBJ): %$(E_ASM)
	$(call wrap,$(CC),$(ASMFLAGS) -c $< -o $@)

# -- remove temporary files
.PHONY: clean

clean:
	$(CLEAN)

# -- install project
.PHONY: install

install:
	$(call install)

# -- EOF
