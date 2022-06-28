#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-monotonic
Version  : 1.6
Release  : 52
URL      : https://files.pythonhosted.org/packages/ea/ca/8e91948b782ddfbd194f323e7e7d9ba12e5877addf04fb2bf8fca38e86ac/monotonic-1.6.tar.gz
Source0  : https://files.pythonhosted.org/packages/ea/ca/8e91948b782ddfbd194f323e7e7d9ba12e5877addf04fb2bf8fca38e86ac/monotonic-1.6.tar.gz
Summary  : An implementation of time.monotonic() for Python 2 & < 3.3
Group    : Development/Tools
License  : Apache-2.0
Requires: pypi-monotonic-license = %{version}-%{release}
Requires: pypi-monotonic-python = %{version}-%{release}
Requires: pypi-monotonic-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
monotonic
        ~~~~~~~~~
        
        This module provides a ``monotonic()`` function which returns the
        value (in fractional seconds) of a clock which never goes backwards.
        
        On Python 3.3 or newer, ``monotonic`` will be an alias of
        ``time.monotonic`` from the standard library. On older versions,

%package license
Summary: license components for the pypi-monotonic package.
Group: Default

%description license
license components for the pypi-monotonic package.


%package python
Summary: python components for the pypi-monotonic package.
Group: Default
Requires: pypi-monotonic-python3 = %{version}-%{release}

%description python
python components for the pypi-monotonic package.


%package python3
Summary: python3 components for the pypi-monotonic package.
Group: Default
Requires: python3-core
Provides: pypi(monotonic)

%description python3
python3 components for the pypi-monotonic package.


%prep
%setup -q -n monotonic-1.6
cd %{_builddir}/monotonic-1.6
pushd ..
cp -a monotonic-1.6 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1656393629
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
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-monotonic
cp %{_builddir}/monotonic-1.6/LICENSE %{buildroot}/usr/share/package-licenses/pypi-monotonic/c700a8b9312d24bdc57570f7d6a131cf63d89016
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
/usr/share/package-licenses/pypi-monotonic/c700a8b9312d24bdc57570f7d6a131cf63d89016

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
