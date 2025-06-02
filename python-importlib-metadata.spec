%define pypi_name	importlib-metadata
%define oname importlib_metadata

Name:		python-%{pypi_name}
Summary:	Library to access the metadata for a Python package.
Version:	8.7.0
Release:	1
Group:		Development/Python
License:	Apache 2.0
URL:		https://github.com/python/importlib_metadata
Source0:	https://files.pythonhosted.org/packages/source/i/%{pypi_name}/%{oname}-%{version}.tar.gz
BuildArch:	noarch

BuildRequires:	python
BuildRequires:	pkgconfig(python)
BuildRequires:	python%{py_ver}dist(setuptools)
BuildRequires:	python%{py_ver}dist(setuptools-scm)
BuildRequires:	python%{py_ver}dist(pip)
BuildRequires:	python%{py_ver}dist(zipp)
BuildRequires:	python%{py_ver}dist(tomli)
BuildRequires:	python%{py_ver}dist(wheel)

%{?python_provide:%python_provide python3-%{pypi_name}}

%description
importlib_metadata is a library which provides an API for accessing an installed package’s metadata (see PEP 566), such as its entry points or its top-level name.
This functionality intends to replace most uses of pkg_resources entry point API and metadata API. 
Along with importlib.resources in Python 3.7 and newer (backported as importlib_resources for older versions of Python), 
this can eliminate the need to use the older and less efficient pkg_resources package.

%prep
%autosetup -p1 -n %{oname}-%{version}
# drop bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
export SETUPTOOLS_SCM_PRETEND_VERSION="%{version}"
%py_build

%install
%py_install

%files
%{python_sitelib}/%{oname}-%{version}.dist-info
%{python_sitelib}/%{oname}
%doc README.rst NEWS.rst
%license LICENSE
