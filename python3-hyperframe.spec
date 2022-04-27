#
# Conditional build:
%bcond_without	doc	# Sphinx documentation
%bcond_without	tests	# unit tests
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	HTTP/2 framing layer for Python 3
Summary(pl.UTF-8):	Warstwa ramek HTTP/2 dla Pythona 3
Name:		python3-hyperframe
# keep in sync with python3-h2.spec
Version:	6.0.1
Release:	1
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/hyperframe/
Source0:	https://files.pythonhosted.org/packages/source/h/hyperframe/hyperframe-%{version}.tar.gz
# Source0-md5:	153c064e8ac654aaf136b3388c36de48
URL:		https://pypi.org/project/hyperframe/
BuildRequires:	python3-modules >= 1:3.6.1
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-pytest >= 6.0.1
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with doc}
BuildRequires:	sphinx-pdg >= 3.5.4
%endif
Requires:	python3-modules >= 1:3.6.1
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This library contains the HTTP/2 framing code used in the hyper
project. It provides a pure-Python codebase that is capable of
decoding a binary stream into HTTP/2 frames.

%description -l pl.UTF-8
Ta biblioteka zawiera kod obsługujący ramki HTTP/2, używany w
projekcie hyper. Zawiera czysto pythonową implementację, potrafiącą
dekodować strumień binary na ramki HTTP/2.

%package apidocs
Summary:	API documentation for Python hyperframe module
Summary(pl.UTF-8):	Dokumentacja API modułu Pythona hyperframe
Group:		Documentation

%description apidocs
API documentation for Python hyperframe module.

%description apidocs -l pl.UTF-8
Dokumentacja API modułu Pythona hyperframe.

%prep
%setup -q -n hyperframe-%{version}

%build
%py3_build

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
PYTHONPATH=$(pwd)/src \
%{__python3} -m pytest test
%endif

%if %{with doc}
PYTHONPATH=$(pwd)/src \
%{__make} -C docs html
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG.rst CONTRIBUTORS.rst LICENSE README.rst
%{py3_sitescriptdir}/hyperframe
%{py3_sitescriptdir}/hyperframe-%{version}-py*.egg-info

%if %{with doc}
%files apidocs
%defattr(644,root,root,755)
%doc docs/build/html/{_modules,_static,*.html,*.js}
%endif
