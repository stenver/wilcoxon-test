EXTERNALLIBS = -lwilcoxontest -lnetcdf_c++ -lgsl -lgslcblas -lboost_program_options
WILXAPP = src/WilcoxonTestLoader.cpp
CXX = g++
CXXFLAGS = -Wall -ggdb
#LIBCPP = src/WilcoxonTest.cpp
#LIBOBJS = obj/WilcoxonTest.o
#LIBRARY = lib/WilcoxonTest.a
EXECUTABLE = WilcoxonTest

all: $(EXECUTABLE)

$(EXECUTABLE): $(WILXAPP) $(EXTERNALLIBS)
	@mkdir -p $(@D)
	$(CXX) $(CXXFLAGS) -o $@ $^ -Isrc

Debug: $(EXECUTABLE)


clean:
	rm -rf obj/*
	rm -rf lib/*
	rm -rf bin/Debug/*
	rm -rf $(EXECUTABLE)

cleanAll:
	rm -rf obj
	rm -rf lib
	rm -rf bin
	rm -rf $(EXECUTABLE)
