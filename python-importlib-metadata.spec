%define pypi_name	importlib-metadata

Name:		python-%{pypi_name}
Summary:	Library to access the metadata for a Python package.
Version:	3.7.2
Release:	1
Group:		Development/Python
License:	Apache 2.0
URL:		https://github.com/python/importlib_metadata
Source0:	https://files.pythonhosted.org/packages/48/18/08eaa583eb21602e86e32d534fa7f40159774566037e60a69822b10ef3ad/importlib_metadata-%{version}.tar.gz
BuildArch:	noarch

BuildRequires:	pkgconfig(python)
BuildRequires:	python3dist(setuptools)
BuildRequires:	python3dist(setuptools-scm)
BuildRequires:  python3dist(pip)

%{?python_provide:%python_provide python3-%{pypi_name}}

%description
importlib_metadata is a library which provides an API for accessing an installed package’s metadata (see PEP 566), such as its entry points or its top-level name.
This functionality intends to replace most uses of pkg_resources entry point API and metadata API. 
Along with importlib.resources in Python 3.7 and newer (backported as importlib_resources for older versions of Python), 
this can eliminate the need to use the older and less efficient pkg_resources package.

%prep
%setup -q -n importlib_metadata-%{version}

# drop bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py_build

%install
%py_install

%files
%doc README.rst CHANGES.rst
%{python_sitelib}/*egg-info
%{python_sitelib}/%{pypi_name}
