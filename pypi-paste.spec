#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-paste
Version  : 3.5.0
Release  : 90
URL      : https://files.pythonhosted.org/packages/b7/e0/eb502f90e14570c88ed108a101ff223ccc853e2ba057ac4e7d6eb40c923e/Paste-3.5.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/b7/e0/eb502f90e14570c88ed108a101ff223ccc853e2ba057ac4e7d6eb40c923e/Paste-3.5.0.tar.gz
Summary  : Tools for using a Web Server Gateway Interface stack
Group    : Development/Tools
License  : MIT
Requires: pypi-paste-license = %{version}-%{release}
Requires: pypi-paste-python = %{version}-%{release}
Requires: pypi-paste-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
Provides: Paste
Provides: Paste-python
Provides: Paste-python3
BuildRequires : pypi(pluggy)
BuildRequires : py-python
BuildRequires : pypi(setuptools)
BuildRequires : pypi(six)
BuildRequires : pytest
BuildRequires : tox
BuildRequires : pypi(virtualenv)

%description
Paste provides several pieces of "middleware" (or filters) that can be nested
to build web applications. Each piece of middleware uses the WSGI (PEP 333)
interface, and should be compatible with other middleware based on those
interfaces.

%package license
Summary: license components for the pypi-paste package.
Group: Default

%description license
license components for the pypi-paste package.


%package python
Summary: python components for the pypi-paste package.
Group: Default
Requires: pypi-paste-python3 = %{version}-%{release}

%description python
python components for the pypi-paste package.


%package python3
Summary: python3 components for the pypi-paste package.
Group: Default
Requires: python3-core
Provides: pypi(paste)
Requires: pypi(setuptools)
Requires: pypi(six)

%description python3
python3 components for the pypi-paste package.


%prep
%setup -q -n Paste-3.5.0
cd %{_builddir}/Paste-3.5.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1641466484
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-paste
cp %{_builddir}/Paste-3.5.0/docs/license.txt %{buildroot}/usr/share/package-licenses/pypi-paste/391729571488896efa70494919f96aab67116ad1
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-paste/391729571488896efa70494919f96aab67116ad1

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
