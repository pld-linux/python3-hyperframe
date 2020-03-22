#
# Conditional build:
%bcond_without	tests	# unit tests
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	HTTP/2 framing layer for Python 2
Summary(pl.UTF-8):	Warstwa ramek HTTP/2 dla Pythona 2
Name:		python-hyperframe
Version:	5.2.0
Release:	1
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/hyperframe/
Source0:	https://files.pythonhosted.org/packages/source/h/hyperframe/hyperframe-%{version}.tar.gz
# Source0-md5:	6919183242feb26d8bce3b4cba81defd
URL:		https://pypi.org/project/hyperframe/
%if %{with python2}
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-setuptools
%if %{with tests}
BuildRequires:	python-pytest
%endif
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.4
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-pytest
%endif
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.7
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

%package -n python3-hyperframe
Summary:	HTTP/2 framing layer for Python 3
Summary(pl.UTF-8):	Warstwa ramek HTTP/2 dla Pythona 3
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.4

%description -n python3-hyperframe
This library contains the HTTP/2 framing code used in the hyper
project. It provides a pure-Python codebase that is capable of
decoding a binary stream into HTTP/2 frames.

%description -n python3-hyperframe -l pl.UTF-8
Ta biblioteka zawiera kod obsługujący ramki HTTP/2, używany w
projekcie hyper. Zawiera czysto pythonową implementację, potrafiącą
dekodować strumień binary na ramki HTTP/2.

%prep
%setup -q -n hyperframe-%{version}

%build
%if %{with python2}
%py_build

%if %{with tests}
%{__python} -m pytest test
%endif
%endif

%if %{with python3}
%py3_build

%if %{with tests}
%{__python3} -m pytest test
%endif
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc CONTRIBUTORS.rst HISTORY.rst LICENSE README.rst
%{py_sitescriptdir}/hyperframe
%{py_sitescriptdir}/hyperframe-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-hyperframe
%defattr(644,root,root,755)
%doc CONTRIBUTORS.rst HISTORY.rst LICENSE README.rst
%{py3_sitescriptdir}/hyperframe
%{py3_sitescriptdir}/hyperframe-%{version}-py*.egg-info
%endif
