#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-paste
Version  : 3.5.2
Release  : 98
URL      : https://files.pythonhosted.org/packages/4c/2b/2e44afea5f8e397a5ce0f7ef78a79647f2c21e3fd7a463bf3be13aa6e819/Paste-3.5.2.tar.gz
Source0  : https://files.pythonhosted.org/packages/4c/2b/2e44afea5f8e397a5ce0f7ef78a79647f2c21e3fd7a463bf3be13aa6e819/Paste-3.5.2.tar.gz
Summary  : Tools for using a Web Server Gateway Interface stack
Group    : Development/Tools
License  : MIT
Requires: pypi-paste-license = %{version}-%{release}
Requires: pypi-paste-python = %{version}-%{release}
Requires: pypi-paste-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(py)
BuildRequires : pypi(setuptools)
BuildRequires : pypi(six)
BuildRequires : pypi-pluggy
BuildRequires : pypi-pytest
BuildRequires : pypi-tox
BuildRequires : pypi-virtualenv

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
%setup -q -n Paste-3.5.2
cd %{_builddir}/Paste-3.5.2
pushd ..
cp -a Paste-3.5.2 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1661193369
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-paste
cp %{_builddir}/Paste-%{version}/docs/license.txt %{buildroot}/usr/share/package-licenses/pypi-paste/391729571488896efa70494919f96aab67116ad1
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

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
