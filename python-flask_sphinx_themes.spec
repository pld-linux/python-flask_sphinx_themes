#
# Conditional build:
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	Sphinx themes for Flask and related projects
Summary(pl.UTF-8):	Motywy Sphinksa dla Flaska i powiązanych projektów
Name:		python-flask_sphinx_themes
Version:	1.0.2
Release:	2
License:	BSD
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/flask-sphinx-themes/
Source0:	https://files.pythonhosted.org/packages/source/f/flask-sphinx-themes/Flask-Sphinx-Themes-%{version}.tar.gz
# Source0-md5:	333813fbba8e4956e69ddd70e6b9fbb3
URL:		https://pypi.org/project/flask-sphinx-themes/
%if %{with python2}
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.4
BuildRequires:	python3-setuptools
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains Sphinx themes for Flask and Flask related
projects.

%description -l pl.UTF-8
Ten pakiet zawiera motywy Sphinksa dla Flaska i projektów związanych z
Flaskiem.

%package -n python3-flask_sphinx_themes
Summary:	Sphinx themes for Flask and related projects
Summary(pl.UTF-8):	Motywy Sphinksa dla Flaska i powiązanych projektów
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.4

%description -n python3-flask_sphinx_themes
This package contains Sphinx themes for Flask and Flask related
projects.

%description -n python3-flask_sphinx_themes -l pl.UTF-8
Ten pakiet zawiera motywy Sphinksa dla Flaska i projektów związanych z
Flaskiem.

%prep
%setup -q -n Flask-Sphinx-Themes-%{version}

%build
%if %{with python2}
%py_build
%endif

%if %{with python3}
%py3_build
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
%doc LICENSE README.rst
%{py_sitescriptdir}/flask_sphinx_themes
%{py_sitescriptdir}/Flask_Sphinx_Themes-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-flask_sphinx_themes
%defattr(644,root,root,755)
%doc LICENSE README.rst
%{py3_sitescriptdir}/flask_sphinx_themes
%{py3_sitescriptdir}/Flask_Sphinx_Themes-%{version}-py*.egg-info
%endif
