EXTERNALLIBS = -lgsl -lgslcblas
LIBCPP = src/WilcoxonTest.cpp
LIBOBJS_NAME = WilcoxonTest.o
LIBOBJS = obj/$(LIBOBJS_NAME)
LIBRARY_NAME = libwilcoxontest.so
LIBRARY = lib/$(LIBRARY_NAME)
HEADER_NAME = WilcoxonTest.h
HEADER = src/$(HEADER_NAME)
INSTALL_LIB = /usr/lib/
INSTALL_HEADER = /usr/include/

TESTCPP = test/test.cpp
TESTEXECUTABLE = rumDemTests

PKG_LIBS = -lgsl

all: $(LIBRARY)

Rcpp: $(LIBCPP)
	R CMD SHLIB $(LIBCPP) -L$(INSTALL_HEADER) $(PKG_LIBS)

install: all
				sudo cp -r $(LIBRARY) $(INSTALL_LIB)
				sudo cp -r $(HEADER) $(INSTALL_HEADER)
				sudo mkdir -p /usr/lib/wilcoxonTest
				sudo cp -rf approximateTable500.txt /usr/lib/wilcoxonTest
				sudo ldconfig

uninstall:
				sudo rm -f $(INSTALL_LIB)$(LIBRARY_NAME)
				sudo rm -f $(INSTALL_HEADER)$(HEADER_NAME)
				sudo rm -rf /usr/lib/wilcoxonTest
				sudo ldconfig

test: $(TESTEXECUTABLE)

$(TESTEXECUTABLE): $(TESTCPP) $(LIBRARY)
	@mkdir -p $(@D)
	 g++ -Wall -ggdb -o $@ $^ -Itest -Isrc $(EXTERNALLIBS)

$(LIBRARY): $(LIBOBJS)
	@mkdir -p $(@D)
	g++ -shared -Wl,-soname,$(LIBRARY_NAME).1 $(EXTERNALLIBS) \
	-o $@ $^

$(LIBOBJS): $(LIBCPP)
	@mkdir -p $(@D)
	g++ -Wall -fpic -c $^ -o $@

$(ARCHIVE): $(ARCHIVE_LIBOBJS)
	@mkdir -p $(@D)
	ar -cr $@ $^

$(ARCHIVE_LIBOBJS): $(LIBCPP)
	@mkdir -p $(@D)
	g++ -Wall -ggdb -c $^ -o $@

clean:
	rm -rf obj/*
	rm -rf lib/*
	rm -rf bin/Debug/*
	rm -rf src/WilcoxonTest.o
	rm -rf src/WilcoxonTest.so
	rm -rf Rcpp
	rm -rf rumDemTests 
  
distclean:
	rm -rf obj
	rm -rf lib
	rm -rf bin
	rm -rf src/WilcoxonTest.o
	rm -rf src/WilcoxonTest.so
	rm -rf Rcpp
	rm -rf rumDemTests
