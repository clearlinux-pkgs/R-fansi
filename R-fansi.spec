#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-fansi
Version  : 0.3.0
Release  : 3
URL      : https://cran.r-project.org/src/contrib/fansi_0.3.0.tar.gz
Source0  : https://cran.r-project.org/src/contrib/fansi_0.3.0.tar.gz
Summary  : ANSI Control Sequence Aware String Functions
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-fansi-lib
BuildRequires : R-markdown
BuildRequires : buildreq-R

%description
the effects of ANSI text formatting control sequences.

%package lib
Summary: lib components for the R-fansi package.
Group: Libraries

%description lib
lib components for the R-fansi package.


%prep
%setup -q -c -n fansi

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1537768154

%install
rm -rf %{buildroot}
export SOURCE_DATE_EPOCH=1537768154
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library fansi
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library fansi
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library fansi
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library fansi|| : 
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/fansi/DESCRIPTION
/usr/lib64/R/library/fansi/INDEX
/usr/lib64/R/library/fansi/Meta/Rd.rds
/usr/lib64/R/library/fansi/Meta/features.rds
/usr/lib64/R/library/fansi/Meta/hsearch.rds
/usr/lib64/R/library/fansi/Meta/links.rds
/usr/lib64/R/library/fansi/Meta/nsInfo.rds
/usr/lib64/R/library/fansi/Meta/package.rds
/usr/lib64/R/library/fansi/Meta/vignette.rds
/usr/lib64/R/library/fansi/NAMESPACE
/usr/lib64/R/library/fansi/NEWS.md
/usr/lib64/R/library/fansi/R/fansi
/usr/lib64/R/library/fansi/R/fansi.rdb
/usr/lib64/R/library/fansi/R/fansi.rdx
/usr/lib64/R/library/fansi/doc/index.html
/usr/lib64/R/library/fansi/doc/sgr-in-rmd.R
/usr/lib64/R/library/fansi/doc/sgr-in-rmd.Rmd
/usr/lib64/R/library/fansi/doc/sgr-in-rmd.html
/usr/lib64/R/library/fansi/help/AnIndex
/usr/lib64/R/library/fansi/help/aliases.rds
/usr/lib64/R/library/fansi/help/fansi.rdb
/usr/lib64/R/library/fansi/help/fansi.rdx
/usr/lib64/R/library/fansi/help/paths.rds
/usr/lib64/R/library/fansi/html/00Index.html
/usr/lib64/R/library/fansi/html/R.css
/usr/lib64/R/library/fansi/libs/symbols.rds

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/fansi/libs/fansi.so
/usr/lib64/R/library/fansi/libs/fansi.so.avx2
/usr/lib64/R/library/fansi/libs/fansi.so.avx512
