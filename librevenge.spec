#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : librevenge
Version  : 0.0.4
Release  : 4
URL      : https://dev-www.libreoffice.org/src/librevenge-0.0.4.tar.bz2
Source0  : https://dev-www.libreoffice.org/src/librevenge-0.0.4.tar.bz2
Summary  : API library for generic document converters
Group    : Development/Tools
License  : LGPL-2.1 MPL-2.0-no-copyleft-exception
Requires: librevenge-lib
Requires: librevenge-license
BuildRequires : boost-dev
BuildRequires : doxygen
BuildRequires : pkgconfig(cppunit)
BuildRequires : pkgconfig(zlib)

%description
librevenge is a base library for writing document import filters. It has
interfaces for text documents, vector graphics, spreadsheets and presentations.

%package dev
Summary: dev components for the librevenge package.
Group: Development
Requires: librevenge-lib
Provides: librevenge-devel

%description dev
dev components for the librevenge package.


%package doc
Summary: doc components for the librevenge package.
Group: Documentation

%description doc
doc components for the librevenge package.


%package lib
Summary: lib components for the librevenge package.
Group: Libraries
Requires: librevenge-license

%description lib
lib components for the librevenge package.


%package license
Summary: license components for the librevenge package.
Group: Default

%description license
license components for the librevenge package.


%prep
%setup -q -n librevenge-0.0.4

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1534616723
%configure --disable-static --disable-werror
make  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1534616723
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/librevenge
cp COPYING.LGPL %{buildroot}/usr/share/doc/librevenge/COPYING.LGPL
cp COPYING.MPL %{buildroot}/usr/share/doc/librevenge/COPYING.MPL
%make_install

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/librevenge-0.0/librevenge-generators/RVNGCSVSpreadsheetGenerator.h
/usr/include/librevenge-0.0/librevenge-generators/RVNGHTMLTextGenerator.h
/usr/include/librevenge-0.0/librevenge-generators/RVNGRawDrawingGenerator.h
/usr/include/librevenge-0.0/librevenge-generators/RVNGRawPresentationGenerator.h
/usr/include/librevenge-0.0/librevenge-generators/RVNGRawSpreadsheetGenerator.h
/usr/include/librevenge-0.0/librevenge-generators/RVNGRawTextGenerator.h
/usr/include/librevenge-0.0/librevenge-generators/RVNGSVGPresentationGenerator.h
/usr/include/librevenge-0.0/librevenge-generators/RVNGTextDrawingGenerator.h
/usr/include/librevenge-0.0/librevenge-generators/RVNGTextPresentationGenerator.h
/usr/include/librevenge-0.0/librevenge-generators/RVNGTextSpreadsheetGenerator.h
/usr/include/librevenge-0.0/librevenge-generators/RVNGTextTextGenerator.h
/usr/include/librevenge-0.0/librevenge-generators/librevenge-generators-api.h
/usr/include/librevenge-0.0/librevenge-generators/librevenge-generators.h
/usr/include/librevenge-0.0/librevenge-stream/RVNGDirectoryStream.h
/usr/include/librevenge-0.0/librevenge-stream/RVNGStream.h
/usr/include/librevenge-0.0/librevenge-stream/RVNGStreamImplementation.h
/usr/include/librevenge-0.0/librevenge-stream/librevenge-stream-api.h
/usr/include/librevenge-0.0/librevenge-stream/librevenge-stream.h
/usr/include/librevenge-0.0/librevenge/RVNGBinaryData.h
/usr/include/librevenge-0.0/librevenge/RVNGDrawingInterface.h
/usr/include/librevenge-0.0/librevenge/RVNGPresentationInterface.h
/usr/include/librevenge-0.0/librevenge/RVNGProperty.h
/usr/include/librevenge-0.0/librevenge/RVNGPropertyList.h
/usr/include/librevenge-0.0/librevenge/RVNGPropertyListVector.h
/usr/include/librevenge-0.0/librevenge/RVNGSVGDrawingGenerator.h
/usr/include/librevenge-0.0/librevenge/RVNGSpreadsheetInterface.h
/usr/include/librevenge-0.0/librevenge/RVNGString.h
/usr/include/librevenge-0.0/librevenge/RVNGStringVector.h
/usr/include/librevenge-0.0/librevenge/RVNGTextInterface.h
/usr/include/librevenge-0.0/librevenge/librevenge-api.h
/usr/include/librevenge-0.0/librevenge/librevenge.h
/usr/lib64/librevenge-0.0.so
/usr/lib64/librevenge-generators-0.0.so
/usr/lib64/librevenge-stream-0.0.so
/usr/lib64/pkgconfig/librevenge-0.0.pc
/usr/lib64/pkgconfig/librevenge-generators-0.0.pc
/usr/lib64/pkgconfig/librevenge-stream-0.0.pc

%files doc
%defattr(0644,root,root,0755)
%doc /usr/share/doc/librevenge/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/librevenge-0.0.so.0
/usr/lib64/librevenge-0.0.so.0.0.4
/usr/lib64/librevenge-generators-0.0.so.0
/usr/lib64/librevenge-generators-0.0.so.0.0.4
/usr/lib64/librevenge-stream-0.0.so.0
/usr/lib64/librevenge-stream-0.0.so.0.0.4

%files license
%defattr(-,root,root,-)
/usr/share/doc/librevenge/COPYING.LGPL
/usr/share/doc/librevenge/COPYING.MPL
